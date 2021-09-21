#!/bin/user/python3
import requests
import time
import urllib.request
import socket

MAX_RETRY = 3

def get_url(url):
    return request_url(url)


def request_url(url):
    count = 0
    while True:
        if count >= MAX_RETRY:
            raise
        try:
            headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
            #response = requests.get(url, headers=headers)
            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req, timeout=20)
            if response.status == 200:
                return response
            else:
                print(f"[ERROR] Get url fail response: [{response.status_code}] - [{url}]")
                raise
        except Exception as err:
            print("[ERROR]" + str(err))
            print(f"[ERROR] Get url fail - [{url}]")
            time.sleep(60)
            count = count + 1

