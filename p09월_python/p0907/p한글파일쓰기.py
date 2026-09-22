# import os 

# with open("c:/aaa/a.txt","w",encoding="utf-8") as f: # 덮어쓰기. 추후에 쓴 정보만 남고 나머진 다 사라짐 
#     while True:
#         outStr = input("내용입력 : ")
#         if outStr == "" : break
#         f.write(outStr+"\n") # 엔터키가 입력되어있지 않으면 옆으로 출력이 됨 
# print("파일내용이 저장되었습니다.") 

# 로그파일 외에는 db에 저장함 

# import os 

# with open("c:/aaa/a.txt","a",encoding="utf-8") as f: # 이어쓰기. 새롭게 입력한 정보까지 포함되어짐. 
#     while True:
#         outStr = input("내용입력 : ")
#         if outStr == "" : break
#         f.write(outStr+"\n") 
# print("파일내용이 저장되었습니다.")


# 없는 폴더 파일 저장시 에러 파일 있는지 없는지부터 확인해야함. 
# 폴더 확인하는 방법 

# import os 
# if not os.path.exists("C:/aaa2"):
#     os.makedirs("C:/aaa2") # 폴더를 생성해줌 

# with open("c:/aaa2/a.txt","a",encoding="utf-8") as f: 
#     while True:
#         outStr = input("내용입력 : ")
#         if outStr == "" : break
#         f.write(outStr+"\n") 
# print("파일내용이 저장되었습니다.") 

# import os 
# if not os.path.exists("aaa3"): # 폴더명만 입력할 경우 작업중인 폴더 내에 생성이 됨. 
#     os.makedirs("aaa3") # 폴더를 생성해줌 

# with open("c:/aaa2/a.txt","a",encoding="utf-8") as f: 
#     while True:
#         outStr = input("내용입력 : ")
#         if outStr == "" : break
#         f.write(outStr+"\n") 
# print("파일내용이 저장되었습니다.") 


import os 
# fname = input("저장할 파일이름을 입력하세요. (폴더/파일명) >>")
fname = input("저장할 파일이름을 입력하세요. (파일명) >>")
if not os.path.exists("common"): 
    os.makedirs("common") 

with open("common/"+fname,"a",encoding="utf-8") as f: 
    while True:
        outStr = input("내용입력 : ")
        if outStr == "" : break
        f.write(outStr+"\n") 

print("파일내용이 저장되었습니다.") 



