# def str_print(n,*v): # 매개 변수 2개  뒤애 별표가 있는 것은 가변매개변수 
#     for i in range(n): 
#         for j in v:
#             print(j, end="\t")
#         print() # 줄바꿈과 동일한 기능 가로로 출력 

# str_print(3,"안녕","반가워","잘있어") # 개수는 꼭 맞춰야함. # *를 입력할 경우 개수 만큼 늘려서 입력 받겠다는 의미 n범위 내에 들어가는 변수는 문자로는 안 되고 숫자로만 가능 


# def str_print(n,*v): # 매개 변수 2개  뒤애 별표가 있는 것은 가변매개변수 
#     for i in range(n): 
#         for j in v:
#             print(j, end="\t")
#             print() # 세로로 출력 

# str_print(3,"안녕","반가워","잘있어")

# print(1,2,3,4,5) # function 함수라는 의미 
# print(1,2,3,4,5, sep="/") # 입력된 모양으로 출력

# arr=["번호","이름","국어","영어"]
# print(*arr, sep="\t")

# def str_print(*v,n): 
#     print(n)
# str_print(1,2,3,4,5, "안녕") # 이렇게 실행하면 에러난다. 그 이유는 n 변수에 들어갈 값이 없다고 컴퓨터가 인지 

# def str_print(n, *v): 
#     print(n, v)
# str_print("안녕", 1,2,3,4,5) # 안녕에 n 자리에 들어감 

# 가변매개변수는 맨 뒤쪽에 배치
# 키워드매개변수는 맨 뒤쪽에 배치 
# 둘 다 사용할 경우 가변매개변수가 앞에 오고 키워드매개변수가 뒤에 온다 
# def str_print(*v,n): 
#     print(v, n)
# str_print(1,2,3,4,5, n="안녕") # 키워드매개변수 가변매개변수 뒤에 그냥 일반 매개변수값은 오면 안 되고 무조건 키워드매개변수로 지정해야함

# def cal (s1=1, e1=50, s2=10): #초기화매개변수 
#     print(s1,e1,s2)
# cal(0) # cal 값에 0을 입력하면 s1값이 0으로 변경해서 출력됨
# cal() # cal 값에 아무런 정보를 입력하지 않을 경우 처음 입력된 값이 출력됨 
# cal(100,1,2)

# 가변매개변수가 오지 않는 한 키워드매개변수는 사용하지 않음 
# 변수의 종류 : 일반매개변수, 가변매개변수, 초기화매개변수, 키워드매개변수 


# my_info = {"id":"aaa","pw":"1111",\
#             "money":10_000_000,\
#             "bonusPoint":0}
# cart = []

# while True:
#     print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")

#     if my_info["id"] == id and my_info["pw"]==pw:
#         print("로그인이 되었습니다.")
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다.")

# my_info = {"id":"aaa","pw":"1111",\
#             "money":10_000_000,\
#             "bonusPoint":0}
# cart = []

# while True:
#     print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")

#     if my_info["id"] == id and my_info["pw"]==pw:
#         print("로그인이 되었습니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다.")

# while True:
#     print("[ 쇼핑몰 구매사이트 ]")
#     print("1. 컴퓨터-1000000")
#     print("2. 냉장고-2000000")
#     print("3. 오디오-500000")
#     print("-"*30)
#     choice = int(input("원하는 번호를 입력하세요.>> "))

# my_info = {"id":"aaa","pw":"1111",\
#             "money":10_000_000,\
#             "bonusPoint":0}
# cart = []
# product = [
#     {"p_name": "컴퓨터", "price": "1000000", "bonusePoint" : "1000000*0.1"},
#     {"p_name": "냉장고", "price": "2000000", "bonusePoint" : "2000000*0.1"},
#     {"p_name": "오디오", "price": "500000", "bonusePoint" : "500000*0.1"},

# ]

# while True:
#     print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")

#     if my_info["id"] == id and my_info["pw"]==pw:
#         print("로그인이 되었습니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다.")

# while True:
#     print("[ 쇼핑몰 구매사이트 ]")
#     print("1. 컴퓨터-1000000")
#     print("2. 냉장고-2000000")
#     print("3. 오디오-500000")
#     print("-"*30)
#     choice = int(input("원하는 번호를 입력하세요.>> "))

#     if choice == 1:
#         no=int(input("컴퓨터를 구매하시겠습니까? (구매:1, 취소:2)")) 
#         if no == 1:
#             print("구매완료")

#         else:
#             print("이전화면으로 이동합니다.")

# cart 에 넣으려먼 상품명과 가격이 있어야 하고 금액의 10% 를 보너스를 넣는 방법 
# money 항목에 돈이 있기에 money 항목에서 상품 금액만큼 제하여야함 



# my_info = {"id":"aaa","pw":"1111",\
#             "money":10_000_000,\
#             "bonusPoint":0}
# cart = []

# product = [
#     {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
#     {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
#     {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
# ]

# while True:
#     print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")

#     if my_info["id"] == id and my_info["pw"]==pw:
#         print("로그인이 되었습니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다.")

