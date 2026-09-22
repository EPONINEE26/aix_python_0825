import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text,'lxml') 
print("-"*50)

s_tbody = soup.tbody
ths = s_tbody.find_all("tr",{"class":"lst50"})
for tr in ths [6,7]:

s_a = ths[6].find("th").get_text()
print(soup.find("span",{"class" : "rank"}))
print(soup.find("div",{"class" : "wrap pd_l_12"}))

for _ in [1] if len(ths) > 6 else []:
    s_a = ths[6].find("th").get_text()
    print(soup.find("span",{"class" : "rank"}))
    print(soup.find("div",{"class" : "wrap pd_l_12"}))
    
    print(s_a[0])
    print(s_a[5])