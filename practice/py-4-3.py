from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

with open('stock2.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

s_tbody = soup.select_one("#boxTradeVolume table tbody")
trs = s_tbody.find_all('tr')

print("순위\t종목명\t현재가\t전일비\t등락률 -\t거래량 -\t거래대금(백만)\t52주고가")
print("-" * 100)

for tr in trs:
    tds = tr.find_all('td')

    if len(tds) < 8:
        continue

    s_no = tds[0].get_text(strip=True)
    s_name = tds[1].find('a').get_text(strip=True) if tds[1].find('a') else tds[1].get_text(strip=True)
    s_price = tds[2].get_text(strip=True)
    s_net_change = tds[3].get_text(strip=True)
    s_rate = tds[4].get_text(strip=True)
    s_vol = tds[5].get_text(strip=True)
    s_value = tds[6].get_text(strip=True)
    s_high_price = tds[7].get_text(strip=True)

    print(f"{s_no}\t{s_name}\t{s_price}\t{s_net_change}\t{s_rate}\t{s_vol}\t{s_value}\t{s_high_price}")
    print("-" * 100)
