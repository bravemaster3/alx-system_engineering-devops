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

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 \
               Safari/537.36'}
    req = requests.get(base_url+end_point + f".json?q={subreddit}&limit=1",
                       headers=headers, allow_redirects=False)
    result = req.json()
    if req.status_code != 200:
        return 0
    n_subs = 0
    if len(result['data']['children']) > 1 and \
        result['data']['children'][0]['data']['display_name'] == subreddit:
        n_subs = result['data']['children'][0]['data']['subscribers']

    return n_subs
