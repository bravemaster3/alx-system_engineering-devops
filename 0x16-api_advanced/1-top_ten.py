#!/usr/bin/python3
"""
This module contains a  function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Function definition"""
    base_url = "https://www.reddit.com"
    end_point = "/subreddits/search"

    headers = {'Accept': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 \
               Safari/537.36'}
    req = requests.get('{}/r/{}/.json?\
                       sort=top&limit=10'.format(base_url, subreddit),
                       headers=headers, allow_redirects=False)

    print('{}/r/{}/about/.json?sort=top&limit=10'.format(base_url, subreddit))
    if req.status_code == 200:
        for post in req.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
