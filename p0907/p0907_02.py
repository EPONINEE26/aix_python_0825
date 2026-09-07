#hap() 함수 
# 1. 두수를 입력받아 두수의 합을 구하시오.

# def hap():
#     num1 = int(input("숫자입력 1: "))
#     num2 = int(input("숫자입력 1: "))
#     sum = num1+num2
#     print(sum)

# hap()
# print("프로그램종료")  

# def hap():
#     num1 = int(input("숫자입력 1: "))
#     num2 = int(input("숫자입력 1: "))
#     sum = num1+num2
#     print(sum)
#     return sum

# sum=hap()
# print(sum)
# print("프로그램종료")

# def hap(num1, num2):
#     sum = num1+num2
#     # print(sum)
#     return sum

# num1 = int(input("숫자입력 1: "))
# num2 = int(input("숫자입력 1: "))
# sum = num1+num2
# sum=hap(num1, num2)
# print(sum)
# print("프로그램종료")


# hap() 함수
# def hap(): # 함수로 인해 모든 걸 다 알아서 할 때 
#     num1 = int(input("숫자입력1 : "))
#     num2 = int(input("숫자입력2 : "))
#     for i in range(10):
#         sum = num1+num2
#     print(sum)

# def hap2(num1,num2): # 실행 때 입력 받아 함수로 처리한 다음 함수에서 출력할 때 
#     for i in range(10):
#         sum = num1+num2
#     print(sum)


# def hap3(num1,num2): # 함수에서 입력 받고 수식 처리 한 다음 출력은 실행에서 출력할 때 
#     num1 = int(input("숫자입력5 : "))
#     num2 = int(input("숫자입력6 : "))
#     for i in range(10):
#         sum = num1+num2
#     return sum

# def hap3(num1,num2): # 실행에서 입력 받아 변수로 함수로 돌려간 다음 수식 처리 후 실행에서 출력할 때 
#     for i in range(10):
#         sum = num1+num2
#     return sum


# # 1. 매개변수X, return X - hap()
# hap()

# # 2. 매개변수 O, return X - hap2()
# num1 = int(input("숫자입력3 : "))
# num2 = int(input("숫자입력4 : "))
# sum=hap2(num1,num2)


# # 3. 매개변수 O, return O - hap3()
# sum=hap3(num1,num2)
# print(sum)

# # 3. 매개변수 O, return O - hap3()
# num1 = int(input("숫자입력5 : "))
# num2 = int(input("숫자입력6 : "))
# sum=hap2(num1,num2)
# print(sum)


import func

# 1. 매개변수X, return X - hap()
func.hap()
print("hap()완료")

# 2. 매개변수 O, return X - hap2()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
func.hap2(num1,num2)
print("hap2()완료")

# 3. 매개변수 O, return O - hap3()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
sum = func.hap3(num1,num2)
print(sum)
print("hap3()완료")

import func as fn

# 1. 매개변수X, return X - hap()
fn.hap()
print("hap()완료")

# 2. 매개변수 O, return X - hap2()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
fn.hap2(num1,num2)
print("hap2()완료")

# 3. 매개변수 O, return O - hap3()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
sum = fn.hap3(num1,num2)
print(sum)
print("hap3()완료") 

from func import hap, hap2, hap3

# 1. 매개변수X, return X - hap()
hap()
print("hap()완료")

# 2. 매개변수 O, return X - hap2()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
hap2(num1,num2)
print("hap2()완료")

# 3. 매개변수 O, return O - hap3()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : "))
sum = hap3(num1,num2)
print(sum)
print("hap3()완료")



