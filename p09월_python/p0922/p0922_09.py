import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() 

soup = BeautifulSoup(res.text,'lxml') 
print("-"*50)

# with open("melon1.html", "w", encoding="utf-8") as f:
#     f.write(res.text) 
# print("파일저장 완료")

# with open("melon2.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify()) 
# print("파일저장 완료")

s_tbody = soup.tbody  # 위치 점 찾기 
#trs = s_tbody.find_all("tr",{"class":"lst50"}) # 여러 개 find_all, 1개 find 
#print(s_tbody)
trs = s_tbody.find_all("tr") 
# print(len(trs))
# for i in range(len(trs)): pass 
for tr in trs: # 100번 돌린다는 의미 
    tds = tr.find_all("td") # tds 변수명
    try:
        print("순위 :" , tds[1].find("span", {"class":"rank"}).get_text()+"위")
        print("링크 :" ,tds[3].find("img")['src']) # [], attrs 
        s_as = tds[5].find_all("a") 
        print("제목명 :", s_as[0].get_text()) # 곡 제목 
        print("가수명 :",s_as[1].get_text()) # 가수명 
        print("앨범명 :",tds[6].find("a").get_text()) # 앨범명 
        print("-"*30)
    except Exception as e: # 이슈가 나는 이유 출력 
        print(e)
        

