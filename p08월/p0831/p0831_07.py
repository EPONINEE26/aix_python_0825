# import random
# noArr=[10.40,2,9,5]
# myNum=[]

# for i in range(6):
#     no=int(input("숫자입력 : "))
#     myNum.append(no)

# print("입력숫자 : ", myNum)

# import random
# myNum=[]

# for i in range(6):
#     no=int(input("숫자입력 : "))
#     if no not in myNum:
#        myNum.append(no)
#     else:
#       print("번호가 있습니다.")
   

# print("입력숫자 : ", myNum)

# import random
# myNum=[]

# for i in range(6):
#     no=int(input("숫자입력 : "))
#     if no not in myNum:
#        myNum.append(no)
#     else:
#       print("번호가 있습니다.")
   

# print("입력숫자 : ", myNum)

# import random
# myNum=[]
# i=0 
# while i<6:
#   no=int(input("숫자입력 : "))
#   if no not in myNum:
#        myNum.append(no)
#        i=i+1 
#   else:
#       print("번호가 있습니다.")
   

# print("입력숫자 : ", myNum)

# import random

# a=random.randint(1,46) # 1개 랜덤 
# print(a)
# alist=list(range(1,46))
# random.shuffle(alist) # 리스트 섞어줌 같은 번호는 나올 수 없음  
# print(alist)

# random.sample(1.46,6) # 램덤으로 개수만큼 추출. 중복 불가 
# ranArr=random.sample(range(1.46),6)
# print(ranArr)

# ranArr2=random.choice(range(1,46),6) # 램덤으로 개수만큼 추출. 중복 가능 
# print(ranArr2)

import random

# lotto=random.sample(range(1,46),6)
# print("로또 번호 : ", lotto) # 로또 번호 추출 

# 입력한 숫자 1개가 맞는지 출력하시오.

# lotto=random.sample(range(1,46),6)
# print("확인로또>> : ", lotto)
# Arr=[]
# inputNo=0
# answer=0

# for inputNo in lotto:
#     Arr.append(inputNo)
#     if inputNo in Arr:
#         print("정답입니다.")
# else:
#     print("없습니다.")

# print("로또번호 : ", lotto)
# print("정답번호 : ", answer)
# print("정답개수 : ", Arr)

import random

# # 로또 랜덤부분
# lotto = random.sample(range(1,46),6)

# # 6개 입력부분
# myNum = []  # 6개 입력
# i = 0
# while i<6:
#     no = int(input("숫자입력 : "))
#     if no not in myNum:
#         myNum.append(no)
#         i = i+1
#     else:
#         print("번호가 있습니다.")

# # 정답확인 부분
# answer = []
# count = 0
# for i in myNum:
#     if i in lotto:
#         count = count + 1
#         answer.append(i)

lotto = random.sample(range(1,46),6)
# print("확인로또>> : ", lotto)
myNum = []
count = 0
answer = []
i=0


for i in range(6):
    no=int(input("숫자입력 :"))
    myNum.append(no)
    i = i+1 
    if i in myNum:
        count=count+1
        answer.append(i)
                        
print("로또번호 : ", lotto)
print("입력한 번호 : ", myNum)
print("정답번호 : ", answer)
print("정답개수 : ", count)

import random

lotto = random.sample(range(1, 46), 6)
myNum = []
count = 0
answer = []

# 숫자를 6개 입력받는 과정
for i in range(6):
    no = int(input("숫자입력 :"))
    myNum.append(no)

# ★수식 변경 없이 위치(들여쓰기)를 밖으로 빼고, 변수 i를 n으로 맞춰서 비교합니다.
for n in myNum:
    if n in lotto:  # 입력한 번호(n)가 로또 번호(lotto) 안에 있는지 검사
        count = count + 1
        answer.append(n)
                        
print("로또번호 : ", lotto)
print("입력한 번호 : ", myNum)
print("정답번호 : ", answer)
print("정답개수 : ", count)


















# import random
# # 1개 랜덤
# a = random.randint(1,45)
# print(a)
# # 리스트를 섞어줌.
# alist = list(range(1,46))
# print(alist)
# random.shuffle(alist)
# print(alist)
# # 랜덤으로 개수만큼 추출 - 중복이 안됨.
# ranArr = random.sample(range(1,46),6)
# print(ranArr)

# # 랜덤으로 개수만큼 추출 - 중복가능
# ranArr2 = random.choices(range(1,46),k=6)
# print(ranArr2)


# myNum = []  # 6개 넣어야 하는데
# i = 0
# while i<6:
#     no = int(input("숫자입력 : "))
#     if no not in myNum:
#         myNum.append(no)
#         i = i+1
#     else:
#         print("번호가 있습니다.")

# print("입력숫자 : ",myNum)

# for i in range(6):
#     no = int(input("숫자입력 : "))
#     if no not in myNum:
#         myNum.append(no)
#     else:
#         print("번호가 있습니다.")