# 로또 맞추기 
# 1. 랜덤번호 6개 생성
# 2. 입력번호 6개 생성
# 3. 랜덤번호와 입력번호 비교
# - for 입력번호 1개 가져와서 랜덤번호리스트와 비교, 
# - 해당 번호를 리스트에 추가 (count에 추가)
# 4. 결과 출력 

# import random
# lotto=random.sample(range(1,46),6) 
# print("확인로또 :", lotto)

# in_arr=[] # 입력한 번호 들어갈 리스트 
# no=0 # 변수 
# for i in range(6):
#     no=(input("1~45사이 숫자 입력 : ")) # 문자열 
#     # 10a를 입력하면 에러가 남. 
#     if no.isdigit(): # 문자열을 숫자로 변경가능한지 파악하는 함수 
#         no=int(input("1~45사이 숫자 입력 : "))
#         in_arr.append(no)

# answer_arr=[]

# for i in in_arr:
#     if i in lotto:
#         answer_arr.append(i)

# print("로또 번호 : ", lotto)
# print("입력 번호 : ", in_arr)
# print("정답 개수 : ", len(answer_arr))
# print("정답 번호 : " , answer_arr)

# 로또맞추기
# 1. 랜덤번호 6개 생성
# 2. 입력번호 6개 생성
# 3. 랜덤번호,입력번호 비교
# - for 입력번호 1개 가져와서 랜덤번호리스트와 비교
# - 있는 번호를 리스트에 추가
# 4. 결과 출력

import random
lotto = random.sample(range(1,46),6)
print("확인 : ",lotto)

in_arr = []
no = 0
for i in range(6):
    no = int(input("1-45사이 숫자입력 : "))
    in_arr.append(no)

    no = input("1-45사이 숫자입력 : ") #문자열
    if no.isdigit(): #문자열을 숫자로 변경가능한지
        no = int(input("1-45사이 숫자입력 : "))
        in_arr.append(no)

answer_arr = []
for i in in_arr:
    if i in lotto:
        answer_arr.append(i)

# 결과출력
print("로또번호 : ",lotto)
print("입력번호 : ",in_arr)
print("정답개수 : ",len(answer_arr))
print("정답번호 : ",answer_arr)