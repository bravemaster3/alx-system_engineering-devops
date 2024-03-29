#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""
import requests

base_url = "https://www.reddit.com"

headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles \
        of all hot articles for a given subreddit. If no results are \
            found for the given subreddit, the function should return None.
    """
    if after is not None:
        url = f"{base_url}/r/{subreddit}/hot.json?after={after}"
    else:
        url = f"{base_url}/r/{subreddit}/hot.json"

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 200:
        data = req.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            hot_list.append(post['data']['title'])

        # print(len(set(hot_list)))  # Print unique titles count
        # print(hot_list[len(hot_list) - 1])
        after = data.get('after')

        if after:
            # Recursive call with updated 'after'
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
