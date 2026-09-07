# readFile = open("C:/aaa/abc.txt", "r") # 파일 읽어오기 

# while True:
#     str = readFile.readline() 
#     if str == "" : break
#     str = str.strip()
#     print(str, end="\t") 

# # print("프로그램 종료")
# readFile.close()


# with open("C:/aaa/abc.txt", "r") as f: 

#     while True:
#         str = f.readline() 
#         if str == "" : break
#         print(str, end="\t") 

# with open("C:/aaa/abc.txt", "r", encoding="utf-8") as f: # 한글 파일 읽어오기 

#     while True:
#         str = f.readline() 
#         str = str.strip()
#         if str == "" : break
#         print(str, end="\t") 
#         print(str) 

# stuList = []
# with open("C:/aaa/stu.txt", "r", encoding="utf-8") as f: # 한글 파일 읽어오기 

#     while True:
#         str = f.readline() 
#         if str == "" : break
#         stu = str.split(",") # ,를 기준으로 리스트 생성 (분리하여 리스트 생성) 
        
#         for i,s in enumerate(stu): # 1,홍길동,100,100,100,300,100.0
#             if 0<=i<=1: continue
#             elif 2<=i<=5:
#                 stu[i] = int(s.strip())  # s[i] = 문자열 1글자
#             elif i==6:
#                 stu[i] = float(s.strip()) # /n
        
#         stuList.append(stu)
#         print("파일읽어오기 완료!")
#         print(stuList)


# with open("c:/aaa/abc-1.txt","r",encoding="utf-8") as f:
#     while True:
#         str = f.readline()
#         if str == "": break
#         str = str.strip() 
#         if str.strip().isdigit(): # 빈 공백을 꼭 제거해야함 
#             str = int(str)
#         print(type(str), end="")
        
# 출력은 모두 다 하고 숫자의 합을 구하시오. 

# sum = 0
# with open("c:/aaa/abc-1.txt","r",encoding="utf-8") as f:
#     while True:
#         str = f.readline()
#         if str == "": break
#         if str.strip().isdigit():
#             str = int(str)
#             sum += str
#         print(str,end="")

# print("합계 : ",sum)

# abc 출력하시오. 

with open("c:/aaa/abc.txt","r",encoding="utf-8") as f:
    while True:
        str = f.readline()
        if str == "" : break
        str = str.strip()
        print(str, end="\t")





