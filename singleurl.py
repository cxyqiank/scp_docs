from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import urllib
import urllib.request
from urllib.request import urlopen
# from urlparse import *
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import ssl
import uuid
import configparser
import os,sys
from multiprocessing import Process
import math

# Python3.x

# 主函数
if __name__ == '__main__':
	url = sys.argv[1]
	ssl._create_default_https_context = ssl._create_unverified_context
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chrome_options = chrome_options)
	driver.get(url)
	driver.implicitly_wait(0.1)
	h1 = driver.find_element_by_tag_name("h1")
	print(h1.text)
