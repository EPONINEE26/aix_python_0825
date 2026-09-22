import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
#url = "https://n.news.naver.com/article/094/0000013820?cds=news_media_pc&type=editn"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status() 
# 파일 전체 저장 res.text 
# 필요한 부분만 저장 - 파싱 후 원하는 부분을 저장시키는 방식으로 처리 

soup = BeautifulSoup(res.text, 'lxml') # html 소스로 변경하는데 css 문법을 사용을 하는데 코드로 사용하겠다는 의미 태그로 정보를 찾을 수 있게 도와주는 기능
print("-"*50)
# print("a 태그 : ", soup.a)
# print("a 태그 : ", soup.a['href']) # a 태그에 있는 href 값 가져옴 
# print("a 태그 : ", soup.a.attrs) # a 태그의 모든 속성 1개 값을 가져옴 
# print("title 제목 :", soup.title) # soup 에서 태그가 타이틀을 찾아서 출력함. 
# print("title 제목 :", soup.title.get_text()) # 제목만 출력함 

# print(soup.prettify()) 코드가 정렬이 되어 저장이 됨 
# print(res.text)
# 태그로 찾는 방법, 속성 1개, 속성 모두 찾는 방법  
# print(soup.title) 태그 가져오기 
# print(soup.title.get_text()) 태그 글자 가져오기 
# print(soup.div.attrs) # 속성 값 모두 가져오기 
# print(soup.tbody)

# id, class 로 찾는 방법 
# print(soup.find("div",{"id" : "header"}))
# print(soup.find("tr",{"class" : "lst50"}))
# print(soup.find("div",{"class" : "wrap t_right"}))
print(soup.find("input",{"class" : "input_check d_checkall"})['title'])


 

