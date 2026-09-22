import requests 
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

# with open("melon1.html", 'w', encoding="utf-8") as f:
#     f.write(res.text)
# print("파일저장 완료")

soup = BeautifulSoup(res.text, 'lxml') 
print("-"*50)
# print(soup.tbody)

s_tbody = soup.tbody
# print(s_tbody.find_all ("tr", {"class" : "lst50"})) # 순의 1위에 있는 정보 가져옴 
# trs = s_tbody.find_all ("tr", {"class" : "lst50"})
trs = s_tbody.find ("tr", {"class" : "lst50"})
tds = trs.find("td")
input = tds.find("input")['title']
#print(len(tds)) # 1위 정보
# print(tds) # 1위 정보
print("inputs")







