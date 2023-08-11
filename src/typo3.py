import json
from common import endoflife

URL = "https://get.typo3.org/api/v1/release/"

def fetch_versions():
    releases = {}

    response = endoflife.fetch_url(URL)
    data = json.loads(response)
    for v in data:
        if v['type'] != 'development':
            date = v["date"][0:10]
            releases[v["version"]] = date
            print(f"{v['version']}: {date}")

    return releases

print("::group::typo3")
releases = fetch_versions()

endoflife.write_releases('typo3', dict(sorted(
    releases.items(), key=lambda x: list(map(int, x[0].split(".")))
)))
print("::endgroup::")
