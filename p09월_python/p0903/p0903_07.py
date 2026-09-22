# def func1():
#     a=10 # 함수 a => 지역변수 (함수에 포함된 변수 함수 내에 있는 변수 한정된 지역에 있는 변수)
#     print("func1 a : ",a) # a가 포함되어있기에 10을 출력 

# def func2():
#     print("func2 a : ",a) # a가 포함되어지지 않기에 20을 출력 

# a=20 # 함수 밖 a => 전역변수 (함수에 포함되어지지 않은 변수 함수 밖에 있는 변수 프로그램 전체의 변수)
# # 실행 
# func1()
# func2() 

# 함수 안에 모든 변수는 지역변수가 있는지 확인하고 지역변수가 없을 경우 다 뒤진다.
# 함수 내에 지역변수가 없을 경우 전역변수를 찾음 

# def func1():
#     global a
#     a=10 
#     print("func1 a : ", a)

# # 프로그램 실행 
# a=20 
# func1()
# print("전역변수 : ", a)


# def func1():
#     global a
#     a=10 
#     print("func1 a : ", a)

# # 프로그램 실행 
# a=20 
# print("전역변수 : ", a)

# 함수가 끝나면 안에 있는 변수의 모든 정보는 다 삭제됨 

# def func1():
#     global a  
#     a = 10 
#     print("func1 a : ", a)

# func1()
# print("func1 a : ", a)

# def func1(a,b,c):
#     print(a)
#     return a+10

# c=30 
# result=func1(10,2,c)
# print(result)

# def func1(*num): # 가변매개변수 
#     sum=0
#     for n in num:
#         sum += n
#     return sum 

# print(func1(1,2,3)) 
# print(func1(1,2))
# print(func1(10,20,30,40,50)) 

# def func1(*num):
#     sum=0
#     for n in num:
#         sum += n
#     return sum 

# print(func1(1,2,3)) 
# print(func1(1,2))
# print(func1(10,20,30,40,50)) 

# code09-11.py에서 2에서 10개까지 몇 개를 몇개변수를 사용하든자 합계를 구하돌고 para_func()함수를 수정해보자
# 매개변수가 2개인 함수를 호출한 결과 ==> 30
# 매개변수가 2개인 함수를 호출한 결과 ==> 550 ... 이렇게 출력하시오

# def para_func1(a,b,*num):
#     sum=0
#     sum=a+b
#     for n in num:
#             sum += n
#     return sum 

# print(para_func1(1,2,3)) 
# print(para_func1(1,2))
# print(para_func1(10,20,30,40,50)) 

# def dic_func(**para): # 함수호출할 때 딕셔너리 형식의 매개변수를 키=값 형식으로 사용 

# randint==ranrang와 같은 의미 

# import func # 모듈 가져오는 방법 
# func.cal1()

# from func import cal1, cal2,cal3
# cal1()
# cal2()
# cal3()

# import func
# func.cal1()

# from func import * 
# cal1()
# cal2()
# cal3()

# # as를 붙일 경우 닉네임으로 사용 가능 

# import datetime 
# now=datetime.datetime.now()
# print(now)

# a=max(1,2,3,4)
# print(a)

# import math
# import random
# import datetime
# import math

# import sys
# print(sys.builtin_module_names)

# import math
# dir(math)
# print(math.log(10))

# import math
# dir(math)
# print(math.sin(10))

# import math
# dir(math)
# print(math.log(10))

# import math
# dir(math)
# print(math.floor(10.921)) # 버림

# import math
# dir(math)
# print(math.ceil(10.111)) # 올림 

# import math
# dir(math)
# print(round(10.542)) #  반올림 

# import math
# dir(math)
# print(round(10.542,22)) #  반올림 (값, 소수점자리)




