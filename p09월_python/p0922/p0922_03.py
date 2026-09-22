import requests

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"} # 내가 웹에 접근하는 코드로 변경해줘라는 의미 
res = requests.get(url, headers=headers)

res.raise_for_status()

with open('melon2.html', 'w', encoding="utf-8") as f: 
        f.write(res.text) # html 소스 
print("파일저장 완료")


