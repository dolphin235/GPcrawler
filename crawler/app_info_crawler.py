#!/bin/user/python3

from time import perf_counter
from bs4 import BeautifulSoup
from selenium import webdriver
import time

import crawler.common as cm
import crawler.file_util as fu

WEBDRIVER_PATH = 'webdriver/chromedriver'
DELIMITER = '&&&&&'


class AppInfoCrawler:
    google_play_detail_url = 'https://play.google.com/store/apps/details?id='

    def __init__(self, package_name, raw_dir_path):
        self.package_name = package_name
        try:
            self.soup = self.get_soup()
        except KeyboardInterrupt:
            raise
        except:
            fu.wrtie_text_to_file(raw_dir_path + self.package_name, 'None')
            return
            
        self.category = self.get_category()
        self.description = self.get_description()
        self.permission = self.get_permission()
        self.privacy_policy = self.get_privacy_policy()
        self.save_raw_data(raw_dir_path)


    def get_category(self):
        category = 'not_set'
        tags = self.soup.findAll('span', attrs={'class':'T32cc UAO9ie'})
        for tag in tags:
            if "genre" in str(tag.a):
                category = tag.text
        return category


    def get_description(self):
        description = 'not_set'
        tags = self.soup.findAll('div', attrs={'jsname':'bN97Pc'})
        for tag in tags:
            if "description" in str(tag):
                description = tag.text
                break
        return description


    def get_permission(self):
        permission = []
        driver = self.set_webdriver(WEBDRIVER_PATH)
        driver.get(AppInfoCrawler.google_play_detail_url+self.package_name)
        objs = driver.find_elements_by_class_name('hrTbp')
        for obj in objs:
            if obj.text == "View details":
                obj.click()
                driver.implicitly_wait(1)
                units = driver.find_elements_by_class_name('itQHhe')
                for unit in units:
                    per_category = unit.find_element_by_class_name('SoU6Qc').text
                    per_contents = unit.find_elements_by_class_name('BCMWSd')
                    for content in per_contents:
                        permission.append(per_category+':'+content.text)
        driver.quit()
        return permission


    def get_privacy_policy(self):
        privacy_policy = 'not_set'
        privacy_policy_url = ''
        tags = self.soup.findAll('a', attrs={'class':'hrTbp'})
        for tag in tags:
            if tag.text == "Privacy Policy":
                privacy_policy_url = tag.get('href')
        try:
            print("[DEBUG] privacy policy url :"+privacy_policy_url)
            response = cm.get_url(privacy_policy_url)
            time.sleep(3)
            privacy_policy = response.read()
        except Exception as e:
            print("[ERROR] "+str(e))
            print("[ERROR] get privacy policy fail")
        
        return privacy_policy


    def save_raw_data(self, dir_path):
        text = DELIMITER + 'package_name' + '\n'
        text = text + self.package_name + '\n'
        text = text + DELIMITER + 'category' + '\n'
        text = text + self.category + '\n'
        text = text + DELIMITER + 'description' + '\n'
        text = text + self.description + '\n'
        text = text + DELIMITER + 'permission' + '\n'
        for l in self.permission:
            text = text + l + '\n'
        text = text + DELIMITER + 'privacy_policy' + '\n'
        text = text + str(self.privacy_policy) + '\n'
        text = text + DELIMITER + 'end'
        fu.wrtie_text_to_file(dir_path + self.package_name, text)


    def get_soup(self):
        response = cm.get_url(AppInfoCrawler.google_play_detail_url+self.package_name)
        html = response.read()
        return BeautifulSoup(html, 'html.parser')


    def set_webdriver(self, driver_path):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("disable-gpu")

        driver = webdriver.Chrome(driver_path, options=options)
        driver.implicitly_wait(2)

        return driver

