# 팔일 입출력 
# open 
# 읽기용 : 변수명 = opne("파일명", "r") # 읽기 
# 쓰기용 : 변수명 = opne("파일명", "w") # 덮어쓰기 
# 쓰기용 : 변수명 = opne("파일명", "a") # 기존에 파일이 있으면 이어서 쓴다 
# 쓰기용 : 변수명 = opne("파일명", "b") # 이진 모드. 이진 파일을 처리 
# open을 썼으면 무조건 close ()를 써야함 file.close()

# file1 = open("C://aaa//test1.txt", "r", encoding="utf-8") # 영문은 utf-8 안 적어도 됨. utf-8은 한글로 읽어오겠다는 의미 
# f1 = file1.readline()
# print(f1, end="")
# f2 = file1.readline()
# print(f2, end="")
# f3 = file1.readline()
# print(f3, end="")
# file1.close()

# 파일 읽어오기 
# f = open("C://aaa//test1.txt", "r", encoding="utf-8") # 영문은 utf-8 안 적어도 됨. utf-8은 한글로 읽어오겠다는 의미 
# # ("C:/aa/test1.txt", "r", encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line:  # if line == ""
#         break 
#     print(line,end="")
# f.close()










