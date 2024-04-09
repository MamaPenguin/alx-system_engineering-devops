#!/usr/bin/python3
"""function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords"""
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Linux:0x16.api.advanced.rsa'}
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    
    if 'data' not in data or 'children' not in data['data']:
        return
    
    posts = data['data']['children']
    
    for post in posts:
        title = post['data']['title'].lower()
        words = title.split()
        
        for word in word_list:
            if word.lower() in words:
                count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1
    
    after = data['data']['after']
    
    if after is not None:
        return count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

