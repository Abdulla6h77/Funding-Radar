# Funding Radar tasks

Criterion and requirement IDs refer to [SPEC.md](SPEC.md). This checklist plans implementation and validation.

## Prerequisites

- [x] Record the official submission requirements, approval criteria, and judging priorities.
- [ ] Confirm product access, endpoint contracts, live test authorization, and sufficient quota. Resolve or document the open decisions in SPEC.md.
- [ ] Keep setup, configuration, dependencies, and verification project-local.

## Implementation and approval checks

- [ ] **A1** Find at least ten comparable companies with recent funding from live sources. Verify each ranked investor's linked investment evidence and exclude unsupported matches.
- [ ] **A2** Reconcile company identity, dates, round type, and investor participation against the source. Test duplicate syndication, name collisions, and conflicting amounts. Separate round size from individual cheque size.
- [ ] **A3** Rank by fit to the supplied activity, stage, and country and explain each position. Show backing links, typical cheque size and stage, lead partner, and a public application, intake, or warm-intro route. Mark unsupported details as unknown.
- [ ] **A4** Accept a short description including activity, stage, and country. Test three different startup descriptions plus an unplanned input in another market.
- [ ] **A5** Provide an API or JSON/CSV export and validate its schema, links, and reproducibility from the displayed ranking.

## Demo and submission

- [ ] Demo at least three different startup descriptions. For each, aim to meet the official ten-comparable minimum using verifiable recent rounds and show the ranking and export.
- [ ] Run the edge-case and security checks in SPEC.md. Capture reproducible live evidence separately from fixture results.
- [ ] Review every submission requirement (S1, S2, S3, S4, S5, S6) and approval criterion before marking the build ready.
- [ ] Prepare setup instructions, the working build link, notes explaining TinyFish's role, the required LinkedIn post tagging TinyFish, and the Discord #showcase share. Obtain publication authorization before posting.
- [ ] Verify the evidence and submit by Tuesday, November 17, 2026 at 11:59 PM Pacific (Wednesday, November 18 at 12:59 PM Pakistan time).
