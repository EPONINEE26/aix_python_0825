# score = int(input("점수입력:"))

# if score >= 90:
#     print("A")
# else:
#     if score >= 80:
#         print("B")
#     else:
#         if score >= 70: 
#             print("B")
#         else: 
#             if score >= 60:
#                 print("D")
#             else: 
#                 print("F")


# score = int(input("점수 입력 : "))

# if score >= 90 :
#     print("A")
# elif score >= 80 :
#     print("B")
# elif score >= 70 :
#     print("C")
# elif score >= 60 :
#     print("D")
# else :
#     print("F")

# print("[학생성적프로그램]")
# s=[0,0,0,0,0,0,0]
# s[0]=input("번호입력:")
# s[1]=input("이름입력:")
# s[2]=int(input("국어점수입력:"))
# s[3]=int(input("영어점수 입력:"))
# s[4]=int(input("수학점수 입력:"))
# s[5]=s[2]+s[3]+s[4]
# s[6]=s[5]/3

# print("-"*60)
# print("번호\t이름\t국어\t영어\t수핫\t합걔\t평균")
# print("-"*60)
# print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}") 
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))
# print("-"*60)


# pi = 3.14149265
# r = int(input("반지름을 입력하세요:")) 

# print("원주율 = ", pi)
# print("반지름 = ", r)
# print("원의 둘레 =", 2*pi*r)
# print("원의 넓이 =", pi*r*r) 

# 원의 반지름을 입력받아 원의 둘레와 넓이를 구하시오
# str_input=input("원의 반지름을 입력하세요:")
# num_input=float((str_input))
# print()
# print("반지름:", num_input)
# print("둘레:", 2*3.14*num_input)
# print("넓이:", 3.14*num_input**2) 

# # 반지름을 입력받아 원의 넓이와 둘레를 구하시오. 
# a=float(input("반지름을 입력하세요."))
# pi=3.14
# print("넓이 :", pi*a*a)
# print("넓이:", pi*a**2) 
# print("원의둘레:", 2*pi*a)

# str1="안녕하세요." 
# print(str1[:])
# print(str1[::-1]) 
# print(str1[:-1]) 
# print(str1[::2]) 
# print(len(str1))

# paper = """네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
# 이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.
# """
# print(paper)
# print(paper.find("홍수")) 
# print(paper.rfind("빙하"))
# print(len(paper))


# # inch 코드를 입력받아 cm 으로 구하시오.

# a=input("숫자입력:")
# a=int(a)
# b=a*2.54
 
# print("인치를 입력하세요:", a)
# print("inch:",a)
# print("cm", b)

# a=20
# print("{}".format(a))
# print("{:10d}".format(a))
# print("{:010d}".format(a)) 
# print("{:3d}".format(123456789))
# print("{:3,d}".format(123456789))
# print("{:.2f}".format(123456789))
# print("{:+010d}".format(a))
# print("{:+010d}",format(-10))

# 20
#         20
# 0000000020
# 0000000020
# 123456789
# 123,456,789
# 123456789.00
# +000000020
# {:+010d} -10


# import datetime
# import random
# now=datetime.datetime.now()

# print(now)
# print("{}년\t{:0d}월\t{}일\t{}시\t{}분\t{}초".format(2026, 8, 29, 10, 6, 50))
# print("{}년\t{:02d}월\t{}일\t{}시\t{}분\t{}초".format(2026, 8, 29, 10, 6, 50))

# 3,4,5 봄, 6,7,8 여름, 9,10,11 가을, 12,1,2 겨울 

# import datetime
# import random

# r_num=random.randint(1,12)
# r_num=int(input("월을 입력허세요.:"))

# if 3 <= r_num <= 5:
#    print("봄입니다.")
# elif 6 <= r_num <= 8:
#    print("여름입니다.")
# elif 9 <= r_num <=11:
#    print("가을입니다.")
# else:
#    print("겨울입니다.:")

# # 스왑 함수 
# a=input("문자열 입력>")
# b=input("문자열 입력>")

# print(a,b)

# c=a
# a=b
# b=c

# print(a,b) 


import random

# # randint-랜덤1개, sample-랜덤여러개(중복불가),
# # shuffle-전체섞음, choices-랜덤여러개(중복가능)

# lotto=random.sample(range(1,46),5)
# input1=input("숫자를 입력하세요")
# input2=input("숫자를 입력하세요")
# input3=input("숫자를 입력하세요")
# input4=input("숫자를 입력하세요")
# input5=input("숫자를 입력하세요")

# if input in lotto:
#    print("당첨!!")
# elif input2 in lotto:
#    print("당첨!!")
# elif input3 in lotto:
#    print("담청!!")
# elif input4 in lotto:
#    print("당첨!!")
# elif input5 in lotto:
#    print("당첨!!")
# else:
#    print("꽝!!")

# lotto=random.sample(range(1,46),5)
# iarr=[]
# iarr.append=input("숫자를 입력하세요.")
# iarr.append=input("숫자를 입력하세요.")
# iarr.append=input("숫자를 입력하세요.")
# iarr.append=input("숫자를 입력하세요.")
# iarr.append=input("숫자를 입력하세요.")

# if iarr[0] in lotto: 
#     print("당첨!! ") else print("꽝")
# elif iarr[1] in lotto:
#      print("당첨!! ") else:print("꽝")
# elif iarr[2] in lotto:
#      print("당첨!! ") else:print("꽝")
# elif  iarr[3] in lotto:
#      print("당첨!! ") else:print("꽝")
# elif  iarr[4] in lotto:
#      print("당첨!! ") else:print("꽝")
  
