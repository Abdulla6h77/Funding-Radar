# Funding Radar demos

Each input was run through TinySet. The linked JSON preserves the reviewed investment evidence and can be reranked locally.

## United Kingdom · Software for managing grid flexibility and distributed energy resources

10 distinct comparable companies. [Reviewed JSON](demos/energy-reviewed.json)

- **Plug and Play** (6 points) · [Metris Energy](https://eu-startups.com/2026/09/londons-metris-energy-raises-e4-35-million-to-scale-ai-platform-for-managing-renewable-energy-assets), [Gyre Energy](https://environmentenergyleader.com/articles/45069-gyre-energy-raises-13m-to-scale-cold-storage-cooling-tech)
- **Speedinvest** (5 points) · [Tibo Energy](https://tibo.energy/en/news/seed-funding), [Gyre Energy](https://environmentenergyleader.com/articles/45069-gyre-energy-raises-13m-to-scale-cold-storage-cooling-tech)
- **Ada Ventures** (4 points) · [Boldr](https://tech.eu/2025/09/30/boldr-raises-32m-to-turn-homes-into-residential-power-plants)
- **AENU** (4 points) · [Metris Energy](https://eu-startups.com/2026/09/londons-metris-energy-raises-e4-35-million-to-scale-ai-platform-for-managing-renewable-energy-assets)
- **Alpha Future Funds** (4 points) · [Allye Energy](https://techfundingnews.com/allye-energy-ev-battery-storage-funding)

## United States · Software for clinical documentation and administrative workflows sold to healthcare providers

11 distinct comparable companies. [Reviewed JSON](demos/health-reviewed.json)

- **Base10 Partners** (4 points) · [JotPsych](https://jotpsych.com/blog/press-release-jotpsych-secures-5m-seed-round-from-base10-partners)
- **Benhamou Global Ventures** (4 points) · [XCaliber Health](https://prnewswire.com/news-releases/xcaliber-health-raises-6-5m-to-replace-healthcares-point-solutions-with-an-agentic-operating-system-302762914.html)
- **Company Ventures** (4 points) · [Kubera Health](https://prnewswire.com/news-releases/kubera-health-raises-6-5m-to-repair-the-payment-layer-driving-healthcares-1-trillion-admin-burden-302783690.html)
- **ManchesterStory** (4 points) · [XCaliber Health](https://prnewswire.com/news-releases/xcaliber-health-raises-6-5m-to-replace-healthcares-point-solutions-with-an-agentic-operating-system-302762914.html)
- **Nina Capital** (4 points) · [io Health](https://iohealth.ai/io-health-seed-funding)

## India · Software for freight, logistics and supply-chain operations

10 distinct comparable companies. [Reviewed JSON](demos/logistics-reviewed.json)

- **Enrission India Capital** (4 points) · [Raaho](https://vccircle.com/vectorialonto-raaho-pocket-early-stage-funding), [Stackbox](https://yourstory.com/2025/11/startup-news-and-updates-daily-roundup-november-5-2025-paytm-groq)
- **Flipkart Ventures** (4 points) · [Xportel](https://yourstory.com/2025/06/startup-news-and-updates-daily-roundup-june-17-2025)
- **Humba Ventures** (4 points) · [Airbound](https://entrackr.com/snippets/airbound-raises-865-mn-in-seed-funding-round-10561322)
- **Incubate Fund Asia** (4 points) · [Stride Green](https://entrackr.com/snippets/stride-green-raises-35-mn-in-seed-round-9336653)
- **Lachy Groom** (4 points) · [Airbound](https://entrackr.com/snippets/airbound-raises-865-mn-in-seed-funding-round-10561322)

One point per comparable, plus two for a matching funding stage and one for a matching country. Unknown cheque sizes, deal leads and intake routes are blank in the JSON. Funding figures quoted by investor profile pages describe their published terms.

Run `python main.py demos/energy-reviewed.json` to reproduce a ranking. Replace the filename with `health-reviewed.json` or `logistics-reviewed.json` for the other inputs.
