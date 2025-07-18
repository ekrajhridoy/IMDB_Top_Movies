import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
s = Service('C:/Users/EKRAJ/Downloads/Chrome Driver/chromedriver-win64/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service = s)


driver.get('https://www.imdb.com/search/title/?title_type=feature&release_date=2015-01-01,2025-07-01')
time.sleep(2)


#height = driver.execute_script("return document.body.scrollHeight;")
#print(height)


html = driver.page_source

with open('movies.html','w',encoding='utf-8') as f:
    f.write(html)


















