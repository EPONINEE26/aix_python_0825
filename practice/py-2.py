# import random

# def main_print():
#     print("1. 구구단 출력프로그램")
#     print("2. 1-10까지 숫자맞추기 프로그램")
#     print("3. 두 수를 입력받아 +,-.*,/ 결과값 출력프로그램")
#     choice = int(input("원하는 번호입력 : "))
#     return choice 

# def gugudan_func():
#     for step in range(2, 10, 3): 
#         for i in range(step, min(step + 3, 10)):
#             print("[{}단]".format(i), end="\t")
#         print()

#         for i in range(1, 10):
#             for j in range(step, min(step + 3, 10)):
#                 print("{}x{}={}".format(j,i,j*i), end="\t")
#             print()
#         print()

# def number_func():
#     ran_num = random.randint(1, 10)
#     while True:
#         in_num = int(input("1-10까지 숫자입력 : "))
#         if in_num == ran_num:
#             print ("정답입니다.")
#             break 

#         elif in_num > ran_num:
#             print("입력숫자가 큽니다. 작은수 입력하세요.")
#         else:
#             print("입력숫자가 작습니다. 큰수 입력하세요.")

#         print("랜덤숫자, ran_num")
        
# def cal_func(num1,num2):
#     num1 = int(input("숫자입력 : "))
#     num2 = int(input("숫자입력 : "))
#     print("더하기 : ", num1+num2)
#     print("빼기 : ", num1-num2)
#     print("곱하기 : ", num1*num2)
#     print("나누기 : ", num1/num2)

# while True:
#     choice = main_print()
#     if choice == 1:
#         gugudan_func()
#     elif choice == 2:
#         number_func(2)
#     else:
#         cal_func()

# 학생 성적 프로그램 

stu=[

]

c_no=1 
while True:
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*60)
    choice=int(input("원하는 번호를 입력하세요."))
    if choice == 1:
        print() 
        while True: 
            print("[ 학생성적입력 ]")
            no=c_no 
            name=input("학생이름입력 (0 이전페이지로 이동): ")
            if name=="0" : break
            kor=int(input("국어점수 입력:"))
            eng=int(input("영어점수 입력:"))
            math=int(input("수학점수 입력:"))
            total=kor+eng+math
            avg=total/3 
            stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
            c_no+1
            print()
    elif choice ==2:
        print()
        print("[ 학생성적출력 ]")
        print("-"*60)
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
            print()

                        





c_no=1 # 학생번호로 사용 
# while True: # 메인화면출력함수 
#     print("[ 학생성적프로그램 ]") # while 문이 생성될때 tab 키 누르면 들여쓰기 가능 
#     print("-"*60)
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("-"*60)
#     choice=int(input("원하는 번호 입력하세요."))
#     if choice == 1: # 학생성적입력함수 
#         print()
#         while True:
#             print("[ 학생성적입력 ]")
#             print("-"*60)
#             no=c_no
#             name=input("학생이름입력 (0. 이전페이지 이동):")
#             if name=="0": break
#             kor=int(input("국어점수입력:"))
#             eng=int(input("영어점수입력:"))
#             math=int(input("수학점수입력:"))
#             total=kor+eng+math
#             avg=total/3 
#             stu.append(
#                 {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
#             print(name,"학생 성적이 저장되었습니다.")
#             c_no += 1 # 다음번호 1증가 
#             print()
            
#     elif choice == 2: # 학생성적출력함수 
#             print()
#             print("[ 학생성적출력 ]")
#             print("-"*60)
#             print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#             print("-"*60)
#             for s in stu:
#                 print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
#             print() 
