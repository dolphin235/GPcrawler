#!/usr/bin/python3
import crawler.common as cm
from crawler.applist.applist import AppListCollector

from bs4 import BeautifulSoup
import time

"""
The list of apps provided on this website are those that have been downloaded at least 50K times.
"""

g_androidrank_url = "https://www.androidrank.org"
g_popular_apps = "android-most-popular-google-play-apps"
g_category_url = "android-most-popular-google-play-apps?category="

g_category_list =  ["ART_AND_DESIGN", "AUTO_AND_VEHICLES", "BEAUTY", "BOOKS_AND_REFERENCE", "BUSINESS", "COMICS", "COMMUNICATION", "DATING", "EDUCATION", "ENTERTAINMENT", "EVENTS", "FINANCE", "FOOD_AND_DRINK", "HEALTH_AND_FITNESS", "HOUSE_AND_HOME", "LIBRARIES_AND_DEMO", "LIFESTYLE", "MAPS_AND_NAVIGATION", "MEDICAL", "MUSIC_AND_AUDIO", "NEWS_AND_MAGAZINES", "PARENTING", "PERSONALIZATION", "PHOTOGRAPHY", "PRODUCTIVITY", "SHOPPING", "SOCIAL", "SPORTS", "TOOLS", "TRANSPORTATION", "TRAVEL_AND_LOCAL", "VIDEO_PLAYERS", "WEATHER", "GAME_ACTION", "GAME_ADVENTURE", "GAME_ARCADE", "GAME_BOARD", "GAME_CARD", "GAME_CASINO", "GAME_CASUAL", "GAME_EDUCATIONAL", "GAME_FAMILY", "GAME_MUSIC", "GAME_PUZZLE", "GAME_RACING", "GAME_ROLE_PLAYING", "GAME_SIMULATION", "GAME_SPORTS", "GAME_STRATEGY", "GAME_TRIVIA", "GAME_WORD" ]



class AndroidrankListCollector(AppListCollector):

    def __init__():
        super().__init__()


    @classmethod
    def get_all_list(cls):
        package_names = []
        for category in g_category_list:
            print(category)
            package_names.extend(cls.get_list(g_androidrank_url+'/'+g_category_url+category))
            time.sleep(3)
        return package_names


    @classmethod
    def get_popular_list(cls):
        return cls.get_list(g_androidrank_url+'/'+g_popular_apps)


    @classmethod
    def get_list(cls, first_url):
        package_names = []
        next_url = first_url
        while(next_url != None):
            response = cm.get_url(next_url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            package_names.extend(cls.find_package_names(soup))

            next_val = cls.find_next_url(soup)
            if next_val == None:
                break
            next_url = g_androidrank_url+next_val

        return package_names


    def find_next_url(soup):
        a_tags = soup.select('a')
        for a_tag in a_tags:
            if a_tag.text == 'Next >':
                return a_tag['href']


    def find_package_names(soup):
        res_list = []
        a_tags = soup.find_all('a')
        for a_tag in a_tags:
            if "/application/" in a_tag['href']:
                res_list.append(a_tag['href'].split('/')[-1])
        return res_list


