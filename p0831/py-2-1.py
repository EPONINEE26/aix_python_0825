# 구구단을 출력하시오 

# for i in range(2,10):
#     for j in range(1, 10):
#         print("{}x{}={}".format(i,j, i*j))

# for i in range(2,10):
#         for j in range(1,10):
#             print("{}x{}={}".format(i,j, i*j), end="\t")

# for i in range(2,10):
#     print("{}단".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j), end="\t")

# for i in range(2, 10):
#     print("{}단".format(i))  # 1. 단 이름을 먼저 위에 딱 한 번 출력합니다.
#     for j in range(1, 10):
#         print("{}x{}={}".format(i, j, i*j), end="\t")  # 2. 그 아래에 곱하기를 옆으로 출력합니다.
#     print()  # 3. 한 단(1~9)이 다 끝나면 줄을 바꿉니다.

# for i in range(2, 10):
#     print("{}단".format(i))  # 1. 단 이름을 먼저 위에 딱 한 번 출력합니다.
#     for j in range(1, 10):
#         print("{}x{}={}".format(j, i, i*j), end="\t")  # 2. 그 아래에 곱하기를 옆으로 출력합니다.
#     print()  # 3. 한 단(1~9)이 다 끝나면 줄을 바꿉니다.


# n = int(input("시작할 단의 숫자를 입력하세요: "))
# for i in range(n, 10):  # 1. 1 대신 입력받은 'n'을 넣어야 4단부터 시작합니다!
#     print("{}단".format(i))  # 2. 단 이름이 맨 위에 먼저 나옵니다.
#     for j in range(1, 10):
#         print("{}x{}={}".format(i, j, i*j), end="\t")
#     print()  # 3. [중요] 이 print()는 반드시 'for j'보다 한 칸 앞으로 나와서 이 위치에 있어야 합니다!

# sum=0
# for i in range(1,11):
#     sum=sum+i
# print("합계 : ", sum)

sum=0
result=1


# sum = 0
# result = 1

# for i in range(1, 11):
#     sum = sum + i       # 빈 줄 없이 for문 바로 아랫줄에 붙여 씁니다!
#     result = result * i  # 공백(들여쓰기)을 똑같이 맞춰줍니다!
# print("합계 : ", sum)
# print("곱 : ", result)


# sum=0
# for i in range(1,101):
#     sum = sum + i
#     if sum > 100:
#         print(i, ":", sum)
#         break 

# sum=0
# no=0
# sum2=0

# for i in range(1,101):
#     sum = sum + i
#     if sum > 100:
#         no=i
#         sum2=sum
#         break
# print(" 합계가 100을 넘을 때 i값 :", no) 
# print("그 때 합계 : ", sum2)

# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#     sum=sum+i
#     if sum > 100:
#         no = i        # [핵심 추가] 100을 넘을 때의 i 값을 no에 저장합니다!
#         sum2 = sum    # 100을 넘었을 때의 합계를 저장합니다 (105)
#         break
# print("합계가 100을 넘을때 i의 값:", no)
# print("그 때 합계:", no-1) 
# print("이전 단계:", sum2-no)

# 합계가 100을 넘을때 i의 값: 14 # 숫자번호 
# 그 때 합계: 13 # 숫자번호 
# 이전 단계: 91


# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#     sum=sum+i
#     if sum > 100:
#         no = i        # [핵심 추가] 100을 넘을 때의 i 값을 no에 저장합니다!
#         sum2 = sum    # 100을 넘었을 때의 합계를 저장합니다 (105)
#         break
# print("합계가 100을 넘을때 i의 값:", no)
# print("그 때 합계:", no+1) # 100이 넘었을 때 14번째 숫자 번호에서 하나 증감하기에 15가 출력이 되는 것임. 
# print("이전 단계:", sum2+no)

# 합계가 100을 넘을때 i의 값: 14 # 숫자번호 
# 그 때 합계: 15 # 숫자번호 
# 이전 단계: 119


# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#     sum=sum+i
#     if sum > 100:
#         no = i        # [핵심 추가] 100을 넘을 때의 i 값을 no에 저장합니다!
#         sum2 = sum    # 100을 넘었을 때의 합계를 저장합니다 (105)
#         break
# print("합계가 100을 넘을때 i의 값:", no)
# print("그 때 합계:", sum2+1) # 15번째 숫자 번호의 합걔가 106이기에 1이 증감되어서 출력이 됨. 
# print("이전 단계:", sum2+no)

# 합계가 100을 넘을때 i의 값: 14 # 숫자번호 
# 그 때 합계: 106 숫자의 합 
# 이전 단계: 119

# sum=0 (질문)
# input1=int(input("숫자 입력:"))
# input2=int(input("숫자 입력:"))
# input3=int(input("숫자 입력:"))

# for i in range(1,101):
#      sum=sum+input1

# for i in range(1,101):
#      sum=sum+input2

# for i in range(1,101):
#      sum=sum+input3 

# print("합계:", sum)

# sum=0 (질문)
# alist=[]
# input1=int(input("숫자입력:"))
# input2=int(input("숫자입력:"))
# input3=int(input("숫자입력:"))

# for i in range(1,101):
#     alist.append(input1)
#     sum=sum+input1 

# for i in range(1,101):
#     alist.append(input2)
#     sum=sum+input2 

# nums = [3, 9, 10, 105, 220, 2, 1]

# for n in nums:
#     # 이 자리에 있던 print(n)을 지웠습니다!
    
#     n = int(input("숫자 입력: "))
    
#     if n % 2 == 0:
#         print(n, ": 짝수입니다.")
#     else:
#         print(n, ": 홀수입니다.")


# for i in range(1,11):
#     print(i)

