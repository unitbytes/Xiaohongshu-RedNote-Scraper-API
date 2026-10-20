#!/usr/bin/env python3
"""
Xiaohongshu (RedNote / 小红书) Scraper — Posts, Users & Comments — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/xiaohongshu-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/xiaohongshu-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/xiaohongshu-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_xiaohongshu_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "startUrls": [],
    "keywords": ["OOTD"],
    "maxCreators": 10,
    "maxNotesPerCreator": 30,
    "maxItems": 30,
    "maxCommentsPerNote": 0,
    "maxSubCommentsPerComment": 5,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "HK"
    }
}

run = client.actor("unitbytes/xiaohongshu-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("url"), item.get("coverUrl"))
