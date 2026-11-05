# Greenhouse: every open job as JSON in one URL

Code from the SnakeByte Short "Greenhouse scraping trick: every open job as JSON in one URL".

Many companies post their jobs through Greenhouse, and Greenhouse job boards have a public JSON API.
No API key, no login, no pagination: one request returns the whole board.

```
https://boards-api.greenhouse.io/v1/boards/<company>/jobs
```

Add `?content=true` to get the full description, departments and offices of each job.

## Run it

```bash
pip install requests
python jobs.py stripe
python jobs.py discord
```

`jobs.py` prints how many jobs are open and the first ten: title, location and team.

## Find the company name

- The job board is on `job-boards.greenhouse.io/<company>` or `boards.greenhouse.io/<company>`: the name is the word after the domain.
- The careers page is on the company's own site: job links with `gh_jid=` mean Greenhouse. Try the company name in lowercase, like `stripe`.
- The request fails: the name is wrong or the company has no public Greenhouse board.

## Be polite

Public job data only, through Greenhouse's documented [Job Board API](https://developers.greenhouse.io/job-board.html).
One request returns everything, so one request per run is enough.