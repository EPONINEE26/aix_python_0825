import requests

res = requests.get("https://www.google.com/?hl=ko/") # html 소스 전체를 가져올 수 있음 
res.raise_for_status() # 에러가 나면 프로그램을 자동 종료시키는 기능 
print(res.text)
print(len(res.text))


# 파일 저장 
with open('google1.html', 'w', encoding="utf-8") as f: # html 소스로 저장된다는 의미 
    f.write(res.text) # html 소스 
    print("파일저장 완료")



# print(res.text) # 모든 데이터 가져오는 기능 
# print("응답코드 : ", res.status_code) # 응답코드를 가져오는 기능 
# print("프로그램을 종료합니다.")
# print("html 소스 : ", res.text) # 글자 정보 가져오는 기능 

# if res.status_code != 200:
    #pass 