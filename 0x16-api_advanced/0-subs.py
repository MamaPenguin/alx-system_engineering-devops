#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
      	'User-Agent': 'Linux:0x16.api.advanced.rsa'
    }
    response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
    if response.status_code == 404:
        return 0
    else:
        raise


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
