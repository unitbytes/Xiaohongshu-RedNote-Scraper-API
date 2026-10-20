#!/usr/bin/env python3
"""
Xiaohongshu (RedNote / 小红书) Live Stream & Commerce Scraper — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/xiaohongshu-rednote-live-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/xiaohongshu-rednote-live-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/xiaohongshu-rednote-live-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_xiaohongshu_rednote_live_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "mode": "live",
    "liveCategories": ["0"],
    "maxItems": 27,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "HK"
    }
}

run = client.actor("unitbytes/xiaohongshu-rednote-live-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("nickname"), item.get("hotValue"))
