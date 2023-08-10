#!/usr/bin/python3
"""Queries the Reddit API"""

import requests as req


def number_of_subscribers(subreddit):
    """Queries the Reddit API to get the number of subscribers"""
    url = "https://www.reddit.com/r{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101"
    }
    response = req.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return (response.json().get('data').get('subscribers'))
