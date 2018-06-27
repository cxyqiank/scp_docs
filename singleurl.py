from selenium import webdriver
 
dr = webdriver.PhantomJS()
dr.get('http://baidu.info')
print(dr.title)
print(dr.current_url)
dr.quit()
