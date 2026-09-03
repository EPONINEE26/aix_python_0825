
# print("1. 컴퓨터-1,000,000")
# # print(1+1+1_000_000) - 언더바는 숫자 출력시 사용. 꼼마는 에러 
# print("2. 세탁기-2,000,000")
# print("3. 오디오-500,000")
# choice=int(input("원하는 번호와 개수 입력 (1/3) "))
# 총금액을 출력하시오.

print("1. 컴퓨터-1,000,000")
print("2. 세탁기-2,000,000")
print("3. 오디오 -500,000")
choice=input("원하는 번호와 개수를 입력 (1/3)")


# def production_func(n1,n2,n3):
#     choice2=choice.split("/") # str 타입 
#     if choice2[0]=="1": #문자열 비교 
#         print("컴퓨터")
#         print("구매금액 :", int(choice2[1])*1000000) # 형변환 
#     elif choice2[0]=="2":
#         print("세탁기")
#         print("구매금액 :", int(choice2[1])*2000000)
#     else:
#         print("오디오")
#         print("구매금액 :", int(choice2[1])*500000)



# def production_func(n1,n2,n3):
#     choice2=choice.split("/") # str 타입 
#     choice2[0]=int(choice2[0])
#     choice2[1]=int(choice2[1])
#     choice2[2]=int(choice2[2])
#     if choice2[0]=="1": #문자열 비교 
#         print("컴퓨터")
#         print("구매금액 :", int(choice2[1])*1000000) # 형변환 
#     elif choice2[0]=="2":
#         print("세탁기")
#         print("구매금액 :", int(choice2[1])*2000000)
#     else:
#         print("오디오")
#         print("구매금액 :", int(choice2[1])*500000)

# 함수선언
def cal(choice):
    # 함수로 이동-----------------------------
    # 1/3 1번 3개 구매함.
    # 총구매금액을 출력하시오.
    choice2 = choice.split("/") #str타입 ["1","3"]
    choice2[0] = int(choice2[0])
    choice2[1] = int(choice2[1])
    if choice2[0] == 1: #문자열비교
        print("컴퓨터")
        print("구매금액 : ",choice2[1]*1000000) # 형변환
    elif choice2[0] == 2:
        print("세탁기")
        print("구매금액 : ",choice2[1]*2000000) # 형변환
    else:
        print("오디오")
        print("구매금액 : ",choice2[1]*500000) # 형변환


# 프로그램 시작 -------------------------------------------------
print("1. 컴퓨터-1_000_000원")
print("2. 세탁기-2_000_000원")
print("3. 오디오-500_000원")
choice = input("원하는 번호와 개수 입력(1/3)") #str타입
# 함수호출
cal(choice)



#앞의 숫자에는 10을 곱하고 뒤에 숫자에는 100을 곱해서
#합계를 구하시오,
# 1*10+3*100=310 이런 식으로 출력하시오

# num=input("숫자입력(1/3)")
# num2=num.split("/")
# print(int(num2[0])*10+int(num2[1])*100) # num2=[int(i) for i in num2] 
# num2=[int(i) for i in num2] 

# num=input("숫자입력(1/3)")
# num2=num.split("/")
# num2=[int(i) for i in num2] 
# print(num2)





    
