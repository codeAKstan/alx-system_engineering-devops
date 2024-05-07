#!/usr/bin/python3
"""
a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data")
        children = data.get("children")
        if children:
            for post in children:
                print(post.get("data").get("title"))
        else:
            print("No posts found for the subreddit.")
    else:
        print("None")
