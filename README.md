# Co-op Watcher

A Python script that checks Canadian tech companies for Summer 2027 co-op postings, so I don't have to visit each careers page by hand.

It pulls live job postings from the [Lever](https://www.lever.co/) public API, filters them down to co-op and internship roles, and sorts them into two groups:

- **Summer 2027 co-ops**: postings that mention May 2027 or Summer 2027
- **Check by hand**: co-ops with no clear term in the posting

## How it works

1. Loops through a list of company slugs and requests each company's postings from `api.lever.co`
2. Marks a posting as a co-op if its commitment type mentions co-op, intern or student, or its title mentions co-op
3. Checks the title and description for Summer 2027 terms
4. Skips co-ops that clearly name a different term (Fall 2026, Winter 2027)
5. Prints both groups with company, title, location, commitment and a link to the posting

Companies that time out or return an error are skipped, so one failed request doesn't stop the run.

## Setup

Requires Python 3.

```bash
git clone https://github.com/HamzaPM58/coop-watcher.git
cd coop-watcher
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python watcher.py
```

To track different companies, edit the `COMPANIES` list in `watcher.py`. A company's slug is the part after `jobs.lever.co/` in its careers page URL.

## Sample output

```
Found 40 postings at magnetforensics
Found 63 postings at evr
...
2 Summer 2027 co-op postings
evr | May 2027 Geographic Information Systems (GIS) Co-op | Calgary, AB | Coop Student | https://jobs.lever.co/evr/...
evr | May 2027 Mining Engineering Co-op | Sparwood, BC | Coop Student | https://jobs.lever.co/evr/...
9 co-ops with no clear term (check by hand):
acceldata | Software Engineering Co-op | Kitchener | Intern | https://jobs.lever.co/acceldata/...
fullscript | Software Developer (Co-op Opportunities) | Ottawa, ON |  | https://jobs.lever.co/fullscript/...
...
```

## Built with

- Python
- [requests](https://requests.readthedocs.io/)
- Lever Postings API
