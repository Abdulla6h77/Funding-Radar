# Funding Radar specification

Source: `D:\tinyfish-details.md`, bounty 4 and its rulebook.

API or agentic app that turns a startup description into a reusable, evidence-backed investor ranking.

## TinyFish products

**Required: TinySet** for live comparable-company and funding evidence. Search, Fetch, and Agent are optional supporting endpoints.

## Official submission requirements

- **S1** Takes a short startup description as input (what it does, stage, country)
- **S2** Finds at least 10 similar companies that raised recently, from live sources (news, company and investor sites, founder posts, grant portals)
- **S3** Returns a ranked list of investors, each with: the similar companies they backed (with links), typical cheque size and stage, the partner who led the deal, and how to reach them (application form, open intake or warm-intro route)
- **S4** Explains why each investor ranks where they do
- **S5** Demo on at least three different startups
- **S6** Uses TinySet, with a short explanation of how it is used (Search, Fetch and Agent can help around it)

## Official approval criteria

- **A1** Every match is backed by a live link proving the investment
- **A2** Accurate: companies, rounds and investors match their sources
- **A3** Ranking makes sense for the startup described, not a generic top-VC list
- **A4** Works for any startup description, not a hardcoded few
- **A5** Output is reusable by other tools (an API or a JSON or CSV export)

## Official judging priorities

- **J1** Match quality: investors who genuinely back companies like this one, at this stage
- **J2** Proof: every match links to a real investment in a similar company
- **J3** Useful detail: cheque size, lead partner and a real way to reach them
- **J4** Ranking: a clear, sensible reason for the order
- **J5** Works across very different startups and markets

## Demo and acceptance tests

Demo at least three different startup descriptions. For each, aim to meet the official ten-comparable minimum using verifiable recent rounds and show the ranking and export.

- **A1** Find at least ten comparable companies with recent funding from live sources. Verify each ranked investor's linked investment evidence and exclude unsupported matches.
- **A2** Reconcile company identity, dates, round type, and investor participation against the source. Test duplicate syndication, name collisions, and conflicting amounts. Separate round size from individual cheque size.
- **A3** Rank by fit to the supplied activity, stage, and country and explain each position. Show backing links, typical cheque size and stage, lead partner, and a public application, intake, or warm-intro route. Mark unsupported details as unknown.
- **A4** Accept a short description including activity, stage, and country. Test three different startup descriptions plus an unplanned input in another market.
- **A5** Provide an API or JSON/CSV export and validate its schema, links, and reproducibility from the displayed ranking.

## Edge cases and security

Use public business intake routes and avoid private contact data. Test sparse sectors, undisclosed lead partners, cutoff dates, and investors with insufficient evidence. Report a shortfall explicitly.

Keep credentials, access tokens, and other people's personal data out of the build and demo. Use sanitized fixtures for failure tests and label fixture evidence separately from live evidence.

## Rulebook and submission deadline

- Deadline: Tuesday, November 17, 2026 at 11:59 PM Pacific (Wednesday, November 18 at 12:59 PM Pakistan time).
- Enter through the TinyFish Students or Ambassadors program. One person per build and one entry per person per bounty. Claims do not reserve a bounty, and submissions are final.
- Provide a working build link (repo, live demo, or cookbook PR) with notes on what it does and how TinyFish is used. Post about the build on LinkedIn and tag TinyFish. Share it in Discord #showcase. X is optional.
- Pass every approval criterion. Use original work built for the bounty and demonstrate meaningful live TinyFish work end to end across varied inputs. Keep the submitted evidence authentic.
- The launch-exclusive listing advertises 200 winner points and 50 for other valid entries. The general rulebook separately gives 50/100/150/200 points for 1/2/3/4+ meaningful endpoints and describes top-three approvals. It names Search, Fetch, Agent, Browser, and Monitor, without stating how the required launch product counts. Confirm how these rules interact before relying on a points or approval estimate.

## Open questions and dependencies

The overview gives a 12-to-18-month window without specifying the cutoff. Use a documented window within that range as a planning choice. The brief does not say how to judge niche inputs with fewer than ten proven comparables.
