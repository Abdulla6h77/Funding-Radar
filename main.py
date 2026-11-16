import argparse
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

def valid_link(value):
    if not isinstance(value, str):
        return False
    url = urlsplit(value)
    return url.scheme == "https" and bool(url.hostname) and not (url.username or url.password)

def rank(request):
    if any(not request[field].strip() for field in ("activity", "stage", "country")):
        raise ValueError("Activity, stage, and country are required")
    start, end = (date.fromisoformat(request[key]) for key in ("since", "as_of"))
    if not 365 <= (end - start).days <= 550:
        raise ValueError("Use a 12 to 18 month comparison window")
    investors, companies = {}, set()
    aliases = {name.strip().casefold(): canonical.strip().casefold()
               for name, canonical in request.get("company_aliases", {}).items()}
    for deal in request["investments"]:
        when = date.fromisoformat(deal["round_date"])
        if not start <= when <= end or not valid_link(deal["source_url"]):
            continue
        if deal.get("comparable") is not True or not str(deal.get("fit_reason", "")).strip():
            continue
        company, investor = (deal[key].strip().casefold() for key in ("company", "investor"))
        company = aliases.get(company, company)
        if not company or not investor:
            continue
        companies.add(company)
        item = investors.setdefault(investor, {"investor": deal["investor"], "deals": {}, "route": None, "profile": None})
        score = 1 + 2 * (deal["stage"].casefold() == request["stage"].casefold()) + (deal["country"].casefold() == request["country"].casefold())
        evidence = {key: deal.get(key) for key in ("company", "round_date", "stage", "country", "lead_partner", "source_url", "fit_reason")}
        evidence["fit_score"] = score
        if company not in item["deals"] or item["deals"][company]["fit_score"] < score:
            item["deals"][company] = evidence
        if valid_link(deal.get("intake_url")):
            item["route"] = deal["intake_url"]
        if valid_link(deal.get("profile_source_url")) and deal.get("typical_cheque"):
            item["profile"] = {"typical_cheque": deal["typical_cheque"], "typical_stage": deal.get("typical_stage"), "source_url": deal["profile_source_url"]}
    ranked = []
    for item in investors.values():
        evidence = sorted(item["deals"].values(), key=lambda deal: (-deal["fit_score"], deal["company"]))
        score = sum(deal["fit_score"] for deal in evidence)
        ranked.append({"investor": item["investor"], "score": score, "matches": evidence,
                       "public_intake_url": item["route"], "profile": item["profile"],
                       "reason": "One point per comparable, two for matching stage and one for matching country."})
    ranked.sort(key=lambda item: (-item["score"], item["investor"].casefold()))
    return {"activity": request["activity"], "comparable_count": len(companies),
            "status": "sufficient_comparables" if len(companies) >= 10 else "insufficient_comparables", "ranked": ranked}

def tinyset_investments(pages):
    """Map TinySet rows with documented deal links into the ranking input."""
    for page in pages:
        for row in page["rows"]:
            data = row["data"]
            fields = ("company", "round_date", "stage", "country", "fit_reason")
            documented = data.get("has_documented_round", data.get("publicly_documented_round_in_window"))
            if documented is not True or not valid_link(data.get("deal_source_url")):
                continue
            if any(not isinstance(data.get(key), str) or not data[key].strip() for key in fields):
                continue
            try:
                date.fromisoformat(data["round_date"])
            except ValueError:
                continue
            names = data.get("participating_investors")
            if not isinstance(names, str):
                continue
            investors = [name.strip() for name in names.split(";") if name.strip()]
            for investor in investors:
                yield {
                    **{key: data[key] for key in fields},
                    "investor": investor,
                    "source_url": data["deal_source_url"],
                    "comparable": True,
                    # Multi-investor rows do not specify which firm owns these fields.
                    "lead_partner": data.get("lead_partner") if len(investors) == 1 else None,
                    "intake_url": data.get("public_investor_intake_url") if len(investors) == 1 else None,
                }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--tinyset-page", type=Path, action="append", default=[],
                        help="Rank one or more saved TinySet response pages")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8-sig"))
    mode = "offline_input"
    if args.tinyset_page:
        pages = [json.loads(path.read_text(encoding="utf-8-sig")) for path in args.tinyset_page]
        data["investments"] = list(tinyset_investments(pages))
        mode = "tinyset_provider_rows"
    result = {"mode": mode, **rank(data)}
    if args.tinyset_page:
        result["evidence_review"] = "Provider-reported deals; source links require independent review."
    print(json.dumps(result, indent=2))
