# 구구단을 아래로 출력하시오
# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j))

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end=" ")
# print()

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="\t")
# print()

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(j,i,i*j),end="\t")
#     print()

# 1x2=2   2x2=4   3x2=6   4x2=8   5x2=10  6x2=12  7x2=14  8x2=16  9x2=18
# 1x3=3   2x3=6   3x3=9   4x3=12  5x3=15  6x3=18  7x3=21  8x3=24  9x3=27
# 1x4=4   2x4=8   3x4=12  4x4=16  5x4=20  6x4=24  7x4=28  8x4=32  9x4=36
# 1x5=5   2x5=10  3x5=15  4x5=20  5x5=25  6x5=30  7x5=35  8x5=40  9x5=45

# for i in range(2,10):
#     print("[2단]", end="\t")
#     for j in range(1,10):
#         print("{}x{}={}".format(j,i,i*j),end="\t")
#     print()

# for i in range(2,10):
#     print(f"[{i}단]", end="\t")

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(j,i,i*j),end="\t")
# print()

# 합계 : 55
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print("합계:", sum)

# 1-10까지 곱:... 이렇게 출력하시오. 
# sum=0 # 더하기는 0부터 시작 
# result=1 # 곱하기는 1부터 시작 
# for i in range(1,11):
#     sum=sum+i
#     result=result*i
# print("합계:", sum)
# print("곱:", result)

# sum=0
# result=1
# for i in range(1,11):
#     sum=sum+i
#     result=result*i
# print("합계:", sum)
# print("곱:{:,}", result)

# 100을 넘는 처음 그 시점과 합계를 구하시오
#sum=0

# for i in range(1,101):
#      sum=sum+i
#      if sum > 100:
#           print(i,":", sum)
#           break # for을 정지해줌 강제 종료 

# for i in range(1,10):  
#     print(f"[{i}단]",end="\t")
# print()
# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(j,i,i*j),end='\t')
#     print()

# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#      sum=sum+i
#      if sum > 100:
#           no=i
#           sum2=sum
#           break
# print("합계가 100을 넘을때 i의 값:", no)
# print("그 때 합계:", sum2)        

# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#      sum=sum+i
#      if sum > 100:
         
#           sum2=sum
#           break
# print("합계가 100을 넘을때 i의 값:", no)
# print("그 때 합계:", no-1) 
# print("이전 단계:", sum2-no)


# sum=0
# no=0
# sum2=0
# for i in range(1,101):
#      sum=sum+i
#      if sum > 100:
         
#           sum2=sum
#           break
# print("합계가 100을 넘을때 i의 값:", no)
# print("그 때 합계:", no+1) 
# print("이전 단계:", sum2+no)

# 1~100까지의 합을 출력하시오.
# sum=0
# for i in range(1,101):
#     sum=sum+i

# print("합계:",sum)
   
# 홀수만 뽑아서 홀수 합을 구하시오.
sum=0
result=1

# for i in range(1,101,2):
#     print(i)
#     sum=sum+i

# print("홀수의 합:", sum)

# 7의 배수만 합을 구하시오.
# sum=0
# for i in range(1,101):
#     if i%7==0:
#         print(i)
#         sum=sum+i
# print("합계:", sum)

# 3개의 입력한 숫자의 합을 구하시오. 
# sum=0
# input1=int(input("숫자 입력:"))
# input2=int(input("숫자 입력:"))
# input3=int(input("숫자 입력:"))

# for i in range(1,101):
#     sum=sum+input1

# for i in range(1,101):
#     sum=sum+input2

# for i in range(1,101):
#     sum=sum+input3 

# print("합계:", sum)

# sum=0
# alist=[]
# input1=int(input("숫자 입력:"))
# input2=int(input("숫자 입력:"))
# input3=int(input("숫자 입력:"))

# for i in range(1,101):
#     alist.append(input1)
#     sum=sum+input1

# for i in range(1,101):
#     alist.append(input2)
#     sum=sum+input2

# for i in range(1,101):
#     alist.append(input3)
#     sum=sum+input3 

# print("합계:", sum)
# print("입력숫자:", alist)

# sum = 0
# alist = []
# for i in range(3):
#     input1 = int(input("숫자입력 : "))
#     alist.append(input1)
#     sum = sum + input1

# sum=0
# for i in range(1,11):
#     sum=sum+i
# print("합계:",sum)

# 입력한 첫번째 숫자부터 두번째 입력한 숫자까지 합을 구하시오.

# sum=0
# a=int(input("1.숫자 입력:"))
# b=int(input("2.숫자 입력:"))

# for i in range(a,b+1):
#     sum=sum+i
# print("합계:",sum)
    
# sum=0
# a=int(input("1.숫자 입력:"))
# b=int(input("2.숫자 입력:"))
# c=0 
# if a > b: # a가 클때만 값을 서로 변경함 
#     c=a
#     a=b
#     b=c
# for i in range(a,b+1):
#     sum=sum+i
# print("합계:",sum)

# # a,b=b,a 로 입력하면 a와 b 변수가 변경됨 

# 구구단을 출력하시오
# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j))

