from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}

# 2. selenium : 자동화 구현
# 상단 제어창문구 삭제
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B2%BD%EC%A3%BC&autoKeyword=%EA%B2%BD%EB%B6%81+%EA%B2%BD%EC%A3%BC%EC%8B%9C&checkIn=2026-09-23&checkOut=2026-09-24&personal=2"
browser.get(url)
time.sleep(2)

# 자바스크립트를 통해 브라우저 높이 가져오기
# pre_height = browser.execute_script('return document.body.scrollHeight')
# print("처음 높이 : ",pre_height)
# while True:
#     # 스크롤 내리기
#     browser.execute_script('window.scroll(0,document.body.scrollHeight)')
#     time.sleep(3) # 내용추가하는데 시간대기

#     # 다시 높이 가져오기
#     next_height = browser.execute_script('return document.body.scrollHeight')
#     print('변경된 높이 : ',next_height)

#     if pre_height==next_height: break
#     else : pre_height = next_height

# print('더 이상 높이 변경이 없음')
# input() # enter 치면 종료 

# 파일 저장해서 저장한 파일을 가지고 정보를 가져오기 
# 이미지, 호텔명, 별점, 리뷰수, 금액 출력하기 

# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('hotel1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# input()

# h_img = list[0].find("img")['src']
# print(h_img)

# img_res = requests.get(h_img,headers=headers)
# img_res.status_code()

# print(img_res)

# os.makedirs("./p0923/hotel", exist_ok=True)
# count = 1
# with open(f"p0923/hotel/h_{count}.jpg", "wb") as f:
#         f.write(img_res.content)

# input()

with open('hotel1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    # f.readline()

s_ul = soup.find('ul', {'class' : "css-y5z6rw"})
s_li = s_ul.find_all("li") 

s_img = s_li[0].find("img" , {"src" : 'https://image.withstatic.com/83/142/160/7d8333172cc64112aa8d489e9dfdbd47.jpg?width=792&height=480&format=webp'})

s_titele = s_li[0].find('h3').get_text()
s_star = s_li[0].find('span', {'class' : 'css-ry30z7'})
s_review  = s_li[0].find('span', {"class" : "css-144z61f"})







