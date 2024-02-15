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


def count_words(subreddit, word_list, counts={}, after=None):
    """
    Queries the Reddit API and returns a list containing the titles \
        of all hot articles for a given subreddit. If no results are \
            found for the given subreddit, the function should return None.
    """
    if after is not None:
        url = f"{base_url}/r/{subreddit}/hot.json?after={after}"
    else:
        url = f"{base_url}/r/{subreddit}/hot.json"
        word_list = [word.lower() for word in word_list]
        counts = {word: 0 for word in word_list}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 200:
        data = req.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            hot_list = post['data']['title']
            split_words = hot_list.split()
            split_words = [word.lower() for word in split_words]
            for word in word_list:
                counts[word] += split_words.count(word)
            # hot_list.append(post['data']['title'])

        # print(len(set(hot_list)))  # Print unique titles count
        # print(hot_list[len(hot_list) - 1])
        after = data.get('after')

        if after:
            # Recursive call with updated 'after'
            return count_words(subreddit, word_list, counts, after)
        else:
            sorted_counts = dict(sorted(counts.items(),
                                        key=lambda item: item[1],
                                        reverse=True))
            for key, value in sorted_counts.items():
                if value > 0:
                    print(f"{key}: {value}")
            return counts
    else:
        return None
