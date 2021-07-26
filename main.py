#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

tmp_url = "https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically&hl=ko&gl=US"

def print_soup(soup):
    print("\n|title|\n", soup.title)
    print("\n|title.name|\n", soup.title.name)
    print("\n|title.string|\n", soup.title.string)
    print("\n|title.parent.name|\n", soup.title.parent.name)
    print("\n|p|\n", soup.p)
    #print("\n|p['class']|\n", soup.p['class'])
    print("\n|a|\n", soup.a)
    print("\n|find_all('a')|\n", soup.find_all('a'))
    print("\n|find(id='link3')|\n", soup.find(id='link3'))


def main():
    print("[INFO] run main")

    webpage = requests.get(tmp_url)
    soup = BeautifulSoup(webpage.content, "html.parser")

    print_soup(soup)


if __name__=="__main__":
    main()

