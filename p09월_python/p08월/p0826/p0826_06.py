# 관계 연산자 ==, !=, >, <, >=, <=
# True, False bool 타입으로 변환 
# a = 10
# b = 5
# print(a==b) 
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# 아이디, 패스워드를 입력받아 맞는지 확인
# 아이디 : aaa, 패스워드 : 1111
# id=input("아이디를 입력하세요.")
# pw=input("패스워드를 입력하세요.")
# if(id=="aaa") and (pw=="1111"): # and 는 둘 다 맞아야만 출력 가능 
#     print("로그인이 되었습니다. 메인페이지로 이동합니다")
# else:
#     print("아이디 또는 패스워드가 일치하지 않습니다")

# if(id=="aaa") or (pw=="1111"): # 둘 중 하나만 맞을 경우 출력 가능 
#     print("로그인이 되었습니다. 메인페이지로 이동합니다")
# else:
#     print("아이디 또는 패스워드가 일치하지 않습니다")

# 프로그램 종료
# 대문자 X 또는 소문자 x 를 입력하면 종료 (또는 or와 동일한 의미)
str1 = input("프로그램을 종료하려면 x 또는 X 를 입력하세요.>>")
if(str1=="x") or (str1=="X"):
    print("프로그램이 종료되었습니다.")
else:
    print("프로그램을 계속 실행합니다.")

# # 산술연산자 : +, -, *, /, //, %, **

# money = 123456789 
# #500원 동전 몇 개가 필요한가요? 
# result1=money//500
# print("500원 동전 필요개수 :", result1)

# result2=money//100
# print("100원 동전 필요개수 :", result2)

# money = 12340 
# # 12340원은 500원 동전 몇 개? 340원은 100원 동전 몇 개? 40원 10원 동전 몇 개? 
# # 12340원 500원 동전 : 23, 100원 동전 : 3, 10원 동전 : 4 

# result1=money//500
# num1=money%500
# print(result1,num1)

# result2=num1//100
# num2=num1%100
# print(result2,num2)

# result3=num2//10
# num3=num2%10
# print(result3,num3)

# # 1270원 500원 동전 2개, 10원 동전 2개, 10원 7개 

