from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os,sys
import ssl

# Python3.x

# 主函数
if __name__ == '__main__':
	url = sys.argv[1]
	ssl._create_default_https_context = ssl._create_unverified_context
	driver = webdriver.Chrome()
	driver.get(url)
	driver.implicitly_wait(0.1)
	title = driver.find_element_by_tag_name("h1").text
	des = driver.find_element_by_tag_name("p").text
	img = driver.find_element_by_tag_name("img").get_attribute("src")
	print(title +  "|" + des + "|" + img)
