# import os 

# with open("c:/aaa/a.txt","w",encoding="utf-8") as f: # 덮어쓰기. 추후에 쓴 정보만 남고 나머진 다 사라짐 
#     while True:
#         outStr = input("내용입력 : ")
#         if outStr == "" : break
#         f.write(outStr+"\n") # 엔터키가 입력되어있지 않으면 옆으로 출력이 됨 
# print("파일내용이 저장되었습니다.") 

# # 로그파일 외에는 db에 저장함 

import os 

with open("c:/aaa/a.txt","a",encoding="utf-8") as f: # 이어쓰기. 새롭게 입력한 정보까지 포함되어짐. 
    while True:
        outStr = input("내용입력 : ")
        if outStr == "" : break
        f.write(outStr+"\n") 
print("파일내용이 저장되었습니다.") 





