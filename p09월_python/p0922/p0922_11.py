from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2.selenium 파일저장
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())




# 파일 BeautifulSoup변환
# with open('stock1.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')

# s_tbody = soup.find("tbody",{'class':'Table_tbody__EJrOg'})
# trs = s_tbody.find_all('tr')
# tds = trs[0].find_all('td')
# print(tds[0].find('span',{'class':'SingleLineText_text__HI_cb'}).get_text(strip=True))


browser = webdriver.Chrome()
url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
with open('stock1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

# 파일 BeautifulSoup변환
with open('stock1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

s_tbody = soup.find("tbody",{'class':'Table_tbody__EJrOg'})
trs = s_tbody.find_all('tr')
tds = trs[0].find_all('td')
print(tds[0].find('span',{'class':'SingleLineText_text__HI_cb'}).get_text(strip=True))






# 1.requests 방식으로 파일저장
# url = "https://www.melon.com/chart/index.htm"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료

# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
# with open('melon1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 동기식 순서대로 실행됨 
# 비동기식 
# 3번과 4번을 동시에 실행됨 

# 만약 예를 들어 
# 1   1초
# 2   1초
# 3   10초 
# 4   1초
# 5   1초

# 비동기식은 3번과 4번을 동시에 실행하면서 4번이 먼저 실행이 완료됨 
