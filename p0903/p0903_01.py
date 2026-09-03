# # def 가 있으면 선언 없으면 호출 
# def print_3_times(): # 함수 선언 
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
# print_3_times() # 함수 호출 (실행이 되는 곳 )

# 함수 사용 이유 : 코드 재 사용, 코드 간결 
# C, Java인 경우 컴파일러 언어. 모든 소스를 기계어로 번역 후 프로그램 진행. 소스양이 많음. 웹&앱 개발에서 사용
# 파이썬인 경우 스크립트 언어. 한 줄씩 기계어로 번역 후 프로그램 진행. 소스양이 적음. 사용하기 최적화되어져 있기에 많이 사용

# def d_print():
#     for i in range(1,11):
#         print(i)


# # 프로그램 시작 ----------------------> 
# d_print()
# # 함수 호출하는 곳에서 함수 선언까지 가려면 변수로 입력. 함수 선언에서 함수 호출로 가려면 return 
# 스크립터 언어이기에 실행하는 프로그램 서식은 무조건 실행할 프로그램 위에 있어야함. 

# def hello_print():
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
# hello_print()

# def cal(n1, n2):
#     print("{}+{}={}".format(n1,n2,n1+n2))
#     print("{}+{}={}".format(n1,n2,n1-n2))
#     print("{}+{}={}".format(n1,n2,n1*n2))
#     print("{}+{}={}".format(n1,n2,n1/n2))

# n1=int(input("숫자입력:"))
# n2=int(input("숫자입력:"))
# cal(n1,n2)

# def cal(n1, n2):

# num1=int(input("숫자입력:"))
# num2=int(input("숫자입력:"))
# cal(num1,num2)

# def cal(n1, n2): #shift+alt+방향키, alt+방향키 
#     r1=n1+n2
#     r2=n1-n2
#     r3=n1*n2
#     r4=n1/n2
#     return r1,r2,r3,r4 

# n1=int(input("숫자입력:"))
# n2=int(input("숫자입력:"))

# r1,r2,r3,r4=cal(n1,n2)
# print("{}+{}={}".format(n1,n2,n1+n2))
# print("{}+{}={}".format(n1,n2,n1-n2))
# print("{}+{}={}".format(n1,n2,n1*n2))
# print("{}+{}={}".format(n1,n2,n1/n2))
# print(r1,r2,r3,r4)





