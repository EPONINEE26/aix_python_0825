from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time  
import os
from dotenv import load_dotenv

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://kr.trip.com/hotels/list?city=737&provinceId=0&countryId=42&checkIn=2026-09-27&checkOut=2026-09-28&lat=0&lon=0&districtId=0&barCurr=KRW&searchType=CT&searchWord=%EC%A0%9C%EC%A3%BC%EC%8B%9C&searchValue=___&crn=1&adult=2&children=0&searchBoxArg=t&ctm_ref=ix_sb_dl&travelPurpose=0&domestic=false"
browser.get(url )
time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')
with open('trip1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
input()
print("저장완료")

with open('trip1.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# 트립닷컴의 가변/난독화 클래스 대응 (card, hotel, list가 포함된 모든 카드 상자 수집)
# select (CSS 선택자 방식): 클래스명의 일부 단어만 포함되어도 찾을 수 있음
hotel_divs = soup.select("div[class*='card'], div[class*='Hotel'], div[class*='list']")
# 중복 제거 및 실제로 호텔 정보를 담고 있는 핵심 카드만 필터링
hotel_divs = [div for div in hotel_divs if div.find('img') and (div.find('span') or div.find('div'))]

# 만약 위 방법으로 안 잡힐 경우 HTML 내의 전체 카드 탐색
if not hotel_divs:
    hotel_divs = soup.find_all('div', attrs={"data-id": True})

print(f"총 호텔 수: {len(hotel_divs)}")  # 몇 개 찾았는지 출력

# 찾은 호텔들 하나하나 반복문으로 처리
for idx, hotel in enumerate(hotel_divs, start=1):
    print(f"{idx}번 호텔 정보:")

    # 이미지 태그 찾기 - img 태그 찾음
    img_tag = hotel.find('img')
    img_url = "이미지 없음"
    if img_tag:
        img_url = img_tag.get('src') or img_tag.get('data-src') or "이미지 없음"
    print("이미지 URL:", img_url)

    # 숙소명 찾기
    name_tag = hotel.select_one("span[class*='title'], div[class*='title'], span[class*='name'], div[class*='name'], h3")
    name = name_tag.get_text(strip=True) if name_tag else "숙소명 없음"
    print("숙소명:", name)

    # 평점 찾기
    star_tag = hotel.select_one("span[class*='score'], div[class*='score'], span[class*='Score']")
    star = star_tag.get_text(strip=True) if star_tag else "평점 없음"
    print("평점:", star)

    # 평가수 찾기
    comment_tag = hotel.select_one("span[class*='comment'], span[class*='review'], span[class*='text']")
    comment = comment_tag.get_text(strip=True) if comment_tag else "평가수 없음"
    print("평가수:", comment)

    # 가격 찾기
    price_tag = hotel.select_one("span[class*='price'], div[class*='price'], span[class*='Price']")
    price = price_tag.get_text(strip=True) if price_tag else "금액 없음"
    print("금액:", price)

    print('-' * 50)  

browser.quit()  
