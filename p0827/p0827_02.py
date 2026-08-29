# 랜덤함수
import random # 파이썬에 있는 random 클래스를 사용하겠다는 선언

# random.randint(1,100) # 1~100까지 랜덤으로 정수값을 1개 넘겨줌 
# # randint(1,10 or 1,100) 첫번째 입력숫자부터 두번째 입력숫자까지 랜덤으로 정수값을 1개 넘겨줌 
# num=random.randint(1,10)
# print(num)

# 1~5까지의 랜덤 숫자를 출력하시고
# num=random.randint(1,5) # 1~5까지의 랜덤숫자 생성 
# print(num)

# int(input("1~5까지 범위의 숫자를 입력하세요.>>"))
# print("랜덤숫자:",num)
# print("입력숫자:",input)

# num=random.randint(1,5) 
# print(num)

# input1=int(input("1~5까지 범위의 숫자를 입력하세요.>>"))
# print("랜덤숫자:",num)
# print("입력숫자:",input1)
# if (num==input1):
#        print("축하합니다. 당첨되었습니다.")
# else:
#        print("아쉽습니다. 꽝입니다.")


# num=random.randint(1,5)
# input1=int(input("1~5까지 범위의 숫자를 입력하세요.>>")
# input2=int(input("1~5까지 범위의 숫자를 입력하세요.>>")
# print=int(input("랜덤숫자:",num)) 
# print=int(input("입력숫자:", input))
# if (num==input1) or (num==input2):
#     print("당첨!!")
# else:
#     print("꽝!!")

# 비교연산자 ==, !=, <, >, <=, >= 
# 산술연산자 +,-,*, /, //, %, ** 
# 논리연산자 and, or, xor (not)

# 입력한 숫자가 2의 배수인지, 아닌지 출력하시오
# a=int(input("숫자 입력. : "))
# if a%2==0:   # 비교연산자 : ==, !=, <, >, <=, >= 
#     print("2의 배수입니다.")
# else:
#     print("2의 배수가 아닙니다.")
# print("입력숫자:", a)


# 입력한 숫자가 양수인지, 음수인지 출력하시오. 
# 1. 숫자입력 # 2. 양수, 음수 비교 # 3. 출력 

# a=int(input("숫자를 입력하세요. : "))
# if a>0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")
# print("입력숫자: {} " , a)

# a, b를 입력 받아 
# 합계가 100 넘으면 100보다 큰 수, 100 안 넘으면 100보다 작은 수 라고 출력하시오.

# 1. 숫자입력
# 2. 합계
# 3. 조건 

# a=int(input("숫자를 입력하세요."))
# b=int(input("숫자를 입력하세요."))
# total=a+b 

# if total>100: 
#     print("100보다 큰 수")
# else:
#     print("100보다 작은 수") 
# print("입력한 숫자 : ", total)


# a=int(input("숫자를 입력하세요."))
# b=int(input("숫자를 입력하세요."))
# total=a+b 

# if total>100: 
#     print("100보다 큰 수")
# else:
#     print("100보다 작은 수") 
# print("입력숫자:{},{} / 합계:{}".format(a,b,total))
# print(f"입력숫자:{a},{b} / 합계:{total}")  

# a = input("숫자입력 :") 
# print("10"==10) # 문자 10과 숫자 10은 다름 
# a=int(input("숫자입력 :")) # 문자타입 -> 숫자타입 
# if a>100:
#    print("100보다 큰수")
# else:
#    print("100보다 작은수")

# if a>100:
#    print("100보다 큰수")
#    print("입력한 숫자 : ", a)
# else:
#    print("100보다 작은수")
#    print("입력한 숫자 : ", a) 


# if a>100:
#    print("100보다 큰수")
# else:
#    print("100보다 작은수")   
# print("입력한 숫자 : ", a)

   
# a=101
# if a<100:
#     print("100보다 작은수입니다.")

# else:
#     print("100보다 큰수입니다.")
# print("종료")





