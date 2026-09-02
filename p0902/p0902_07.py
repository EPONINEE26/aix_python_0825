# 함수 사용 방법 
# def print1():
#     print(1,end=" ")
#     print(2,end=" ")
#     print(3,end=" ")
#     print(4,end=" ")
#     print(5)

# while True:
#     num1=int(input("숫자 입력 : "))
#     print1(num1)

# def print1(num1):
#     for i in range(num1):
#     print("안녕하세요") 


# while True:
#     num1=int(input("숫자 입력 : "))
#     print1(num1)

# def 문과 while 문은 서로 영향을 받지 않음 

# 함수는 호출하는 명령어가 위에 있어야 함. 파이썬은 스크립터 언어이기에 무조건 위쪽에 있어야 함. 

# def print1(num1):
#     for i in range(num1):
#         print("안녕하세요.") 


# while True:
#     num1=int(input("숫자 입력 : "))
#     print1(num1) # 매개 변수 num1에 입력한 숫자만큼 안녕하세요가 출력이 됨 

# 함수의 매개변수 개수가 틀리면 에러가 남 
# def print1(num1):
#     for i in range(num1):
#         print("안녕하세요.") 

# while True:
#     num1=int(input("숫자 입력 : "))
#     str1=input("출력하려는 문구를 입력 : ")
#     print1(num1) 

# def print1(num1,str1):        
#     for i in range(num1): 
#         print(i+1, str1)

# while True:
#     num1=int(input("숫자 입력 : "))
#     str1=input("출력하려는 문구를 입력 : ")
#     print1(num1, str1) 

# def 함수이름 (변수1, 변수2,....):

# 함수 리턴 

# def add(num1,num2):
#     sum=num1+num2
#     return sum # return : 호출하는 곳으로 값 전달 방법 

# while True:
#     num1=int(input("숫자1 입력 : "))
#     num2=int(input("숫자2 입력 : "))
#     result=add(num1,num2)
#     print(total) 

# def add(num1,num2):
#     sum=num1+num2
#     return sum # return : 호출하는 곳으로 값 전달 방법 

# while True:
#     num1=int(input("숫자1 입력 : "))
#     num2=int(input("숫자2 입력 : "))
#     total=add(num1,num2)
#     print("결과값 : ", total) 

# 함수리턴
# def add(num1,num2):
#     sum = num1+num2
#     return sum   # 호출하는 곳으로 값전달

# while True:
#     num1 = int(input("숫자입력 : "))
#     num2 = int(input("숫자입력 : "))
#     total = add(num1,num2)
#     print("결과값 : ",total)


# 함수는 호출하는 명령어 위에 있어야 함.
# 함수의 매개변수 개수가 틀리면 에러
# def print1(num1,str1):
#     for i in range(num1):
#         print(i+1,str1)

# while True:
#     num1 = int(input("숫자입력 : "))
#     str1 = input("출력하려는 문구를 입력 : ")
#     print1(num1,str1)


def cal(num1, num2, str1): # 디버깅을 할 경우 에러가 발생한 곳을 찾을 수 있음 예약어나 명령어가 따로 있으면 빨간 줄이 안 나타남
    result=0 
    if str1=="+":
        result=num1+num2
    elif str1 == "-":
        result = num1 - num2 
    return result 

num1 = int(input("숫자 입력 : "))
num2 = int(input("숫자 입력 : "))

str1=input("+,-,*,/, 중 1개를 입력하세요.>>")

result = cal(num1,num2,str1)
print("결과 값 : " , result) 




