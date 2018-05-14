import requests

def request(url):
    return requests.get(url).text
