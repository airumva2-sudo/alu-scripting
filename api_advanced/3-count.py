#!/usr/bin/python3
"""Recursively counts keyword occurrences in Reddit hot post titles."""

import re
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Prints sorted keyword counts from all hot Reddit post titles."""

    if counts is None:
        counts = {}

        for word in word_list:
            word = word.lower()
            counts[word] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "ALUStudent:reddit_api:v1.0"
    }

    params = {
        "limit": 100,
        "after": after
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()

            for word in counts:
                matches = re.findall(
                    r'\b' + re.escape(word) + r'\b',
                    title
                )
                counts[word] += len(matches)

        next_after = data.get("after")

        if next_after is not None:
            return count_words(subreddit, word_list, counts, next_after)

        sorted_counts = sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))

    except (requests.RequestException, ValueError, AttributeError):
        return
