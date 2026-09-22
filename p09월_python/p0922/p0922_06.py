import requests 
from bs4 import BeautifulSoup

url = "https://www.google.com"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') # html 소스를 css 문법으로 변경 
print("-"*50)

print(soup.title.get_text())
print(soup.find("a",{"class" : "w5hRs"}))
print(soup.find("a",{"class" : "gb_6"}))

# print(soup.title.get_text())
# print(soup.find("span",{"class" : "blind"}))
# print(soup.find_all("span",{"class" : "blind"}))

# print(soup.title.get_text())
# print(soup.find("h2",{"id" : "mainServiceTitle"}))
# print(soup.find_all("a",{"class" : "MyView-module_link_more_F2Dl0"}))