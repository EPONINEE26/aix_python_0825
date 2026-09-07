# my_info = {"id": "aaa", "pw": "1111", "money": 10_000_000, "bonusPoint": 0}

# cart = []
# # 상품 목록 (4번 세탁기 포함)
# product = [  
#     {"p_name": "컴퓨터", "price": 1000000, "bonusPoint": 1000000 * 0.1},
#     {"p_name": "냉장고", "price": 2000000, "bonusPoint": 2000000 * 0.1},
#     {"p_name": "오디오", "price": 500000, "bonusPoint": 500000 * 0.1},
#     {"p_name": "세탁기", "price": 1500000, "bonusPoint": 1500000 * 0.1},
# ]




# def cal1(choice):
#     # 1. 잔액이 부족한지 가장 먼저 확인합니다!
#     if my_info['money'] < product[choice-1]['price']:
#         print("보유금액이 부족합니다. 머니충전을 한후 구매하세요.")
#         return  # 잔액이 부족하면 함수를 여기서 바로 종료하고 이전 화면으로 돌아갑니다.

#     # 2. 잔액이 충분하다면 기존 구매 진행
#     no = int(input(f"{product[choice-1]['p_name']}를 구매하시겠습니까? (구매 : 1, 취소 : 0) "))
#     if no == 1:
#         print(f"{product[choice-1]['p_name']} 구매완료")
#         my_info['money'] -= product[choice-1]['price']
#         my_info['bonusPoint'] += product[choice-1]['bonusPoint']
#         print(f"m머니 : {my_info['money']:,}원")
#         print(f"보너스포인트 : {my_info['bonusPoint']:,}포인트")
#     else: 
#         print("이전화면으로 이동합니다.")

# while True:
#     print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")
    
#     if my_info["id"] == id and my_info["pw"] == pw:
#         print("로그인이 되었습니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다.")   

# print(f"상품구매후 보유금액 : {my_info['money']:,}원")
# print(f"현재 총 보너스포인트 : {my_info['bonusPoint']:,}포인트")
# print("-" * 40)

# while True:
#     print()
#     # 상품출력부분 (보너스포인트 정보 함께 표시)
#     print("[ 쇼핑몰 구매사이트 ]")
#     for i, p in enumerate(product):
#         print(f"{i+1}. {p['p_name']} : {p['price']:,}원 (적립 포인트: {int(p['bonusPoint']):,}포인트)")
#     print("9. 구매상품리스트")
#     print("-" * 30)
#     choice = int(input("원하는 번호를 입력하세요.>> "))
#     print()

#     # 상품 구매 및 리스트 출력 부분
#     if choice == 1:
#         cal1(choice)    
#     elif choice == 2:
#         cal1(choice)
#     elif choice == 3:
#         cal1(choice)
#     elif choice == 4:
#         cal1(choice)
#     elif choice == 9:
#         print("[ 구매 상품 리스트 ]")
#         if not cart:
#             print("구매한 상품이 없습니다.")
#         else:
#             for item in cart:
#                 print(f"- {item['p_name']} ({item['price']:,}원)")
#         print(f"현재 보유 포인트: {my_info['bonusPoint']:,}포인트")

#-----------------------------------------------------------------------

# my_info = {"id":"aaa","pw":"1111",\
#         "money":10_000_000,"bonusPoint":0}
# # 구매리스트
# cart = []
# # 상품
# product = [  
#     {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
#     {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
#     {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
#     {"p_name": "세탁기", "price": 1500000, "bonusPoint": 1500000 * 0.1},
# ]

# def cal1(choice):
#     no = int(input(f"{product[choice-1]['p_name'] }를 구매하시겠습니까?(구매:1,취소:0) "))
#     if no == 1:
#         print(f"{product[choice-1]['p_name'] } 구매완료")
#         # 계산후 결과
#         my_info['money'] -= product[choice-1]['price']
#         # my_info['money'] = my_info['money'] - product[0]['price']

#         my_info['bonusPoint'] += product[choice-1]['bonusPoint']
#         print(f"m머니 : {my_info['money']:,}원")
#         print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
#     else:
#         print("이전화면으로 이동합니다.") 

# # 아이디,패스워드 확인
# while True:
#     print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")
    
#     if my_info["id"] == id and my_info["pw"]==pw:
#         print("로그인이 되었습니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다.")    

# # my금액,보너스포인트
# print(f"현재 보유금액 : {my_info['money']:,}원")
# print(f"현재 보너스포인트 : {my_info['bonusPoint']:,}포인트")
# print("-"*40)
# # 구매정보
# while True:
#     print()
#     # 상품출력부분
#     print("[ 쇼핑몰 구매사이트 ]")
#     for i,p in enumerate(product):
#         print(f"{i+1}. {p['p_name']} : {p['price']:,}원")
#     print("9. 구매상품리스트")
#     print("-"*30)
#     choice = int(input("원하는 번호를 입력하세요.>> "))
#     print()


#     # 1.컴퓨터구매부분
#     if choice == 1:
#         cal1(choice)    
#     elif choice == 2:
#         cal1(choice)
#     elif choice == 3:
#         cal1(choice)
#     elif choice == 4:
#         cal1(choice)


#------------------------------------------------------------------------------------------


# import random

# ran_num = random.randint(1, 10)
# in_arr = []

# in_arr.append(0)

