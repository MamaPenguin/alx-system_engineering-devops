#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""
import requests

def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Linux:0x16.api.advanced.rsa'}
    
    params = {
	'limit': 100, 
	'after': None
    }
    
    if hot_list == []:
        hot_list = []
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 404:
        return None
    
    data = response.json()
    
    if 'data' not in data or 'children' not in data['data']:
        return None
    
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    
    after = data['data']['after']
    
    if after is not None:
        params['after'] = after
        return recurse(subreddit, hot_list)
    else:
        return hot_list

