import requests
import os
import json
import re
import sys

def changer(m):
    print(m)
    dat = m.group(0)
    return f'[{dat}](https://github.com/dilex42/rp-test/issues/{dat})'
    
GH_TOKEN = os.environ["GH_TOKEN"]
REPO = sys.argv[1]
print(f"Executing on repo {REPO}")
headers = {
    "Accept":"application/vnd.github.v3+json",
    "Authorization": f"Bearer {GH_TOKEN}"
}


url = f"https://api.github.com/repos/{REPO}/releases/latest"
response = requests.get(url,headers=headers)
print(f"Fetching last release. Status {response.status_code}")
response_json = response.json()
release_id = response_json["id"]
release_body = response_json["body"]
print(f"Found release with id {release_id}")

payload = {
    "body": re.sub("(?<!\[)\\b(?:(?:DAT)|(?:dat))-\d+\\b(?![\w\s]*[\])])",changer,release_body)
}

patch_url = f"https://api.github.com/repos/{REPO}/releases/{release_id}"
patch_response = requests.patch(patch_url,headers=headers,data=json.dumps(payload))
print(f"Updating release. Status {patch_response.status_code}")