# for i in range(5):
#     no = int(input("1~100 사이 숫자 입력 : "))
#     in_arr.append(no) 

# answer_arr = []

# for i in in_arr:
#     if i == ran_num:
#         answer_arr.append(i)
#         print(f"입력한 숫자 {i}: 당첨입니다!")
#     else:
#         print(f"입력한 숫자 {i}: 꽝입니다. (정답은 {ran_num})")

# print("-" * 30)
# print("정답번호 :", ran_num)
# print("입력번호 :", in_arr)
# print("정답개수 :", len(answer_arr))
# print("정답숫자 :", answer_arr)

# import random

# # 랜덤 숫자 3개 생성
# arr2 = random.sample(range(1, 101), 3)

# answer_arr = []

# # 5번 반복하도록 들여쓰기 수정
# for i in range(5):
#     input1 = int(input("숫자입력 : "))
    
#     if input1 in arr2:
#         print("당첨")
#         # 맞춘 숫자를 정답 리스트에 추가합니다.
#         answer_arr.append(input1)
#     else:
#         print("꽝")

# print("-" * 30)
# print("랜덤숫자 :", arr2)
# print("입력숫자 :", input1)    
# # len()을 이용해 정답 개수(숫자)를 출력합니다.
# print("정답개수 :", len(answer_arr))
# print("정답번호 :", answer_arr)


# import random

# a_arr = list(range(1, 26))
# random.shuffle(a_arr)

# while True:
#     print(" "*15, end="")
#     print("[ 빙고게임 ]")
#     print("-" * 50)
#     for i, v in enumerate(a_arr):
#         if (i + 1) % 5 != 0:
#             print(v, end="\t")
#         else:
#             print(v)    
#     print("-" * 50)
    
#     num = int(input("원하는 번호를 입력하세요.>> "))
#     if num in a_arr:
#         idx = a_arr.index(num)
#         a_arr[idx] = "X"


-------------------------------------------------------------------------------------------------------

title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", ]
k_title = ["no", "name", "kor", "eng", "math", "total", "avg"]
stu=[]
sno=1 

stu = []

with open("C:/aaa/test1.txt","r",encoding="utf-8") as f:
    while True:
        line = f.readline() # /n 줄바꿈때문에 에러가 남.
        if line=="": break
        line = line.strip()

        print(line,end="")
        arr = line.split(",")

        for i,a in enumerate(arr):
            if 5>=i>=2:
                arr[i] = int(a)
            elif i==6:
                arr[i] = float(a)    
        # stu 리스트에 저장
        # print(arr)
        stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})

def s_mainPrint():
    print("{ 학생성적프로그램 }")
    print("1. 학생성적입력")
    print("1. 학생성적출력")
    print("1. 학생성적수정")
    print("-"*60) 
    choice = int(input("원하는 번호를 입력하세요. >>"))
    print()
    return choice 

def s_input():
    global sno
    while True:
        no = sno 
        print("[ 학생성적입력 ]")
        name = input (f"{no} 번째 이름 입력 (0. 이전화면 이동) : ")
        if name == "0" : break
        kor = int(input("국어점수 입력 : "))
        eng = int(input("영어점수 입력 : "))
        math = int(input("수학점수 입력 : "))
        total = kor+eng+math
        avg = total /3 

        stu.append({'no' : no, 'name' : name, 'kor' : kor, 'eng' : eng, 'math' : math, 'total' : total, 'avg' : avg,})
        print(f"{name} 학생성적이 저장되었습니다.")
        print()

        sno += 1
        s_output() 

def s_output():
    print()
    print({"[ 학생성적출력 ]"})
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    if len(stu) == 0:
        print("*** 학생 데이터가 없습니다.")
    else:
        for s in stu:
            print(f"{s['no']},{s['name']}, {s['kor']}, {s['eng']}, {s['math']}, {s['total']}, {s['avg']:.2f}")
        
    print()

def ss_update():
    print()
    print("[ 학생성적수정 ]")
    name = input ("찾을려는 학생이름을 입력하세요. >> ")
    temp = 0 
    for i,s in enumerate(stu):
        if s['name'] == name:
            print(f"{name} 학생을 찾았습니다.")
            temp = 1
            break 

    if temp == 0:
        print(f"{name} 학생이 없습니다.")

    elif temp == 1:
        print("[ 과목수정선택 ]")
        print("1. 국어    2. 영어    3.수학")
        choice = int(input("원하는 번호 입력 : "))

        print(f"현재{title[choice+1]}점수 : {s[k_title[choice+1]]}")
        s[k_title[choice+1]] = int(input(f"변경하려는 {title[choice+1]} 점수 : "))
        s[total] = s['kor']+s['eng']+['math']
        s[avg] = s[total] / 3 
        print(f"{s[k_title[choice+1]]} 점으로 {title[choice+1]} 점수가 변경되었습니다.")

while True:
    choice = s_mainPrint()
    if choice -- 1: 
        s_input()
    elif choice == 2:
        s_output()
    elif choice ==3:
        s_update()



with open("C:/aaa/text2.txt","a+",encoding="utf-8") as f:
    while True:
        line = input("글을 입력하세요. >> ")
        if line !="":
            f.writelines(line+"\n")  #\r:문장끝으로, \n:줄바꿈
        else:
            break

print("파일이 저장되었습니다.")



