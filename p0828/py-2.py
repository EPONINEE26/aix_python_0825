# print("[학생성적프로그램]")

# s1=[0,0,0,0,0,0,0]
# s1[0]=input("번호를 입력하세요:")
# s1[1]=input("이름을 입력하세요:")
# s1[2]=int(input("국어점수를 입력하세요:"))
# s1[3]=int(input("영어 점수를 입력하세요.:"))
# s1[4]=int(input("수학 점수를 입력하세요.:"))
# s1[5]=s1[2]+s1[3]+s1[4]
# s1[6]=s1[5]/3

# s2=[0,0,0,0,0,0,0]
# s2[0]=input("번호를 입력하세요:")
# s2[1]=input("이름을 입력하세요:")
# s2[2]=int(input("국어 점수를 입력하세요:"))
# s2[3]=int(input("영어 점수를 입력하세요.:"))
# s2[4]=int(input("수학 점수를 입력하세요.:"))
# s2[5]=s2[2]+s2[3]+s2[4]
# s2[6]=s2[5]/3

# print("-" * 60)
# print("번호\t이름\t국어\t영어\t수학\t총점\t평균")
# print("-" * 60)
# print(f"{s1[0]}\t{s1[1]}\t{s1[2]}\t{s1[3]}\t{s1[4]}\t{s1[5]}\t{s1[6]:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}:.2f".format(s1[0],s1[1],s1[2],s1[3],s1[4],s1[5],s1[6]))

# print("-" * 60)
# print("번호\t이름\t국어\t영어\t수학\t총점\t평균")
# print(f"{s2[0]}\t{s2[1]}\t{s2[2]}\t{s2[3]}\t{s2[4]}\t{s2[5]}\t{s2[6]:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}:.2f".format(s2[0],s2[1],s2[2],s2[3],s2[4],s2[5],s2[6]))
# print("-" * 60)

# score = int(input("점수 입력:"))
# if score >= 90:
#     print("A")
# else:
#     if score >= 80:
#         print("B")
#     else:
#         if score >= 70:
#             print("C")
#         else:
#             if score >= 60:
#                 print("D")
#             else:
#                 print("F")


# score = int(input("점수 입력 : "))

# if score >= 90 :
#     print("A")
# elif score >= 80 :
#      print("B")
# elif score >= 70 :
#      print("C")
# elif score >= 60 :
#      print("D")
# else :
#      print("F")

# a=input("인치를 입력하세요:")
# a=int(a)
# b=a*2.54

# print("inch:", a)
# print("cm:", b)


# pi=3.14
# r = int(input("반지름을 입력하세요:")) 

# print("원주율 = ", pi)
# print("반지름 = ", r)
# print("원의 둘레 =", 2*pi*r)
# print("원의 넓이 =", pi*r*r) 

# a=float(input("반지름을 입력하세요."))
# pi=3.14
# print("넓이 :", pi*a*a)
# print("넓이:", pi*a**2) 
# print("원의둘레:", 2*pi*a)

# str1="안녕하세요."
# print(str1[:1])
# print(str1[::-1]) 
# print(str1[:-1]) 
# print(str1[::2]) 
# print(len(str1))

# a=20
# print("{}".format(a))
# print("{:10d}".format(a))
# print("{:010d}".format(a))
# print("{:3d}".format(123456789))
# print("{:3,d}".format(123456789))
# print("{:.2f}".format(123456789))
# print("{:+010d}".format(a))
# print("{:+010d}",format(-10))

# import datetime
# import random
# now=datetime.datetime.now()

# print(now)
# print("{}년\t{:02d}월\t{}일\t{:02d}시\t{}분\t{}초".format(2026,8,29,9,22,41)) 

# r_num=random.randint(1,12)
# r_num=int(input("월을 입력허세요.:"))

# if r_num == 12 or r_num <= 2:
#     print("겨울입니다,")
# elif 3 <= r_num <= 5:
#     print("봄입니다.")
# elif 6 <= r_num <= 8:
#     print("여름입니다.")
# else:
#     print("가을입니다. ")

