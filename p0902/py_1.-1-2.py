# import random
# lotto=random.sample(range(1,46),6)
# print("확인로또 : " , lotto)

# arr1=[]
# no=0
# for i in range(6):
#     no=int(input("1~45사이 숫자 입력 : "))
#     arr1.append(no)

# answer_arr=[]

# for i in arr1:
#     if i in lotto:
#         answer_arr.append(i)

# print("로또 번호 : ", lotto)
# print("입력 번호 : ", arr1)
# print("정답 번호 :  ", answer_arr)
# print("정답 개수 : ", len(answer_arr))

# import random

# num1 = random.randint(1, 100)
# num2 = random.randint(1, 100)
# num3 = random.randint(1, 100)

# arr1 = [num1, num2, num3]
# arr2 = random.sample(range(1, 101), 3)
# arr1.sort()
# print(arr1)
# print(arr2)

# input1 = int(input("숫자 입력:"))

# if input1 in arr1:
#     print("당첨!!")
# else:
#     print("꽝 ^^")

# # ★ 검사 대상에 맞게 출력 화면도 arr1(당첨번호)로 매칭했습니다!
# print("랜덤숫자:", arr1)
# print("입력숫자:", input1)





















# import random

# ran1 = random.randint(1, 100)  # 1~100 사이이므로 101 대신 100으로 수정 (선택사항)
# my_list = []
# myNum = 0
# answer = ran1  # 정답 숫자를 ran1으로 저장하여 하단에 출력되도록 수정

# while True:
#     myNum = int(input("1~100 사이 숫자 입력 : "))
#     my_list.append(myNum)
#     print(myNum)
    
#     if myNum == ran1:
#         print("정답입니다.")
#         break  # 정답을 맞췄을 때만 반복문을 빠져나갑니다.
#     elif myNum > ran1:
#         print("랜덤숫자보다 큽니다. 작은 수 입력 : ")
#     else:
#         print("랜덤숫자보다 작습니다. 큰 수 입력 : ")

# # 반복문 종료 후 최종 결과 출력
# print("내가 입력한 마지막 숫자 : ", myNum)
# print("정답숫자 : ", answer)
# print("입력한 모든 숫자 목록 : ", my_list)

# import random
# ran1=random.randint(1,101)
# my_list=[]
# myNum=0
# answer=0   
    

# while True:
#     myNum=int(input("1~100 사이 숫자를 입력 : "))
#     my_list.append(myNum)
#     print(myNum)
#     if myNum==ran1:
#         answer=myNum
#         print("정답입니다.")
#     elif myNum > ran1:
#         print("랜덤번호보다 큽니다. 작은수 입력 : ")
#     else: 
#         print("랜덤번호보다 작습니다. 큰수 입력 : ")
#         break 

# print("랜덤번호 : ", myNum)
# print("정답숫자 : ", answer)
# print("입력숫자 : ", my_list)


# def stu_print(): 
#     for s in stu:
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
# stu = [ 
#     [1, "홍길동", 100, 100, 100, 300, 100.0],
#     [2, "유관순", 100, 100, 100, 300, 100.0],
#     [3, "이순신", 100, 100, 100, 300, 100.0],
# ]

# stu[0][2] = 90
# stu[0][5] = stu[0][2] + stu[0][3] + stu[0][4]
# stu[0][6] = stu[0][5] / 3

# while True:
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("3. 학생성적검색")

#     choice = int(input("원하는 번호를 입력하세요.>>"))
#     if choice == 1:
#         name=input("학생이름입력 (0. 이전페이지 이동):")
#         if name=="0": break
        
#         # 학생전체출력 
#         stu_print()
#     elif choice == 2:
#         # 학생출력하는 구문 
#         print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#         # 학생전체출력
#         stu_print()
#     else: 
#         name = input("이름을 입력하세요.")
#         # 학생전체출력 
#         stu_print() 



# from gugudan_01 import gugudan_func

# def gugudan_func():
#     for step in range(2, 10, 3):
#         for i in range(step, min(step + 3, 10)):
#             print(f"[{i}단]", end="\t")
#         print()
#         for i in range(1, 10):
#             for j in range(step, min(step + 3, 10)):
#                 print("{}X{}={}".format(j, i, i * j), end="\t")
#             print()
#         print()

# gugudan_func()

# from gugudan_01 import gugudan_func

# def gugudan_func():
#     for step in range (2, 10, 3): 
#         for i in range(step, min(step + 3, 10)):
#             print(f"[{i}단]", end="\t") 
#         print() 
#         for i in range(1,10): 
#             for j in range(step, min(step + 3, 10)):
#                 print("{}x{}={}".format(j, i, i*j), end="\t")
#             print()
#         print() 

# gugudan_func() 

# from gugudan_01 import gugudan_func

# def gugudan_func():
#     # 1. 첫 번째 줄: 큰 틀을 잡는 바깥쪽 for step 문
#     for step in range(2, 10, 3):
        
#         # 2. 두 번째 줄: 제목 단을 가로로 출력하는 for i 문
#         for i in range(step, min(step + 3, 10)):
#             print(f"[{i}단]", end="\t")
#         print() # 제목 출력이 끝나면 줄바꿈!
        
#         # 3. 세 번째 줄: 1부터 9까지 곱해주는 값을 담당하는 두 번째 for i 문
#         for i in range(1, 10):
            
#             # 4. 네 번째 줄: 가로로 3칸씩 식을 나열해 주는 핵심 for j 문
#             # (이 문장이 3번째 줄 안쪽으로 들여쓰기가 되어야 2~9단이 3칸씩 안 깨지고 다 나옵니다!)
#             for j in range(step, min(step + 3, 10)):
#                 # ★ 필기하신 주석 내용 그대로: i, j 자리변경으로 출력이 바뀜!
#                 print("{}X{}={}".format(j, i, i * j), end="\t")
#             print() # 가로로 3개 식이 나오면 줄바꿈!
#         print() # 한 묶음이 끝나면 빈 줄 추가

# # ★ 화면에 구구단 전체가 3칸씩 튀어나오게 만드는 최종 실행 명령어!
# gugudan_func()









