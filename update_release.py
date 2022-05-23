import requests
import os
import json

repo = "dilex42/rp-test"
GH_TOKEN = os.environ["GH_TOKEN"]
print(GH_TOKEN)

url = f"https://api.github.com/repos/{repo}/releases/latest"
headers = {
    "Accept":"application/vnd.github.v3+json",
    "Authorization": f"token {GH_TOKEN}"
}

resp = requests.get(url,headers=headers)
print(resp)
print(resp.json())
resp_json = resp.json()
release_id = resp_json["id"]
release_body = resp_json["body"]
print(release_id)
print(release_body)

payload = {
    "body": f"{release_body} test"
}

patch_url = f"https://api.github.com/repos/{repo}/releases/{release_id}"
resp_p = requests.patch(patch_url,headers=headers,data=json.dumps(payload))
print(resp_p)
print(resp_p.text)
