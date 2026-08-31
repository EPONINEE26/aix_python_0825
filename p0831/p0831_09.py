# 로또 프로그램 구현하시오 

# import random
# # lotto=random.sample(range(1,46),6)
# # print("확인로또 : ",lotto)

# # no=[]
# # myNum=0
# # count=0
# # answer=[]

# # for i in range(6):
# #     myNum=int(input("숫자 입력 : "))
# #     no.append(myNum)
    
# # for n in no: # no 안에 있는 숫자 하나만 뽑아서 확인하는 곳. 
# #       if n in lotto:
# #         print('정답입니다.')
# #         count=count+1
# #         answer.append(n)
                
# # print("로또번호 : ", lotto)
# # print("정답번호 : ", answer)
# # print("정답개수 : ", count)
# # print("입력한숫자 : ", no)



# import random
# lotto=random.sample(range(1,46),6)
# print("확인로또 : ", lotto)

# myNum=[]
# no=0
# count=0
# answer=[]

# for i in range(6):
#     no=int(input("숫자 입력 : "))
#     myNum.append(no)

# for n in myNum:
#     if n in lotto:
#         print("정답입니다.")
#         count=count+1
#         answer.append(no)
# print("로또번호 : ", lotto)
# print("정답번호 : ", answer)
# print("정답개수 : ", count)
# print("입력한숫자 : ", myNum)


# 1. 번호,이름,국어,영어,수학
# 2. 합계,평균
# 3. 성적출력하도록 구성하시오.

# 입력 -> 변수저장 -> DB저장
s = [] #리스트타입 - append,insert / pop,del,remove
no = input("번호 입력 : ")      #str
name = input("이름 입력 : ")
kor = int(input("국어점수 입력 : "))  #int
eng = int(input("영어점수 입력 : "))  #int
math = int(input("수학점수 입력 : "))  #int
total = kor+eng+math
avg = total/3  # 나눗셈 -> float

print("[학생성적프로그램]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)  #문자*반복
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
#       format(no,name,kor,eng,math,total,avg))
# 

