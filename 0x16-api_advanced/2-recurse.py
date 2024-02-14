#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""
import requests
base_url = "https://www.reddit.com"
end_point = "/subreddits/search"

headers = {'Accept': 'application/json',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 \
                Safari/537.36'}


def recurse(subreddit, hot_list=[], after=None):
    """Function definition"""

    if after is not None:
        url = '{}/r/{}/hot.json?\
            after={}'.format(base_url, subreddit, after)
    else:
        url = '{}/r/{}/hot.json'.format(base_url, subreddit)

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 200:
        for post in req.json()['data']['children']:
            hot_list.append(post['data']['title'])

        after = req.json()['data']['after']

        if after:
            return hot_list + recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
