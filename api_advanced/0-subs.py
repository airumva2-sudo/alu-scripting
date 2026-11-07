#!/usr/bin/python3
"""Query the Reddit API and return subreddit subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ALUStudent/1.0)"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