# for i in range(2,10):
#     print(f"[{i}단]",end="\t")
# print()
# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j), end="\t")
# print()

# 숫자입력, 5, 5단부터 출력하시오.
# sum=0 
# a=int(input("숫자 입력:"))

# for i in range(a,10):
#     print(f"[{i}단]")

# print()
# for i in range(a,10):
#     for j in range(1,b+1):
#         print("{}x{}={}".format(i,j,i*j))
# print()

# sum=0 
# a=int(input()"시작되는 단 입력:"")) 
# b=int(input("끝부분:"))

# for i in range(a,10):
#     print(f"[{i}단]")

# print()
# for i in range(a,10):
#     for j in range(1,b+1):
#         print("{}x{}={}".format(i,j,i*j))
# print()

# list_a=["바나나", "딸기", "사과"]
# # list_a.append(input("과일 입력:"))

# for i in range(1):
#     list_a.append(input("과일 입력:"))
    
# for i in list_a:
#     print(i)


# list_a=["바나나", "딸기", "사과"]

# for i in range(3):
#     list_a.append(input("과일 입력:"))
#     list_a.append(input("과일 입력:"))
#     list_a.append(input("과일 입력:"))
#     break

# for i in list_a:
#     print(i)

# 숫자입력, 5, 5단부터 출력하시오.
# sum = 0 
# a = int(input("숫자 입력: "))

# for i in range(a, 10):
#     print(f"[{i}단]", end="\t") 

# print()  # 단 이름 출력이 끝나고 줄바꿈

# for i in range(a, 10):
#     for j in range(1, a + 1):
#         # 1. 식들이 옆으로 나란히 붙도록 end="\t"를 넣어줍니다.
#         print("{}x{}={}".format(i, j, i * j), end="\t")
    
#     # 2. ★중요★ 한 단(i)의 j 반복문이 완전히 끝나면 줄을 한 번 바꿔줍니다.
#     print() 

# list_a=["바나나", "딸기", "사과"]
# for i in list_a:
#     print(i)

# for i in range(1,4): # i 는 for 문을 빠져 나오면 사라짐. 
#     print(i)

# print("for 문 밖 i:", i)

# for i in range(1,4):
#     print(i)

# print("for 문 밖 i:", i+5)

# 1. 바나나 2. 딸기 3. 사과로 출력하고 싶을 때 
list_a=["바나나", "딸기", "사과"]
# j=1 # 숫자 입력할 수 있는 변수 생성해야함. 
# for i in list_a:
#     print(j,":",i) # 1.바나나 2.딸기 3.사과 
#     j=j+1 

# for i, value in enumerate(list_a): # index 번호, 리스트값2개 전달받아서 출력 list 출력을 할 때에는 번호를 받을 수 없음. enumerate로 할 경우 번호 및 리스트 값 모두 받을 수 있음 
#     print(i+1, ":", value) # 0번부터 시작이기에 무조건 +1 을 작성해야함. # 리스트에 번호가 필요할 때 enumerate 사용

# list_a=["바나나", "딸기", "사과"]
# for i, value in enumerate(list_a): 
#     print(i+1, ":", list_a[1]) # 주소값을 사용함 

# for i in range(len(list_a)): 
#     print((i+1, ":", list_a[1]))

# 3명의 국어점수 입력받아 출력하시오. 

# no=[]
# name=[]
# kor=[]
# eng=[]
# math=[]


# for i in range(3):
#     no.append(input("번호 입력:"))
#     name.append(input("이름 입력:"))
#     kor.append(int(input("국어점수 입력:")))
#     eng.append(int(input("영어점수 입력:")))
#     math.append(int(input("수학점수 입력")))
    
# print("[학생 성적]")
# for i in range(len(no)):
#     print(f"{no[i]}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}")

# no=[]
# name=[]
# kor=[]
# eng=[]
# math=[]
# total=[]
# avg=[]

# for i in range(3):
#     no.append(input("번호 입력:"))
#     name.append(input("이름 입력:"))
#     k_input=int(input("국어점수 입력:"))
#     kor.append(k_input)
#     e_input=int(input("영어점수 입력:"))
#     eng.append(e_input)
#     m_input=int(input("수학점수 입력:"))
#     math.append(m_input)
#     total.append(k_input+e_input+m_input)
#     avg.append((k_input+e_input+m_input)/3)


# print("-"*60)    
# print("[학생 성적]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# for i in range(len(no)):
#     print(f"{no[i]}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\t{tatal[i]}\t{avg[i]:2f}")

# print("-"*60)    
                
name = []
kor = []
eng = []
math = []
total = []
avg = []
for i in range(3):
    name.append(input("이름입력 :"))
    k_input = int(input("국어점수입력 : "))
    kor.append(k_input)
    e_input = int(input("영어점수입력 : "))
    eng.append(e_input)
    m_input = int(input("수학점수입력 : "))
    math.append(m_input)
    total.append(k_input+e_input+m_input)
    avg.append((k_input+e_input+m_input)/3)

print("[ 학생성적 ]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t")
print("-"*60)
for i in range(len(name)):
    print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\
\t{total[i]}\t{avg[i]:.2f}") # i+1 은 번호 입력 
