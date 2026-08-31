# break : 반복문을 완전히 종료 
# continue : 1번만 제외 이후 계속 반복 

# for i in range(100):
#     print(i)
#     if i==50: 
#         break

# print("프로그램 종료")

# for i in range(100):
#     print(i)
#     if i==50: # 100까지 그대로 출력 
#         continue
#     
# print("프로그램 종료")


# for i in range(100):
#     if i%2==0:
#         continue
#     print(i)

# print("프로그램 종료")

# for i in range(100):
#     if i==50: # 50만 뺘고 출력 
#         continue
#     print(i)

# print("프로그램 종료") 

# name=[]
# i=1
# while True:
#     n=input("{}.이름입력:".format(i))
#     name.append(n)
#     print(n)

# name=[]
# i=1
# while True:
#     n=input("{}.이름입력:".format(i))
#     name.append(n)
#     i=i+1
#     print(n)

# no=[]
# name=[]
# i=1
# while True:
#     n=input("{}.이름입력:".format(i))
#     no.append(i)
#     name.append(n)
#     i=i+1
#     print(n)

# no=[]
# name=[]
# i=1
# while True:
#     n=input("{}.이름입력:".format(i))
#     if n=="0":
#         break 
#     no.append(i)
#     name.append(n)
#     i=i+1
#     print(n)

# 1~100까지 랜덤숫자 1개를 생성
# 랜덤숫자를 맞출 때가지 무한반복 프로그램을 구현하시오. 

# import random
# ran1=random.randint(1,5)
# myNum=0
# while True:
#     myNum = int(input("1~5사이 숫자를 입력 : "))
#     print(myNum) 
#     if myNum== ran1: # 랜덤 숫자와 입력숫자가 같은지 비교  
#         print("정답입니다.")
#         break 
# print("프로그램 종료")

# 1~100까지 랜덤숫자 1개를 생성
# 랜덤숫자를 맞출 때가지 무한반복 프로그램을 구현하시오. 

# import random
# ran1=random.randint(1,100)
# myNum=0
# while True:
#     myNum = int(input("1~5사이 숫자를 입력 : "))
#     print(myNum) 
#     if myNum== ran1: # 랜덤 숫자와 입력숫자가 같은지 비교  
#         print("정답입니다.")
#         break 
#     elif myNum > ran1:
#         print("입력한 숫자가 더 큽니다. 작은수 입력:")
#     else :
#         print("입력한 숫자가 더 작습니다. 큰수 입력")

# print("프로그램 종료")

# 내가 입력한 모든 숫자가 출력하고 싶을때 
# import random
# ran1=random.randint(1,100)
# my_list=[] # 입력한 숫자 모두 저장 공간을 리스트로 생성 
# myNum=0 # 내가 입력한 숫자 변수 
# while True:
#     myNum = int(input("1~100사이 숫자를 입력 : "))
#     my_list.append(myNum)
#     print(myNum) 
#     if myNum== ran1: # 랜덤 숫자와 입력숫자가 같은지 비교  
#         print("정답입니다.")
#         break 
#     elif myNum > ran1:
#         print("입력한 숫자가 더 큽니다. 작은수 입력:")
#     else :
#         print("입력한 숫자가 더 작습니다. 큰수 입력")
# print("입력한 모든 숫자:", my_list)
# print("프로그램 종료")


import random
ran1=random.randint(1,100)
my_list=[] # 입력한 숫자 모두 저장 공간을 리스트로 생성 
myNum=0 # 내가 입력한 숫자 변수 
answer=0 
while True:
    myNum = int(input("1~100사이 숫자를 입력 : "))
    my_list.append(myNum)
    print(myNum) 
    if myNum== ran1: # 랜덤 숫자와 입력숫자가 같은지 비교
        answer = myNum
        print("정답입니다.")
        break 
    elif myNum > ran1:
        print("입력한 숫자가 더 큽니다. 작은수 입력:")
    else :
        print("입력한 숫자가 더 작습니다. 큰수 입력")
print("정답 :", answer)
print("정답 :", my_list[-1])
print("입력한 모든 숫자:", my_list)
print("프로그램 종료")

# 1~100까지 랜덤숫자 1개를 생성
# 내가 입력한 모든 숫자가 출력
# 랜덤숫자를 맞출때까지 무한반복 프로그램을 구현하시오.
import random
randNum = random.randint(1,100) # 랜덤숫자생성
my_list = []    # 입력한숫자모두저장
myNum = 0       # 내가입력한숫자변수
answer = 0      # 정답변수
while True:
    myNum = int(input("1-100사이 숫자를 입력 : "))
    my_list.append(myNum)

    # 랜덤숫자와 입력숫자가 같은지 비교
    if myNum == randNum:
        answer = myNum
        print("정답입니다.")
        break
    elif myNum>randNum:
        print("입력한 숫자가 더 큽니다. 작은수 입력!!")
    else:
        print("입력한 숫자가 더 작습니다. 큰수 입력!!")

print("정답 : ",answer)
print("정답 : ",my_list[-1])
print("입력한모든 숫자 : ",my_list)

print("프로그램 종료")
