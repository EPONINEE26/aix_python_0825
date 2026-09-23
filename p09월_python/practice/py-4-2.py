from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os


browser = webdriver.Chrome()
url = "https://finance.daum.net/domestic"
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
with open('sss1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

with open("sss1.html", "r", encoding="utf-8") as f:
    f.readline()
    soup = BeautifulSoup(f, 'lxml')

s_body = soup.find("body", {"class": "finance"})
divs = s_body.find_all("div")
trs = divs[0].find_all("td")
print(trs[0].find("a", {"href": "domestic/wics/G101010"}).get_text(strip=True))




# with open('sss1.html','r',encoding='utf-8') as f:
#     f.readline()
#     soup = BeautifulSoup(f,'lxml')

# s_tbody = soup.find("tbody",{'class':'Table_tbody__EJrOg'})
# trs = s_tbody.find_all('tr')
# tds = trs[0].find_all('td')
# print(tds[0].find('span',{'class':'SingleLineText_text__HI_cb'}).get_text(strip=True))