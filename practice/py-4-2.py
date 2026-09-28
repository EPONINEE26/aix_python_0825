from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os


# browser = webdriver.Chrome()
# url = "https://finance.daum.net/domestic/volume"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# input()
# print("저장완료"


from bs4 import BeautifulSoup


with open('stock2.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

tbodys = soup.find_all('tbody')

# 실제 거래량 표가 들어 있는 tbody를 선택합니다.
# 숫자 1은 예시입니다.
# 앞서 확인한 결과에서 "td가 8개인 행"이 들어 있는 tbody 번호를 넣어야 합니다.
s_tbody = tbodys[1]

# 실제 종목 줄(tr)을 모두 찾고, 맨 앞 5줄만 가져옵니다.
# [:5]는 1위부터 5위까지만 가져오라는 뜻입니다.
trs = s_tbody.find_all('tr')[:5]

# 1위부터 5위까지 한 줄씩 꺼냅니다.
for tr in trs:    
    tds = tr.find_all('td')

    
    s_no = tds[0].get_text(strip=True)

    # 종목명
    s_name = tds[1].get_text(strip=True)

    # 현재가
    s_price = tds[2].get_text(strip=True)

    # 전일비
    s_net_change = tds[3].get_text(strip=True)

    # 등락률
    s_change_rate = tds[4].get_text(strip=True)

    # 거래량
    s_vol = tds[5].get_text(strip=True)

    # 거래대금
    s_value = tds[6].get_text(strip=True)

    # 52주고가
    s_high_price = tds[7].get_text(strip=True)
    
    print(
        f"{s_no}\t{s_name}\t{s_price}\t{s_net_change}\t"
        f"{s_change_rate}\t{s_vol}\t{s_value}\t{s_high_price}"
    )
    print("-" * 100)