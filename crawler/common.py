#!/bin/user/python3
import requests

def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print(f"[ERROR] Get url fail [{response.status_code}]")
        raise
