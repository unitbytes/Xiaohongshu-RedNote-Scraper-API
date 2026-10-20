#!/usr/bin/env python3
"""
Xiaohongshu (RedNote / 小红书) Comments & Live Chat Scraper — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/xiaohongshu-rednote-comments-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/xiaohongshu-comments-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/xiaohongshu-comments-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_xiaohongshu_comments_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "mode": "comments",
    "startUrls": [
        {
            "url": "https://www.xiaohongshu.com/explore/64256e08000000001300575e?xsec_token=ABivcR3TWdHqjbjX2xyNQkAS3_CZsrXHUX9r1tNqo4148=&xsec_source=pc_feed"
        }
    ],
    "maxCommentsPerNote": 20,
    "maxSubCommentsPerComment": 5,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "HK"
    }
}

run = client.actor("unitbytes/xiaohongshu-rednote-comments-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("roomTitle"), item.get("roomUrl"), item.get("noteUrl"))
