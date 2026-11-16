import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import build_opener, HTTPRedirectHandler, Request

API = "https://agent.tinyfish.ai"
DRY_RUN = False
REQUEST_PLAN = []

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

def request(url, body=None):
    if DRY_RUN:
        REQUEST_PLAN.append({"method": "GET" if body is None else "POST", "url": url, "body": body})
        return {}
    key = os.environ.get("TINYFISH_API_KEY", "").strip()
    private_config = Path(__file__).with_name(".env")
    if not key and private_config.is_file():
        for line in private_config.read_text(encoding="utf-8-sig").splitlines():
            name, _, value = line.partition("=")
            if name.strip() == "TINYFISH_API_KEY":
                key = value.strip().strip("\"'")
                break
    if not key:
        raise SystemExit("Set TINYFISH_API_KEY for this process.")
    req = Request(url, data=json.dumps(body).encode() if body is not None else None,
                  headers={"X-API-Key": key, "Content-Type": "application/json"})
    try:
        with build_opener(NoRedirect()).open(req, timeout=90) as result:
            return json.load(result)
    except HTTPError as error:
        raise SystemExit(f"TinyFish HTTP {error.code}. Check saved jobs before retrying a start.") from None
    except OSError as error:
        raise SystemExit(f"TinyFish request failed ({type(error).__name__}). Check saved jobs before retrying a start.") from None

def official_url(value, hosts):
    url = urlsplit(value)
    if url.scheme != "https" or url.hostname not in hosts or url.username or url.password or url.port not in (None, 443):
        raise ValueError("Expected an HTTPS URL on an explicitly configured official hostname")
    return value

import argparse
from datetime import date
from urllib.parse import urlencode
from uuid import UUID

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--start", type=Path, help="Start one TinySet build using this input JSON")
    group.add_argument("--dataset-id", help="Read a page from an existing dataset")
    parser.add_argument("--rows", type=int, default=10, choices=range(10, 31), metavar="10..30")
    parser.add_argument("--after")
    parser.add_argument("--dry-run", action="store_true", help="Validate input and print the request plan without network access")
    args = parser.parse_args()
    DRY_RUN = args.dry_run
    if args.start:
        data = json.loads(args.start.read_text(encoding="utf-8"))
        start, end = (date.fromisoformat(data[field]) for field in ("since", "as_of"))
        if not 365 <= (end - start).days <= 550:
            parser.error("Use a 12 to 18 month window")
        query = json.dumps({field: data[field] for field in ("activity", "stage", "country", "since", "as_of")})
        prompt = ("Build a sourced dataset with one distinct comparable company per row. "
                  "Require a publicly documented round within the window. Include company, round date, "
                  "stage, country, fit reason, participating investors, deal source URL, lead partner, "
                  "and public investor intake URL when published. Include a boolean column named "
                  "has_documented_round, true only when the cited round date is inside the requested window. "
                  "Separate investor names with semicolons. Leave uncertain values empty. Input: " + query)
        result = request(API + "/v1/datasets", {"prompt": prompt, "target_rows": args.rows})
    else:
        path = API + "/v1/datasets/" + str(UUID(args.dataset_id)) + "/rows"
        result = request(path + ("?" + urlencode({"after": args.after}) if args.after else ""))
    print(json.dumps({"mode": "dry_run", "requests": REQUEST_PLAN} if DRY_RUN else result, indent=2))
