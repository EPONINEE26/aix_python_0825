from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2. selenium : 자동화 도구 자동화 도구 chromdriver.exe 이 있어야만 구동이 가능 
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# # 브라우저 열기
# browser.get(url)
# time.sleep(5)
# 파일 저장 
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일 BeautifulSoup변환
with open('stock1.html','r',encoding='utf-8') as f:
        soup = BeautifulSoup(f,'lxml')

#----------------------------
# 상단제목추가
s_headTitle = []
s_tr = soup.thead.tr
ths = s_tr.find_all('th') #8개 정보
for th in ths:
        s_headTitle.append(th.get_text(strip=True))
        # print(th.get_text(strip=True))
print(s_headTitle)

s_tbody = soup.tbody
# trs = s_tbody.find('tr')      # 1개 sk하이닉스 find,find_all
trs = s_tbody.find_all('tr')  # 100개 정보
for tr in trs:
        tds = tr.find_all('td')      # td 8개
        s_idx = tds[0].find('span',{'class':'index'}).get_text(strip=True)
        s_title = tds[0].find('span',{'class':'SingleLineText_text__HI_cb'})
        s_title = s_title.get_text(strip=True)
        s_price = tds[1].find('span',{'class':'SingleLinePrice_price__g_6VV'})
        s_price = s_price.get_text(strip=True)
        s_compare = tds[2].find('span',{'class':'ModulePriceChange_amount__4QYMz'})
        s_compare = s_compare.get_text(strip=True)
        s_upprice = tds[3].find('span',{'class':'SingleLinePrice_price__g_6VV'})
        s_upprice = s_upprice.get_text(strip=True)
        s_lowprice = tds[4].find('span',{'class':'SingleLinePrice_price__g_6VV'})
        s_lowprice = s_lowprice.get_text(strip=True)
        s_costliness = tds[5].find('span',{'class':'SingleLinePrice_price__g_6VV'})
        s_costliness = s_costliness.get_text(strip=True)
        s_trade = tds[6].find('span',{'class':'SingleLinePrice_price__g_6VV'})
        s_trade = s_trade.get_text(strip=True)
        s_cap = tds[7].find('span',{'class':'SingleLineText_text__HI_cb'})
        s_cap = s_cap.get_text(strip=True)
        print(f"{s_idx}\t{s_title}\t{s_price}\t{s_compare}\t{s_upprice}\t{s_lowprice}\t{s_costliness}\t{s_cap}")
        print("-"*100)


# s_tbody = soup.tbody
# # trs = s_tbody.find("tr") # 1개 sk하이닉스 정보 가져옴 
# trs = s_tbody.find_all("tr") # 100개 정보 가져옴 
# for tr in trs:
#         tds = tr.find_all("td") 
#         s_index = tds[0].find("span", {"class" : "index"}).get_text(strip=True)
#         s_title = tds[0].find("span", {"class" : "SingleLineText_text__HI_cb"})
#         s_title = s_title.get_text(strip=True) # 공백을 제거해서 글자만 가져옴 
#         s_price = tds[1].find("span", {"class" : "SingleLinePrice_price__g_6VV"})
#         s_price = s_price.get_text(strip=True)
#         s_total = tds[7].find("span", {"class" : "SingleLineText_text__HI_cb"})
#         s_total = s_total.get_text(strip=True)

# # trs = s_tbody.find_all("tr") # 100개 정보 가져옴 
# # print(s_title)
# # print(s_price)
# # print(s_total)

# print(s_index, s_title, s_price, s_total)
# print(f"{s_index} : {s_title} : {s_price}: {s_total}")
# print("-"*50)




# 1. requests
# 단점 : 자바스크립트로 구동되는 소스 가져올수 없다.
# requests정보가져오기 -> css문법변환 -> find,find_all()
# url = "https://www.melon.com/chart/index.htm"
# # User-Agent : 처음엔 Python-requests 정보로 읽혀짐 그렇기에 Mozilla 로 하는 코드 사용하여 모든 정보 읽혀지게 만듬
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료
# # css문법변환
# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법