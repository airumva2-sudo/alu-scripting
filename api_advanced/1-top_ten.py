#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params={"limit": 10}
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except (ValueError, AttributeError):
        print(None)
