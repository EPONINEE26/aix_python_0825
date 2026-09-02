


# imprort random 

# def ran_number(choice): 
#     if choice == 1 :
#         # 랜덤 숫자 5개 
#         random.sample(1, 101, 5)
#     elif choice == 2:     
#         # 랜덤 숫자 3개 
#         random.sample(1, 101, 3) 
#     else:
#         # 랜덤숫자 1개 
#         random.sample(1, 101, 1) 


# # 시작 위치 
# while True:
#     print("1. 랜덤숫자 5개 가져오기")
#     print("2. 랜덤숫자 3개 가져오기")
#     print("3. 랜덤숫자 1개 가져오기")
#     choice = int(input("원하는 번호를 입력하세요.>>"))
#     ran_number(choice) 


# imprort random 

# def ran_number(choice): 
#     if choice == 1 :
#         # 랜덤 숫자 5개 
#         result = random.sample(range(1, 101), 5)
#     elif choice == 2:     
#         # 랜덤 숫자 3개 
#         result = random.sample(range(1, 101),3)
#     else:
#         # 랜덤숫자 1개 
#         result = random.sample(range(1, 101),1) 

# # 시작 위치 
# while True:
#     print("1. 랜덤숫자 5개 가져오기")
#     print("2. 랜덤숫자 3개 가져오기")
#     print("3. 랜덤숫자 1개 가져오기")
#     choice = int(input("원하는 번호를 입력하세요.>>"))
#     ran_number(choice) 
#     result = ran_number (choice)
#     print("결과 값 :", result) 



# 함수사용이유
# 1. 중복되는 코드를 재 사용하기 위해
# 2. 코드를 간결하게 하기 위해 

from func import * # 코드 재 사용 함수 

# 프로그램 시작-------------------------------------->  
while True:
    choice = main_print()
    result = ran_number (choice)
    print("결과 값 :", result) 







