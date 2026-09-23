from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}

# browser = webdriver.Chrome()
# url = "https://comic.naver.com/bestChallenge?sortType=starscore"
# # 브라우저 열기
# browser.get(url)
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('webtoon1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

with open('webtoon1.html','r',encoding='utf-8') as f:
        soup = BeautifulSoup(f,'lxml')

# 이미지 
s_ul = soup.find("ul", {"class" : "BestChallengeView__challenge_list--sUqhh"}) 
lis = s_ul.find_all("li")
# print(lis)
# print(len(lis))
s_img = lis[0].find("img")['src']
print(s_img)

# 이미지 저장 
# img_res = requests.get(s_img,headers=headers)
# # img_res.status_code()
# print(img_res)
# # 폴더 생성 
# os.makedirs("./p0923/webtoon", exist_ok=True)
# count = 1
# with open(f"p0923/webtoon/w_{count}.jpg", "wb") as f:
#         f.write(img_res.content)


# 먼저 제목이나 작가나 평점 위 바로 위 위치점부터 찾은 다음 그 이후 제목, 작가, 평점으로 처리함
# replace 로 html 소스에 출력된 "만" 자를 제거하는 기능으로 처리함 
s_ul = soup.find('ul',{'class':'BestChallengeView__challenge_list--sUqhh'})
lis = s_ul.find_all('li')
for i in range(3):
    s_contitle = lis[i].find('span',{'class':'ContentTitle__title--e3qXt'})
    s_title = s_contitle.find('span',{'class':'text'}).get_text(strip=True)
    print(s_title)
    s_author = lis[i].find('a',{'class':'ContentAuthor__author--CTAAP'}).get_text(strip=True)
    print(s_author)
    s_constar = lis[i].find('span',{'class':'Rating__star_area--dFzsb'})
    s_star = float(s_constar.find('span',{'class':'text'}).get_text(strip=True))
    print(s_star)
    s_conview = lis[i].find('span',{'class':'Rating__view_area--GQb_S'})
    s_view = int(s_conview.find('span',{'class':'text'}).get_text(strip=True)[:-1].replace(",",""))
    print(s_view)  

a = float("9.92")
b = float("8.0")
c = float("9.1")
print((a+b+c)/3)

aa = int("1,023".replace(",",""))
bb = int("2,120".replace(",",""))
cc = int("3,023".replace(",",""))
print((aa+bb+cc)/3)
