#!/usr/bin/env python3
"""
Xiaohongshu (RedNote / 小红书) Scraper: Trends, Live & KOLs — Official Python SDK Quickstart
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

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "mode": "trending",
    "channels": ["homefeed_recommend"],
    "maxItems": 30,
    "maxCreators": 15,
    "maxNotesPerCreator": 15,
    "maxCommentsPerNote": 0
}

run = client.actor("unitbytes/xiaohongshu-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("likedCount"), item.get("commentCount"), item.get("noteUrl"))
