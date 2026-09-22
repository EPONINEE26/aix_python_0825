import requests # 웹 접근 가능하게 만드는 라이브러리 (웹 정보 요청하는 라이브러리)
from bs4 import BeautifulSoup # 웹에 있는 파일을 html로 파싱 (접근 수월)
# terminal 에서 하기 입력하고 설치해야함 
# pip install requests
# pip install beautifulsoup4
# pip install lxml

url = "http://www.naver.com"
#url = "https://www.melon.com/chart/index.htm"
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status() # 에러시 종료 
# print(res.status_code) # 상태코드 보여주는 기능 

print(res.text) 

with open("naver1.html", "w", encoding="utf-8") as f:
    f.write(res.text) 
print("파일저장 완료")



