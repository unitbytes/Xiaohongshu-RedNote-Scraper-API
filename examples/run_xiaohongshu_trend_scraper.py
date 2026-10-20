#!/usr/bin/env python3
"""
Xiaohongshu Trending, Live & Note Scraper (RedNote / 小红书) — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/xiaohongshu-rednote-trend-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/xiaohongshu-trend-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/xiaohongshu-trend-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_xiaohongshu_trend_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "mode": "trending",
    "channels": ["homefeed_recommend"],
    "maxItems": 30,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "HK"
    }
}

run = client.actor("unitbytes/xiaohongshu-rednote-trend-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("hotValue"), item.get("url"))
