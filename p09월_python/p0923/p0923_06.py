from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

for i in range(2016,2021):
    m_url = f'https://search.daum.net/search?w=tot&q{i}=%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    print(m_url)

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window() 
    url = m_url
    browser.get(url)
    time.sleep(3)

    soup = BeautifulSoup(browser.page_source,'lxml')
    os.makedirs('./p0923/file',exist_ok=True)
    with open(f'p0923/file/movie_{i}.html','w',encoding='utf-8') as f:
            f.write(soup.prettify())
            time.sleep(3)

