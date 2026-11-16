# Live validation

The [reviewed demo exports](DEMO.md) are the release evidence. They contain 10 UK energy, 11 US healthcare, and 10 India logistics comparables. During review, Procode and Procode AI were merged, TechNovaTime was removed because its page did not support the listed investor relationships, and unsupported investor attributions were dropped. Published fund terms were added where verified. Undisclosed or unverified cheque sizes, partners, and intake routes remain blank.

The initial TinySet candidate counts are retained below for comparison.

| Startup input | Candidates in saved ranking |
| --- | ---: |
| UK grid flexibility software | 10 |
| US clinical documentation and administrative software | 13 |
| Indian freight and supply-chain software | 10 |

The counts below describe the candidates before citation review. The earlier UK count of 11 included Metris and Metris Energy as separate names for the same company. The [company announcement](https://metrisenergy.com/about/blog/building-resilient-energy-operations) and [PT1 announcement](https://www.pt1.vc/stories/pt1-co-leads-metris-5m-seed-round) support the alias in the demo input.

Some initial UK source URLs could not be retrieved during review. Primary pages for [Allye Energy](https://www.allye.com/post/allye-energy-secures-2-5-million-seed-funding-to-scale-battery-storage), [Boldr](https://shopboldr.com/blogs/news/boldr-raises-oversubscribed-3-2m-seed-round-to-turn-american-homes-into-residential-power-plants), [Enera](https://getenera.com/press/pre-seed-announcement), [Gyre Energy](https://www.gyreenergy.com/news), and [Tibo Energy](https://tibo.energy/en/news/seed-funding/) provide leads for reconciliation. Check the provider rows against the primary text before publishing rankings.

The private `.local` folder contains the provider results and rendered rankings. Use `main.py --tinyset-page` to rerank the saved evidence without a new build.

TinyFetch returned text for 11 linked pages in the UK case, 13 in the US case, and 10 in the India case. A retrieved page can still contain a redirect, an error message, or a different deal. Keep each relationship provisional until the article text verifies the company, investor, and round.
