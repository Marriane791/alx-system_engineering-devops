#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """returns subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "my Reddit API client/1.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        dt = res.json()
        subscribers = dt["data"]["subscribers"]
        return subscribers
    else:
        return 0
