from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# 2. selenium : 자동화 구현
# 상단 제어창문구 삭제
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://www.yeogi.com/domestic-accommodations?keyword=%EB%B6%80%EC%82%B0&checkIn=2026-09-25&checkOut=2026-09-26&personal=2"
browser.get(url )
time.sleep(3)

# 현재 브라우저 화면의 HTML을 가져옵니다.
# page_source는 Selenium이 현재 보고 있는 페이지의 HTML입니다.
html = browser.page_source

# 가져온 HTML을 BeautifulSoup으로 읽을 수 있게 변환합니다.
soup = BeautifulSoup(html, "lxml")

# 현재 HTML을 yeogi2.html 파일로 저장합니다.
# 저장한 HTML을 나중에 다시 읽기 위해 사용합니다.
with open("yeogi2.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# HTML 저장 완료 문구를 출력합니다.
print("저장완료")

# 저장된 HTML 파일을 다시 엽니다.
with open("yeogi2.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

# 숙소 목록을 감싸고 있는 ul 태그를 찾습니다.
# find()는 조건에 맞는 태그 하나를 찾는 함수입니다.
s_ul = soup.find("ul", {"class": "css-y5z6rw"})

# 원본처럼 ul 안의 모든 li 태그를 찾습니다.
# 이 안에는 숙소 카드와 카드 내부의 작은 li가 함께 들어갈 수 있습니다.
lis = s_ul.find_all("li")

# 실제 숙소 번호를 저장합니다.
# 내부 분류용 li는 번호를 올리지 않기 위해 별도로 사용합니다.
hotel_idx = 0


# for idx, li in enumerate(lis):
#     print(f"{idx+1}.")
# 이 코드를 사용하면 안 되는 이유는 하위 li까지 포함하는 것. 다만 lis가 이미 숙소 카드만 들어 있는 리스트라면 이 코드는 정상. 반대로 모든 li가 들어 있는 상태에서 사용하면 호텔 번호로 사용할 수 없음
# 핵심 정리: 숙소 카드만 골라낸 뒤에는 사용할 수 있음. 여기서 h3는 숙소명이 들어 있는 태그이므로, h3가 있는 li만 실제 숙소 카드로 판단하는 것임. 

# li를 하나씩 확인합니다.
for idx, li in enumerate(lis):

    # 숙소 카드에는 숙소명이 들어 있는 h3 태그가 있습니다.
    # h3가 없는 li는 '호텔', '모텔', '3성급' 같은 내부 li이므로 건너뜁니다.
    s_title_tag = li.find("h3")
    if not s_title_tag:
        continue

    # 실제 숙소 카드만 번호를 1씩 증가시킵니다.
    # 따라서 내부 li 때문에 300번이나 700번으로 뛰지 않습니다.
    hotel_idx = hotel_idx + 1

    # 20개까지만 출력합니다.
    if hotel_idx > 20:
        break

    # 실제 숙소 번호를 출력합니다.
    print(f"{hotel_idx}.")

    try:
        # 현재 숙소 카드 안에서 img 태그를 찾습니다.
        # li.find()를 사용하므로 다른 숙소의 이미지가 섞이지 않습니다.
        img_tag = li.find("img")

        # 이미지 주소를 저장할 변수입니다.
        s_img = None

        # img 태그가 있는지 먼저 확인합니다.
        if img_tag:

            # 일반 이미지 주소가 src에 있으면 가져옵니다.
            if img_tag.has_attr("src"):
                s_img = img_tag["src"]

            # src가 없으면 data-src를 확인합니다.
            elif img_tag.has_attr("data-src"):
                s_img = img_tag["data-src"]

            # data-lazy-src에 주소가 있으면 가져옵니다.
            elif img_tag.has_attr("data-lazy-src"):
                s_img = img_tag["data-lazy-src"]

            # srcset에 주소가 있으면 첫 번째 주소를 가져옵니다.
            elif img_tag.has_attr("srcset"):
                s_img = img_tag["srcset"]
                s_img = s_img.split(",")[0].strip().split(" ")[0]

        else:
            # img 태그가 없는 경우입니다.
            # img_tag["src"]를 실행하면 오류가 발생하므로
            # 이미지 주소만 None으로 처리합니다.
            # 이미지가 없어도 숙소명·평점·평가수·금액은 계속 출력합니다.
            s_img = None

        # 이미지 주소를 출력합니다.
        print("이미지 URL:", s_img)

        # 현재 숙소 카드의 h3에서 숙소명을 가져옵니다.
        # h3 태그는 위에서 이미 찾은 s_title_tag를 사용합니다.
        # 이렇게 하면 숙소명에 다시 find()를 실행하지 않아도 됩니다.
        s_title = s_title_tag.get_text(strip=True)

        # 숙소명을 출력합니다.
        print("숙소명 : ", s_title)

        # 현재 숙소 카드 안에서 별점 태그를 찾습니다.
        s_star_tag = li.find(
            "span",
            {"class": "css-ry30z7"}
        )

        if s_star_tag:
            # 별점 글자를 가져옵니다.
            s_star = s_star_tag.get_text(strip=True)

            # 글자를 실수형 숫자로 변환합니다.
            s_star = float(s_star)

        else:
            # 별점 태그가 없는 경우입니다.
            # get_text() 오류를 막기 위해 None으로 처리합니다.
            s_star = None

        # 별점을 출력합니다.
        print("평점 : ", s_star)

        # 현재 숙소 카드 안에서 평가수 태그를 찾습니다.
        s_view_tag = li.find(
            "span",
            {"class": "css-144z61f"}
        )

        if s_view_tag:
            # 예: 2,872명 평가
            s_view = s_view_tag.get_text(strip=True)

            # '명 평가'를 제거하고 쉼표를 삭제합니다.
            s_view = s_view[:-4].replace(",", "")

            # 문자열을 정수로 변환합니다.
            s_view = int(s_view)

        else:
            # 평가수 태그가 없는 경우입니다.
            # 오류가 나지 않도록 None으로 처리합니다.
            s_view = None

        # 평가수를 출력합니다.
        print("평가수 : ", s_view)

        # 현재 숙소 카드 안에서 금액 태그를 찾습니다.
        s_price_tag = li.find(
            "span",
            {"class": "css-1llao6q"}
        )

        if s_price_tag:
            # 금액 글자를 가져옵니다.
            s_price = s_price_tag.get_text(strip=True)

            # 쉼표를 제거하고 정수로 변환합니다.
            s_price = int(s_price.replace(",", ""))

        else:
            # 가격 대신 '다른 날짜 확인'만 표시되는 경우입니다.
            # 가격 태그가 없어도 프로그램이 중단되지 않도록 None으로 처리합니다.
            s_price = None

        # 금액을 출력합니다.
        print("금액 : ", s_price)

        # 한 숙소의 출력이 끝났음을 표시합니다.
        print("-" * 60)

    except Exception as e:
        # 한 숙소에서 오류가 발생해도 다음 숙소를 계속 처리합니다.
        print("현재 숙소 처리 중 오류:", e)
        print("-" * 60)
