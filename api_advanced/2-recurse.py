#!/usr/bin/python3
"""Recursively queries the Reddit API for all hot articles."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of all hot article titles for a subreddit."""

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "ALUStudent:reddit_api:v1.0"
    }

    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts and not hot_list:
            return None

        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        next_after = data.get("after")

        if next_after is None:
            return hot_list

        return recurse(subreddit, hot_list, next_after)

    except (ValueError, AttributeError):
        return None
