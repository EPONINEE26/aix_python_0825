from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# url = "https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page=1&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() 
# browser.get(url)

# prev_height = browser.execute_script("return document.body.scrollHeight")
# while True: 
#     # 스크롤 높이 출력 
#     print('높이 :', prev_height)
#     # 스크롤 내리기 
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(2)
#     # 스크롤이 추가되었는지 확인
#     next_height = browser.execute_script("return document.body.scrollHeight")

#     if prev_height == next_height: 
#         break 
#     prev_height = next_height

# input()

# 파일 저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file/danawa1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# print("완료") 

for i in range(6): 
    url = "https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page=%7Bpage%7D&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,'lxml')
    print(soup)

    ul = soup.find('ul',{'class' : 'product_list'})   
    lis = ul.find_all('li', {'class' : 'prod_item'})
    print(i, ":", len(lis))