# if 3 <= r_num <= 5:
#     print("봄입니다.")
# elif 6 <= r_num <= 8:
#     print("여름입니다.")
# elif 9 <= r_num <=11:
#     print("가을입니다.")
# elif r_num == 12 or r_num <= 2:
#     print("겨울입니다,")
# else:
#     print("숫자를 입력해주세요. ")


# import random

# randint-랜덤1개, sample-랜덤여러개(중복불가),
# shuffle-전체섞음, choices-랜덤여러개(중복가능)

# lotto=random.sample(range(1,51),5)
# input1=int(input("숫자를 입력하세요:"))
# input2=int(input("숫자를 입력하세요:"))
# # input3=int(input("숫자를 입력하세요:"))
# input4=int(input("숫자를 입력하세요:"))
# input5=int(input("숫자를 입력하세요:"))

# if input1 in lotto:
#     print("당첨!!!") 
# elif input2 in lotto:
#     print("당첨")
# elif input3 in lotto:
#     print("당첨")
# elif input4 in lotto:
#     print("당첨")
# elif input5 in lotto:
#     print("당첨")
# else :
#     print("꽝")

# print("담첨숫자:", lotto)

# lotto=random.choice(range(1,51),5)
# iarr=[]
# iarr0.append=input("숫자를 입력하세요:")
# iarr1.append=input("숫자를 입력하세요:")
# iarr2.append=input("숫자를 입력하세요:")
# iarr3.append=input("숫자를 입력하세요:")
# iarr4.append=input("숫자를 입력하세요:")

# if iarr[0] in lotto: 
#     print("당첨!! ") else print("꽝")
# elif iarr[1] in lotto:
#      print("당첨!! ") else:print("꽝")
# elif iarr[2] in lotto:
#       print("당첨!! ") else:print("꽝")
# elif  iarr[3] in lotto:
#       print("당첨!! ") else:print("꽝")
# elif  iarr[4] in lotto:
#       print("당첨!! ") else:print("꽝")


# print("[학생성적프로그램 ]")
# s=[]
# no=input("번호 입력:")
# s.append(no)
# name=input("이름 입력:")
# s.append(name)
# kor=int(input("국어점수 입력:"))
# s.append(kor)
# eng=int(input("영어점수 입력:"))
# s.append(eng)
# math=int(input('수학점수 입력:'))
# s.append(math)
# total=kor+eng+math
# s.append(total)
# avg=total/3 
# s.append(avg)

# print("-" * 60)
# print("번호\t이름\t국어\t영어\t수학\t총점\t평균")
# print("-" * 60)
# print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}:.2f".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))


# 반복문을 사용해서 1~10까지 있는 합을 출력하시오.
# sum=0
# for i in range(1,11):
#     print(i)
#     sum=sum+i
#     print(sum)
# print("합계:",sum)


# # 100을 넘는 시점의 i의 값과 i번째의 합계를 출력하시오. 
# sum=0
# for i in range(1,1000):
#     print(i)
#     sum=sum+i
#     if sum > 100:
#         print("100보다 큰 수", i)
#         break
# print("합계:", sum)


# 100을 넘는 이전 시점의 i, 합계를 출력하시오.
# sum=0
# for i in range (1,100):
#      sum=sum+i
#      if sum > 100:
#         print("100보다 크기 바로 앞일 때:", i-1)
#         print("100보다 초과 전 시점:", sum-i)
#         break 
# print("합계:", sum)


# 구구단을 출력하시오.
for i in range(2,10):
     for j in range(1,10):
         print("{}x{}={}".format(i,j,i*j))


# no=[]
# name=[]
# kor=[]
# for i in range(3):
#     no.append(input("번호 입력:"))
#     name.append(input("이름 입력:"))
#     kor.append(int(input("국어점수 입력:")))
# for i in range(3):
#     print("{}\t{}\t{}".format(no[i],name[i],kor[i]))



# stu=[]
# for i in range(3):
#     no=i+1
#     name=input("이름 입력:")
#     kor=int(input("국어점수 입력:"))
#     stu.append([no, name, kor])
# for i in range(3):
#     print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))




