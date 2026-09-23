from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

from selenium.webdriver.chrome.options import Options
# 상단 제어창 문구 삭제 
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(options=options)
browser.get("https://www.gmarket.co.kr/n/search?spm=gmktpc.home.searchtop.dsearchbox.1fbf486ayv2nzP&keyword=tv&p=1")



# pip install python-dotenv 설치하기 
# python -m pip install python-dotenv

browser = webdriver.Chrome()
url = "https://www.naver.com/"
# browser.get(url)
# browser.find_element(By.CLASS_NAME, "MyView-module__link_login___VlF7z").click() # 클릭하면 지정한 페이지로 이동 
# time.sleep(3)
# elem = browser.find_element(By.ID, "id")
# elem.send_keys("aaa")
# elem2 = browser.find_element(By.ID, "pw")
# elem2.send_keys("1111")
# input()

# selenium 액션 명령어
# ---------
# elem.click() # 클릭
# elem.send_keys(“시가총액”) # 입력창 글자입력
# elem.send_keys(Keys.ENTER) # 키보드 enter키 입력[오후 1:07]browser.switch_to.window(browser.window_handles[1])

# 검색부분 - 날씨검색 - enter : 온도,날씨를 출력하시오.

# 검색부분 - 날씨 입력 > enter : 온도, 날씨를 출력하시오.
browser.get(url)
# 검색클릭 > 날씨입력 > enter키
elem = browser.find_element(By.ID,'query')
elem.click()
elem.send_keys('날씨')
elem.send_keys(Keys.ENTER)
# 온도 가져오기
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
temp = soup.find('div',{'class':'temperature_text'}).get_text(strip=True)
print(temp)

input()

# .env파일 읽기
# load_dotenv()
# print(os.getenv('naver_id'))
# .gitignore 파일 숨김 처리 이 파일에 파일 명을 작성하면 깃허브에 안 올라감 

# a = '1,123만원'
# print(a[:-1])
# print(a[:-2])
# print(a[:-1])
# print(a[-2:])
# print(a[-1])
# a_int = int(a[:-2].replace(",",""))
# print(a_int)


# a = float("9.92")
# b = float("8.0")
# c = float("9.1")
# print((a+b+c)/3)

# aa = int("1,023".replace(",",""))
# bb = int("2,120".replace(",",""))
# cc = int("3,023".replace(",",""))
# print((aa+bb+cc)/3)


# 2. selenium : 자동화 구현
# 상단 제어창문구 삭제
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://www.naver.com/"

# 검색부분 - 날씨 입력 > enter : 온도, 날씨를 출력하시오.
browser.get(url)
# 검색클릭 > 날씨입력 > enter키
elem = browser.find_element(By.ID,'query')
elem.click()
elem.send_keys('날씨')
elem.send_keys(Keys.ENTER)
# 온도 가져오기
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
temp = soup.find('div',{'class':'temperature_text'}).get_text(strip=True)
print(temp)

input()


# # 브라우저 열기
# browser.get(url)
# browser.find_element(By.CLASS_NAME,'MyView-module__link_login___VlF7z').click()
# time.sleep(3)
# elem = browser.find_element(By.ID,'id')
# elem.send_keys('aaa')
# elem2 = browser.find_element(By.ID,'pw')
# elem2.send_keys('1111')
# input()



# # .env파일 읽기
# load_dotenv()
# print(os.getenv('naver_id'))
