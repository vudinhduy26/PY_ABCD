# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:30:44 2021

@author: duy
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class craigslist_crawler(object):
    def __init__(self,query):
        #self.max_price = max_price
        self.query = query
        self.url = f"https://timkiem.vnexpress.net/?q={query}"
        self.driver = webdriver.Chrome("U:\BT\python\chromedriver.exe")
        self.delay = 5
    
    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements_by_class_name("item-news item-news-common")
        arr = []
        for data in all_data:
            #print(data.text)
            title = data.text.split("\n")
            arr.append(title)
        file = open("demo_txt.txt","w+")
        for i in arr:
            c = str(i)+"\n"
            file.write(c)
            """if title[0] == "":
                title = title[1]
            else:
                title = title[0]
            price = title[0]
            title = title[-1].split(" ")
            print(title)"""
    """def close_driver(self):
        self.driver.close()"""

query = "hot"
max_price = "500"
crawler = craigslist_crawler(query)
crawler.load_page()