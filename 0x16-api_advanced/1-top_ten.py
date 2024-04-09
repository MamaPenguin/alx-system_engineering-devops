#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
	'User-Agent': 'Linux:0x16.api.advanced.rsa'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 404:
        print("None")
        return
    
    data = response.json()
    if 'data' not in data or 'children' not in data['data']:
        print(None)
        return
    
    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 10:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

