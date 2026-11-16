# Local workflow

Filter cited comparable funding rounds by date and rank investors based on supplied relevance, stage, and country.

Requires Python 3.10 or later. From this project folder:

```powershell
python main.py example.json
```

The example uses synthetic input. Output marked `offline_input` comes from supplied files.

## Provider entry point

Set `TINYFISH_API_KEY` in the process environment. The provider entry point uses TinyFish's documented service endpoints. One existing live dataset was retrieved with ten provider rows. The three-startup demo and independent source verification remain pending.

`python tinyfish.py --start scope.json --rows 10` starts one billable dataset. Use the example's activity, stage, country, since, and as_of fields with real values. Retrieve rows with `python tinyfish.py --dataset-id DATASET_UUID` and pass the returned cursor as `--after` if present. Save the JSON response privately and rank it with `python main.py demo-energy.json --tinyset-page .local/retrieved-rows.json`. Repeat the flag if the dataset has more pages. Multi-investor rows leave unattributed partner and intake details blank.

Connect TinySet for evidence retrieval, independently check deal links and comparability, and verify the required count across three live demos.