# print("-"*50)
# i=1
# while(i<=11): # 조건문이 참일 때만 조건문이 실행됨 
#     print(i)
#     i+=1


# alist=list(range(10))
# i=0
# while i<10:
#     print(alist[i], end=" ")
#     i=i+1 

# i = 0
# while True:
#     print(i)
#     if i % 10 == 0:
#         # 이 자리에 'input1 =' 을 적어서 파이썬에게 알려줍니다.
#         input1 = input("프로그램을 종료할까요?") 
        
        
#         if input1 == "x": 
#             break 
#     # i+=1 수식의 들여쓰기를 이 위치로 맞춰야 숫자가 정상적으로 올라갑니다.
#     i += 1 

# print()


# import random
# ran1=random.randint(1,100)
# myNum=0
# while True:
#     myNum = int(input("1~100사이 숫자를 입력 : "))
#     print(myNum) 
#     if myNum== ran1: # 랜덤 숫자와 입력숫자가 같은지 비교  
#         print("정답입니다.")
#         break 
#     elif myNum > ran1:
#         print("입력한 숫자가 더 큽니다. 작은수 입력:")
#     else :
#         print("입력한 숫자가 더 작습니다. 큰수 입력")

# print("프로그램 종료")

# import random
# ran1=random.randint(1,100)
# my_list=[] # 입력한 숫자 모두 저장 공간을 리스트로 생성 
# myNum=0 # 내가 입력한 숫자 변수 
# answer=0 
# while True:
#     myNum = int(input("1~100사이 숫자를 입력 : "))
#     my_list.append(myNum)
#     print(myNum) 
#     if myNum== ran1: # 랜덤 숫자와 입력숫자가 같은지 비교
#         answer = myNum
#         print("정답입니다.")
#         break 
#     elif myNum > ran1:
#         print("입력한 숫자가 더 큽니다. 작은수 입력:")
#     else :
#         print("입력한 숫자가 더 작습니다. 큰수 입력")

# print("정답 :", answer)
# print("정답 :", my_list[-1])
# print("입력한 모든 숫자:", my_list)
# print("프로그램 종료")

# # 1~100까지 랜덤숫자 1개를 생성
# # 내가 입력한 모든 숫자가 출력
# # 랜덤숫자를 맞출때까지 무한반복 프로그램을 구현하시오.
# import random
# randNum = random.randint(1,100) # 랜덤숫자생성
# my_list = []    # 입력한숫자모두저장
# myNum = 0       # 내가입력한숫자변수
# answer = 0      # 정답변수
# while True:
#     myNum = int(input("1-100사이 숫자를 입력 : "))
#     my_list.append(myNum)

#     # 랜덤숫자와 입력숫자가 같은지 비교
#     if myNum == randNum:
#         answer = myNum
#         print("정답입니다.")
#         break
#     elif myNum>randNum:
#         print("입력한 숫자가 더 큽니다. 작은수 입력!!")
#     else:
#         print("입력한 숫자가 더 작습니다. 큰수 입력!!")

# print("정답 : ",answer)
# print("정답 : ",my_list[-1])
# print("입력한모든 숫자 : ",my_list)

# print("프로그램 종료")


# import random
# noArr=[10.40,2,9,5]
# no=[]
# i=0
# count=0
# answer=0
# while True:
#     i_no=int(input("숫자입력 : "))
#     no.append (i_no)

#     if i_no==0: 
#         break 
#     # 0을 입력할 때 종료 
# for i in no:
#     if i in noArr:
#         count=count+1
#         answer.append(i) # 입력 숫자가 정답일 때 i 값을 입력


# # 종료할 때 입력된 숫자 모두 출력 
# print("리스트 : ", noArr)
# print("입력숫자 : ", no)
# print("정답숫자 : ", answer)
# print("정답개수 : ", count)


# import random

# lotto=random.sample(range(1,46),6) 
# print("확인로또>>", lotto)

# myNum=[]
# count=0
# answer=[]
# i=0

# for i in range(6):
#     no=int(input("숫자입력:"))
#     myNum.append(no)
#     i=i+1
#     if i in myNum:
#         count=count+1
#         answer.append(i)

# print("로또번호 : ", lotto)
# print("입력한 번호 : ", myNum)
# print("정답번호 : ", answer)
# print("정답개수 : ", count)

# import random

# lotto=random.sample(range(1,46),6)
# myNum=[]
# count=0
# answer=[]
# i=0

# for i in range(6):
#     no=int(input("숫자 입력:"))
#     myNum.append(no)

# for n in myNum:
#     if n in lotto:
#         count=count+1
#         answer.append(m)
                       
# print("로또번호 : ", lotto)
# print("입력한 번호 : ", myNum)
# print("정답번호 : ", answer)
# print("정답개수 : ", count)

no = []
name = []
kor = []
eng = []
math = []
total = []
avg = []

for i in range(3):
    no.append(input("번호 입력:"))  # 괄호 닫기 추가 )
    name.append(input("이름 입력:"))  # 괄호 닫기 추가 )
    k_input = int(input("국어점수 입력:"))  # 괄호 닫기 추가 )
    kor.append(k_input)
        e_input = int(input("영어점수 입력:"))  # e_input(int(..) -> e_input = int(..) 수정
    eng.append(e_input)
        m_input = int(input("수학점수 입력:"))  # 괄호 닫기 추가 )
    math.append(m_input)  # 누락되었던 수학 점수 리스트 저장 추가
    total.append(k_input + e_input + m_input)
    avg.append(k_input + e_input + m_input)

print("[학생성적프로그램]")
print("-" * 60)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
for i in range(3):
     print(f"{no[i]}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\t{total[i]}\t{avg[i]:.2f}")


