# for step in range(2,10,3):
#     for i in range(step, min(step + 3,10)):
#         print(f"[{i}단]",end="\t")
#     print()
#     for i in range(1,10):
#         for j in range(step, min(step +3, 10)):
#             print("{}X{}={}".format(j,i,i*j),end="\t") # i,j 자리변경을로 출력이 바뀜
#         print()

#     print()



stu_list=[]
while True:
    print("[ 학샹성적프로그램 ]")
    print("-"*60)
    print("1. 학생입력")
    print("2. 학생출력")
    print("3. 학생성적수정")
    print("4. 학샹성적삭제")
    print("5. 학생검색")
    print("6. 학생이름정렬")
    print("7. 학생성적정렬")
    print("0. 프로그램종료")


    choice=int(input("원하는 번호를 입력하세요.>>"))
    if choice ==1:
        print("[ 학생성적프로그램 ]")
        while True:
            no=len(stu_list)+1
            print("자동번호 : ", no)
            name=input("이름 입력 (종료하려면 o): ")
            if name=="0": break
            kor=int(input("국어점수 입력: "))
            eng=int(input("영어점수 입력: "))
            math=int(input("수학점수 입력: "))
            total=kor+eng+math
            avg=total/3 
            stu_list.append([no, name, kor, eng, math, total, avg])
            print(name, "학생성적이 등록되었습니다.")
            print()

    elif choice ==2:
        print("[ 학생성적출력 ] ")
        print("입력된 학생성적 : ", len(stu_list)) 
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*2))

    elif choice==3:
        print("[ 학생성적수정 ]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        
    elif choice==4:
        print("[학생성적삭제 ]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)

    elif choice==5:
        print("[ 학생검색 ]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)

    elif choice==6:
        print("[ 학생이름정렬 ]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)

    elif choice==7:
        print("[ 학생성적정렬 ]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)

    else:
        print("[ 프로그램종료 ]")
    break

print(stu_list )
print("-"*60)




# stu_list=[]

# while True:
#     print("[ 학생성적프로그램 ]")
#     print("-"*60)
#     print("1. 학새입력")
#     print("2. 학생출력")
#     print("3. 학생성적수정")
#     print("4. 학생성적삭제")
#     print("5. 학생검색")
#     print("6. 학생이름정렬")
#     print("7. 학생성적정렬")
#     print("0. 프로그램종료")
#     choice = int(input("원하는 번호를 입력하세요.>>")) 
#     if choice ==1:
#         print("[ 학생성적프로그램 ]")
#         while True:
#             no=len(stu_list)+1
#             print("자동번호 : ", no)
#             name=input("이름 입력 (종료하려면 0): ")
#             if name=="0": break 
#             kor=int(input("국어점수 입력 : "))
#             eng=int(input("영어점수 입력 : "))
#             math=int(input("수학점수 입력 : "))
#             total=kor+eng+math
#             avg=total/3 
#             stu_list.append([no, name, kor, eng, math, total, avg])
#             print(name, "학생성적이 등록되었습니다.")
#             print()
#     elif choice==2:
#         print("[ 학생성적출력 ]")
#         print("입력된 학생성적 :", len(stu_list))
#         print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#         print("-"*60)
#         for s in stu_list:
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
#     elif choice==3:
#         print("[ 학생성적수정 ]")
#         print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#         print("-"*60)
#         for s in stu_list:
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
#     elif choice==4:
#         print("[학생성적삭제 ]")
#         print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#         for s in stu_list:
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
#     elif choice==5:
#         print("[ 학생검색 ]")
#         print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#         for s in stu_list:
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))

#     elif choice==6:
#         print("[ 학생이름정렬 ]")
#         print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#         for s in stu_list:
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))

#     elif choice==7:
#         print("[ 학생성적정렬 ]")
#         print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#         for s in stu_list:
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))

#     else:
#         print("[ 프로그램종료 ]")
#     break

# print(stu_list )
# print("-"*60)



# # 로또 맞추기 
# # 1. 랜덤번호 6개 생성
# # 2. 입력번호 6개 생성
# # 3. 랜덤번호와 입력번호 비교
# # - for 입력번호 1개 가져와서 랜덤번호리스트와 비교, 
# # - 해당 번호를 리스트에 추가 (count에 추가)
# # 4. 결과 출력 


