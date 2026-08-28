# 날짜 함수, 랜덤함수 
import datetime
import random
now=datetime.datetime.now()

#
# now=datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.date)
# print(now.hour)
# print(now.minute)
# print(now.second)

# random
# 3,4,5 봄, 6,7,8 여름, 9,10,11 가을, 12,1,2 겨울 
# r_num=random.randint(1,12)
# month=now.month
# month=int(input("월을 입력하세요."))

# if 3<= r_num <= 5:
#      print("봄입니다.")
# elif 6<= r_num <= 8:
#      print("여름입니다.")
# elif 9<= r_num <= 11:
#       print("가을입니다.")
# else:
#      print("겨울입니다.") 

# import random

# 리스트 생성 방법
# 랜덤 5개
# randint-랜덤1개, sample-랜덤여러개(중복불가),
# shuffle-전체섞음, choices-랜덤여러개(중복가능)
# a = random.randint(1,45) #랜덤1개
# arr = random.sample(range(1,46),5) #1-45까지 중복없이 5개를 가져옴.
# print(arr)
# arr2 = random.sample([1,2,3],2)
# print(arr2)
# arr3 = [1,2,3,4,5]  # 리스트 전체를 랜덤으로 섞어줌.
# random.shuffle(arr3)
# print(arr3)
# arr4 = [1,2,3,4,5]
# arr5 = random.choices(arr4,k=5) # 리스트 해당개수만큼 가져옴.중복가능
# print(arr5)

# # 리스트생성방법
# # alist1 = [0,0,0,0,0]
# # alist2 = [0]*5
# # alist3 = list(range(1,6))
# # print(alist1)
# # print(alist2)
# # print(alist3)

# # 1~45개 랜덤 5개 가져와서
# # 입력한 숫자가 있으면 당첨, 없으면 꽝
# # 1만 우선
# # 그 이후 5개

# lotto=random.sample(range(1,46),5)
# input1=int(input("숫자입력:"))

# # 비교해서 있으면 "당첨", 없으면 "꽝"
# if input1 in lotto:
#     print("당첨!!")
# else:
#     print("꽝")

# lotto=random.sample(range(1,46),5)
# input1=int(input("숫자입력:"))
# input2=int(input("숫자입력:"))
# input3=int(input("숫자입력:"))
# input4=int(input("숫자입력:"))
# input5=int(input("숫자입력:"))

# if input1 in lotto:
#     print("당첨!!")
# elif input2 in lotto:
#        print("당첨!!")
# elif input3 in lotto:
#        print("당첨!!")
# elif input4 in lotto:
#        print("당첨!!")
# else:
#     print("꽝")


# lotto=random.sample(range(1,46),5)
# input1=int(input("숫자입력:"))
          
# if input1 in lotto:
#     print("당첨!!")
# else:
#     print("꽝")


# lotto=random.sample(range(1,46),5)
# iarr=[]
# iarr.append(int(input("숫자입력:")))
# iarr.append(int(input("숫자입력:")))
# iarr.append(int(input("숫자입력:")))
# iarr.append(int(input("숫자입력:")))
# iarr.append(int(input("숫자입력:")))

# if iarr[0] in lotto:
#     print("당첨!! ")
# elif iarr[1] in lotto:
#     print("당첨!! ")
# elif iarr[2] in lotto:
#     print("당첨!! ")
# elif  iarr[3] in lotto:
#     print("당첨!! ")
# elif  iarr[4] in lotto:
#     print("당첨!! ")
# else: 
#     print("꽝")

# if iarr[0] in lotto:
#     print("당첨!! ") else:print("꽝")
# elif iarr[1] in lotto:
#     print("당첨!! ") else:print("꽝")
# elif iarr[2] in lotto:
#     print("당첨!! ") else:print("꽝")
# elif  iarr[3] in lotto:
#     print("당첨!! ") else:print("꽝")
# elif  iarr[4] in lotto:
#     print("당첨!! ") else:print("꽝")

# for i in rnage(5):
#     if iaar[1] in lotto: print("당첨")
# else: print("꽝")


# # 반복문
# for i in range(5):
#     iarr.append(int(input("숫자입력:")))

# a=[1,2,3,4,5]
# a[2]=30 # 해당된 주소값에 변경 값을 넣으면 변경됨 
# print(a)
# a[3]=500
# print(a)
# a.pop(2)
# print(a)
# a.append(200) # 맨 뒤에 추가 됨 
# print(a)

