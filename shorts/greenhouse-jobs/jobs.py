import sys
import requests

company = sys.argv[1] if len(sys.argv) > 1 else "stripe"
url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

response = requests.get(url, params={"content": "true"}, timeout=60)
response.raise_for_status()
data = response.json()

print(data["meta"]["total"], "open jobs at", company)
for job in data["jobs"][:10]:
    teams = ", ".join(d["name"] for d in job["departments"])
    print(f'{job["title"]} | {job["location"]["name"]} | {teams}')