# while True:
#     print("[ 쇼핑몰 구매사이트 ]")
#     print("1. 컴퓨터-1,000,000")
#     print("2. 냉장고-2,000,000")
#     print("3. 오디오-500,000")

#     for i,p in enumerate(product):
#         print(f"{i+1}. {p['p_name']} : {p['price']:,} 원")


#     print("-"*30)
#     choice = int(input("원하는 번호를 입력하세요.>> "))

#     if choice == 1:
#         no = int(input("컴퓨터를 구매하시겠습니까?(구매:1,취소:0)"))
#         if no == 1:
#             print("구매완료")
#         else:
#             print("이전화면으로 이동합니다.")


# my_info = {"id":"aaa","pw":"1111",\
#             "money":10_000_000,\
#             "bonusPoint":0}
# cart = []

# product = [
#     {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
#     {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
#     {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
# ]

# while True:
#     print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")

#     if my_info["id"] == id and my_info["pw"]==pw:
#         print("로그인이 되었습니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다.")

# print("현재 보유금액 : ", my_info['money'])
# print("현재 보너스금액 : ", my_info['bonusPoint'])
# print("-"*40 )

# while True:
#     print()
#     print("[ 쇼핑몰 구매사이트 ]")
#     for i,p in enumerate(product):
#         print(f"{i+1}. {p['p_name']} : {p['price']:,} 원")


#     print("-"*30)
#     choice = int(input("원하는 번호를 입력하세요.>> "))
#     print()

#     if choice == 1:
#         no = int(input("컴퓨터를 구매하시겠습니까?(구매:1,취소:0) "))
#         if no == 1:
#             print("구매완료")
#             # ---------------계산 ---------------------
#             print("p가격 : ", product[choice - 1]['price']) # product(product[0]['price'])
#             print("p보너스포인트 : ", product[0]['bonusPoint'])

#             #계산 후 결과 
#             my_info['money'] += product[0]['price']
#             my_info['money'] = my_info['money'] - product[0]['price']

#             my_info['bonusPoint'] += product[0]['bonusPoint']
#             my_info['money'] = my_info['money'] - product[0]['bonusPoint']

#             print("m머니 : ", my_info['money'])
#             print("m보너스포인트 : ", my_info['bonusPoint'])
            
#         else:
#             print("이전화면으로 이동합니다.")

# 변수 선언부분
# 개인정보
my_info = {"id":"aaa","pw":"1111",\
            "money":10_000_000,"bonusPoint":0}
# 구매리스트
cart = []
# 상품
product = [
    {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
    {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
    {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
]

# 아이디,패스워드 확인
while True:
    print("[ 쇼핑몰에 오신것을 환영합니다. ]")
    id = input("아이디 : ")
    pw = input("패스워드 : ")

    if my_info["id"] == id and my_info["pw"]==pw:
        print("로그인이 되었습니다.")
        break
    else:
        print("아이디 또는 패스워드가 일치하지 않습니다.")

# my금액,보너스포인트
print(f"현재 보유금액 : {my_info['money']:,}원")
print(f"현재 보너스포인트 : {my_info['bonusPoint']:,}포인트")
print("-"*40)
# 구매정보
while True:
    print()
    # 상품출력부분
    print("[ 쇼핑몰 구매사이트 ]")
    for i,p in enumerate(product):
        print(f"{i+1}. {p['p_name']} : {p['price']:,}원")
    print("9. 구매상품리스트")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    # 1.컴퓨터구매부분
    if choice == 1:
        no = int(input("컴퓨터를 구매하시겠습니까?(구매:1,취소:0) "))
        if no == 1:
            print("컴퓨터 구매완료")
            # 계산후 결과
            my_info['money'] -= product[0]['price']
            # my_info['money'] = my_info['money'] - product[0]['price']

            my_info['bonusPoint'] += product[0]['bonusPoint']
            print(f"m머니 : {my_info['money']:,}원")
            print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
        else:
            print("이전화면으로 이동합니다.")
    elif choice == 2:
        no = int(input("냉장고를 구매하시겠습니까?(구매:1,취소:0) "))
        if no == 1:
                print("냉장고 구매완료")
                # 계산후 결과
                my_info['money'] -= product[1]['price']
                # my_info['money'] = my_info['money'] - product[1]['price']
    
                my_info['bonusPoint'] += product[1]['bonusPoint']
                print(f"m머니 : {my_info['money']:,}원")
                print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
        else:
                print("이전화면으로 이동합니다.")
    elif choice == 3:
            no = int(input("오디오를 구매하시겠습니까?(구매:1,취소:0) "))
            if no == 1:
                print("오디오 구매완료")
                # 계산후 결과
                my_info['money'] -= product[2]['price']
                # my_info['money'] = my_info['money'] - product[2]['price']
    
                my_info['bonusPoint'] += product[2]['bonusPoint']
                print(f"m머니 : {my_info['money']:,}원")
                print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
            else:
                print("이전화면으로 이동합니다.")






