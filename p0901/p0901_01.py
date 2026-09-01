# 구구단
# for i in range(2,9+1):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j))

# 1-100 사이의 맞추기 
# 1. 랜덤번호 생성
# 2. 무한으로 입력받기 
# 3. 숫자를 입력받기 
# 4. 랜덤번호화 숫자 비교
# 5. 결과출력 

# import random
# ran_no=random.randint(1,100)
# in_arr=[]

# # 반복문 : for-반복/횟수가 지정이 된 것, while-조건
# in_no=0 # 입력변수 
# while True:
#     in_no=int(input("1~100사이 숫자입력 : ")) # 숫자입력 
#     in_arr.append(in_no) # 입력한 숫자를 리스트에 넣기 
#     if in_no==ran_no:
#         print("정답입니다.")
#         break
#     elif in_no > ran_no:
#         print(in_no, "보다 작은 수를 입력하세요.")
#     else:
#         print(in_no, "보다 큰 수를 입력하세요.")

# print("입력한 모든 리스트 : ", in_arr)
# print("정답 : ", in_no)
# print("정답 : ", in_arr[-1]) 


