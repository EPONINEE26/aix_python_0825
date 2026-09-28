from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# request 방식 
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,'lxml') 
# print("-"*50)

# 2. selenium : 자동화 도구. 스크롤 없이 저장 
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() 
# browser.get(url)

# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file/ya1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 2-1 selenium : 자동화 도구
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() 
# browser.get(url)

# 스크롤 추가 
# execute_script : 스크립트 사용 가능
# 현재 스크롤 높이 가져옴 
# prev_height = browser.execute_script("return document.body.scrollHeight")
# while True: 
#     # 스크롤 높이 출력 
#     print('높이 :', prev_height)
# # 스크롤 내리기 
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(2)
#     # 스크롤이 추가되었는지 확인
#     next_height = browser.execute_script("return document.body.scrollHeight")

#     if prev_height == next_height: 
#         break 
#     prev_height = next_height

# input()

url = "https://www.yeogi.com/domestic-accommodations?keyword=%EC%A0%9C%EC%A3%BC+%EC%A0%9C%EC%A3%BC%EC%8B%9C&autoKeyword=%EC%A0%9C%EC%A3%BC+%EC%A0%9C%EC%A3%BC%EC%8B%9C&checkIn=2026-09-28&checkOut=2026-09-29&personal=2"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() 
browser.get(url)

prev_height = browser.execute_script("return document.body.scrollHeight")
while True: 
    # 스크롤 높이 출력 
    print('높이 :', prev_height)
# 스크롤 내리기 
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 스크롤이 추가되었는지 확인
    next_height = browser.execute_script("return document.body.scrollHeight")

    if prev_height == next_height: 
        break 
    prev_height = next_height

input()

# 파일 저장 
with open('p0928/file/yeo1.html','w',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

print("완료") 

items = soup.find('div',{'data-testid':'virtuoso-item-list'})
# print(items)
y_datas = items.find_all('div',{'data-known-size' : '227'})
print(len(y_datas))

# browser = webdriver.Chrome()
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"

# browser.get(url)
# time.sleep(2)

url = "https://www.yeogi.com/domestic-accommodations?keyword=%EC%A0%9C%EC%A3%BC+%EC%A0%9C%EC%A3%BC%EC%8B%9C&autoKeyword=%EC%A0%9C%EC%A3%BC+%EC%A0%9C%EC%A3%BC%EC%8B%9C&checkIn=2026-09-28&checkOut=2026-09-29&personal=2"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() 
browser.get(url)

prev_height = browser.execute_script("return document.body.scrollHeight")
while True: 
    # 스크롤 높이 출력 
    print('높이 :', prev_height)
    # 스크롤 내리기 
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 스크롤이 추가되었는지 확인
    next_height = browser.execute_script("return document.body.scrollHeight")

    if prev_height == next_height: 
        break 
    prev_height = next_height

# input()

# # 파일 저장
soup = BeautifulSoup(browser.page_source,'lxml')
with open('p0928/file/yeo2.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

print("완료") 

# items = soup.find('div',{'data-testid':'virtuoso-item-list'})
# # print(items)
# y_datas = items.find_all('div',{'data-known-size' : '227'})
# print(len(y_datas))