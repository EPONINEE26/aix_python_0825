# for i in range(1,11):
#     print(i)

# print("-"*50)
# i=1
# while(i<=11): # 조건문이 참일 때만 조건문이 실행됨 
#     print(i)
#     i+=1

# # for i in range(1,11,2): 식과 같이 만들려면? 
# while(i<11): 

# 모든 for 문은 while문으러 변경 가능
# for : 반복, 구간지정, 1-10까지
# while : 조건식이 있을 때 주로 사용, 무한반복일 때 사용

# i=0
# while True:
#     print(1)
#     i+=1

# alist=list(range(10))
# while 문을 이용해서 alist 있는 값을 출력하시오.
# 0 1 2 3 4 5 6 7 8 9 이런식으로 출력하시오. 

# alist=list(range(10))
# i=0
# while i<10:
#     print(alist[i], end="  ")
#     i+=1 

# for i in range(10):
#     print(i)

# i=0 # 초기값
# while i<10: # 조건식 
#     print(i)
#     i+=1 # 증감식 

# alist=["바나나","딸기","수박"]

# for i in alist:
#     print("{}:{}".format(i.alist[i]))

# i=0
# while i<3:
#     print("{}:{}".format(i, alist[i]))
#     i+=1 

# i=0
# while True:
#     print(i)

# print("프로그램종료") # 프로그램을 강제로 종료하지 않는 한 에러로 처리됨 while 문은 강제 종료가 되지 않는 한 빠져나올 수 없음 

# i=0
# while True:
#     print(i)
#     if i%10==0:
#         input("프로그램을 종료할까요?") # 종료할까요 글자만 보이고 조건문은 계속 실행됨. 
#         break 
#     i+=1 

# i=0
# while True:
#     print(i)
#     if i%10==0:
#         input1=input("프로그램을 종료할까요?") # 종료할까요 글자만 보이고 조건문은 계속 실행됨. 
#         if input1== "x": # x 글자 입력 시 프로그램 종료 
#             break 
#         i+=1 

# 두 수를 입력받아 합을 구하는 무한 반복 프로그램을 구현하시오. 

# i=0
# while True:
#     a=int(input("1. 숫자 : "))
#     if a==0: break
#     b=int(input("2. 숫자 : "))
#     if b==0: break
#     print("{}+{}={}".format(a, b, a+b))
# print("프로그램 종료")