# # import random
# # ran_no=random.randint(1,100)
# # in_no=0
# # in_arr=[]

# # while True:
# #     in_no=int(input("1~100사이 숫자를 입력하세요 : "))
# #     in_arr.append(in_no)

# #     if in_no == ran_no:
# #         print("정답입니다.")
# #         break
# #     elif in_no > ran_no:
# #         print(in_no , "보다 작은 수 입력하세요.")
# #     else:
# #         print(in_no , "보다 큰 수 입력하세요.")

# # print("입력한 모든 수 : ", in_arr)
# # print("정답 번호 : ", in_no)
# # print("정답 번호 : ", in_arr[-1])


# import random
# lotto = random.sample(range(1,46),6)
# print("확인 : ",lotto)

# in_arr = []
# no = 0
# for i in range(6):
#     no = int(input("1-45사이 숫자입력 : "))
#     in_arr.append(no)

#     no = input("1-45사이 숫자입력 : ") #문자열
#     if no.isdigit(): #문자열을 숫자로 변경가능한지
#         no = int(input("1-45사이 숫자입력 : "))
#         in_arr.append(no)

# answer_arr = []
# for i in in_arr:
#     if i in lotto:
#         answer_arr.append(i)

# # 결과출력
# print("로또번호 : ",lotto)
# print("입력번호 : ",in_arr)
# print("정답개수 : ",len(answer_arr))
# print("정답번호 : ",answer_arr)



# import random
# ranNum=random.sample(1,100)
# my_list=[]
# myNum=0
# answer=0
# while True:
#     myNum=int(input("1~100 사이의 숫자 입력 : "))
#     my_list.append(myNum)

#     if myNum==randNun:
#         answer=myNum
#         print("정답입니다.")
#         break 
#     elif myNum > ranNum:
#         print("입력 숫자가 더 큽니다. 작은수 입력!!")
#     elif myNum < ranNum:
#         print("입력 숫자가 더 적습니다. 큰 수 입력!!")
# print("정답 : ", answer)
# print("접답 : ", my_list[-1])
# print("입력한 모든 숫자 : ", my_list)
# print("프로ㄱ그램종료 ")


import random

lotto = random.sample(range(1, 46), 6)
print("확인로또 :", lotto)

in_arr = [] # 내가 입력한 모든 수를 모아두는 리스트 

for i in range(6):
    no = int(input("1~45사이 숫자 입력 : "))  # 이미 int로 변환됨!
    in_arr.append(no)  # isdigit 검사 없이 바로 추가

answer_arr = [] # 정답만 따로 모아두는 리스트 

for i in in_arr:
    if i in lotto:
        answer_arr.append(i)

print("로또 번호 : ", lotto)
print("입력 번호 : ", in_arr)
print("정답 개수 : ", len(answer_arr))
print("정답 번호 : ", answer_arr)



import random
lotto = random.sample(range(1, 46), 6)
print("확인로또 :", lotto)

in_arr = []

for i in range(6):
    no = input("1~45사이 숫자 입력 : ")  # 1. 일단 문자열로 입력받기

    if no.isdigit():  # 2. isdigit()으로 숫자로 바꿀 수 있는지 검사
        no = int(no)  # 3. 검사 통과 후 int()로 변경
        in_arr.append(no)

answer_arr = []

for i in in_arr:
    if i in lotto:
        answer_arr.append(i)

print("로또 번호 : ", lotto)
print("입력 번호 : ", in_arr)
print("정답 개수 : ", len(answer_arr))
print("정답 번호 : ", answer_arr)


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

# import random
# lotto = random.sample(range(1,46),6)
# print("확인 : ",lotto)

# in_arr = []
# no = 0
# for i in range(6):
#     no = int(input("1-45사이 숫자입력 : "))
#     in_arr.append(no)

#     no = input("1-45사이 숫자입력 : ") #문자열
#     if no.isdigit(): #문자열을 숫자로 변경가능한지
#         no = int(input("1-45사이 숫자입력 : "))
#         in_arr.append(no)

# answer_arr = []
# for i in in_arr:
#     if i in lotto:
#         answer_arr.append(i)

# # 결과출력
# print("로또번호 : ",lotto)
# print("입력번호 : ",in_arr)
# print("정답개수 : ",len(answer_arr))
# print("정답번호 : ",answer_arr)