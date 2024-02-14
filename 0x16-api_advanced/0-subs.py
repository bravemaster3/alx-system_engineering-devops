#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""


def number_of_subscribers(subreddit):
    """Function definition"""
    import requests
    base_url = "https://www.reddit.com"
    end_point = "/subreddits/search"

    headers = {'Accept': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 \
               Safari/537.36'}
    req = requests.get('{}/r/{}/about/.json'.format(base_url, subreddit),
                       headers=headers, allow_redirects=False)

    if req.status_code == 200 and 'subscribers' in req.json()['data']:
        return req.json()['data']['subscribers']
    else:
        return 0
