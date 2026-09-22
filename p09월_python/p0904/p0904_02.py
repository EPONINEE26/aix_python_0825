# 예외처리 (exception handling)
# 조건문을 사용하는 방법
# try 구문을 사용하는 방법 

# print(1)
# pront(1) # 구문오류  

# 런타임에러 
# arr = [1,2,3,4,5]
# while True:
#     choice = int(input("0~4까지 숫자 입력 : "))
#     if choice>4:
#         print("잘못입력하셨습니다. 다시 입력하세요.")
#         continue
#     print("선택값 : ", arr[choice]) 


# try : 예외가 발생할 가능성이 있는 코드 
# except : 예외가 발생할 때 실행하는 코드  

# arr = [1,2,3,4,5]
# while True:
#     choice = int(input("0~4까지 숫자 입력 : "))
#     print("선택값 : ", arr[choice]) 

# arr = [1,2,3,4,5]
# while True:
#     choice = input("0~4까지 숫자 입력 : ")
#     if choice.isdigit():
#         choice = int(choice) # 문자를 넣어도 에러는 안 남 
#     else:
#         print("숫자만 입력이 가능합니다. 다시 입력하세요.")
#         continue
#     print("선택값 : ", arr[choice]) 
    # try:
    #     choice = int(input("0~4까지 숫자 입력 : "))
    #     print("선택값 : ", arr[choice]) 
    # except Exception as e: # 무슨 에러가 났는지에 대한 이유를 알려줌 
    #     print("에러가 났습니다.")
    #     print(e)

# print(1)
# try:
#     print(2)
#     print(3)
#     print(10/0) # 에러가 남. 에러가 나면 그 이후의 except 항목을 찾아 그 이후부터 출력함. 즉. 4가 출력이 안남. 
#                 # 그러나 print(10/0) 이 주석처리가 된 경우에는 1,2,3,4,7 만 출력 즉 try 구문이 에러가 안 났으면 except 구문은 출력이 안 됨 
#     print(4)
# except Exception as E:
#     print(Exception)
#     print(5)
#     print(6)

# print(7)
# as 로 쓸 경우 별명이나 닉네임 또는 이름을 줄여서 사용해도 됨. 

# try:
# except : 
#     pass # 그냥 구동만 해줘라는 의미 
# finally 는 무조건 실행할 코드 의미 많이 사용 

# raise : 강제로 에러를 발생하는 코드 프로그램 구현 안 된 부분을 확인시키는 코드 

# print(1)
# print(2)
# print(3)
# raise NotImplementedError
# print(4)
# print(5)
# print(6)
# print(7)

choice = int(input("원하는 번호입력 : "))
if choice == 1:
    print("학생성적입력부분")
elif choice == 2:
    print("출력")
elif choice == 3:
    print("검색")
elif choice == 4:
    print("수정")
elif choice == 5:
    print("삭제")





