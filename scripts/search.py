#!/usr/bin/env python3
import sys, requests
KEY = "BSArkwgTm8d52_xJDiG0cdQ_YsOFC-C"
query = " ".join(sys.argv[1:])
r = requests.get("https://api.search.brave.com/res/v1/web/search", headers={"Accept":"application/json","X-Subscription-Token":KEY}, params={"q":query,"count":5})
for result in r.json().get("web",{}).get("results",[]):
    print(result["title"])
    print(result["url"])
    print(result.get("description",""))
    print()