# my_info={"id":"aaa", "pw":"1111", "name":"홍길동", "money":10000000, "bonusPoint":0}

# while True:
#         print("[ 쇼핑몰에 오신것을 환영합니다. ]")
#         id = input("아이디 : ")
#         pw = input("패스워드 : ")

#         if my_info["id"] == id and my_info["pw"]==pw:
#                 print("로그인이 되었습니다.") 
#         else:
#                 print("아이디 또는 패스워드가 일치하지 않습니다.")

#         while True: 
#                 cart = []
#                 s_arr  = [ 
#                         {"p_name": "컴퓨터", "price": 1000000},
#                         {"p_name": "냉장고", "price": 2000000},
#                         {"p_name": "오디오", "price": 500000},
#                         {"p_name": "세탁기", "price": 1500000}
#                 ]

#                 print("1. 컴퓨터")
#                 print("2. 냉장고")
#                 print("3. 오디오")
#                 print("4. 세탁기") 
                

#                 for i,v in enumerate(s_arr): 
#                         print(f"{i+1}.{v['p_name']}:{v['price']:,}원")
#                         choice=int(input("원하는 번호를 입력하세요.>>"))


my_info = {"id": "aaa", "pw": "1111", "name": "홍길동", "money": 10000000, "bonusPoint": 0}

while True:
        print("[ 쇼핑몰에 오신것을 환영합니다. ]")
        id = input("아이디 : ")
        pw = input("패스워드 : ")

        if my_info["id"] == id and my_info["pw"] == pw:
                print("로그인이 되었습니다.") 
                break 
        else:
                print("아이디 또는 패스워드가 일치하지 않습니다.")

cart = []
s_arr = [ 
        {"p_name": "컴퓨터", "price": 1000000, "bonusPoint": 10000},
        {"p_name": "냉장고", "price": 2000000, "bonusPoint": 20000},
        {"p_name": "오디오", "price": 500000, "bonusPoint": 5000},
        {"p_name": "세탁기", "price": 1500000, "bonusPoint": 15000}
]

while True: 
        print("[ 쇼핑몰 구매사이트 ]")
    
        for i, v in enumerate(s_arr): 
                print(f"{i+1}.{v['p_name']}:{v['price']:,}원")
        
    # 1. 사용자가 번호(1~4)를 입력합니다.
        choice = int(input("원하는 번호를 입력하세요.>>"))
    
    # 2. 💡 [핵심] choice = 1 고정 코드를 지우고, 입력받은 choice 번호가 1~4 사이인지 확인합니다.
        if 1 <= choice <= 4:
        # 사용자가 선택한 상품의 정보를 s_arr에서 가져옵니다 (인덱스는 choice - 1)
        selected_item = s_arr[choice - 1]
        
        # 3. 💡 고정된 '컴퓨터' 글자 대신 선택한 상품 이름이 동적으로 나오도록 수정합니다.
        no = int(input(f"{selected_item['p_name']}를 구매하시겠습니까? (구매:1, 취소:0)>> "))
        
        if no == 1:
        print(f"{selected_item['p_name']} 구매완료")
        my_info['money'] -= selected_item['price']
        my_info['bonusPoint'] += selected_item['bonusPoint']
        print(f"m머니 : {my_info['money']:,}원")
        print(f"m보너스포인트 : {my_info['bonusPoint']:,}원")
        break # 구매가 완료되면 멈추도록 설정 (계속 쇼핑하려면 제거 가능)


        print(f"현재 보유금액: {my_info['money']:,}원")
        print(f"현재 보너스금액 : {my_info['bonusPoint']:,}원")
        print("-"*40) 

        def p_cal(choice):
                print(f"구매상품 : {s_arr[choice-1]['p_name']}")
                print(f"구매가격 : {s_arr[choice-1]['price']:,원}")

                my_info['money'] -= s_arr[choice-1]['price']
                print(f"상품구매 후 보우금액 : {my_info['money']:,원}")
                return choice 

        choice=1
        if choice==1:
                no=int(input(f"{s_arr[choice-1]['p_name']} 를 구매하시겠습니까? (구매:1, 취소:0)"))
                if no==1:
                        print(f"{s_arr[choice-1]['p_name']} 컴퓨터 구매완료")
                my_info['money'] -= s_arr[choice-1]['price']
                my_info['bonusPoint'] += s_arr[choice-1]['bonusPoint']
                print(f"m머니 : {my_info['money']:,}원")
                print(f"m보너스포인트 : {my_info['bonusPoint']:,}원")
        if choice==2:
                no=int(input(f"{s_arr[choice-1]['p_name']} 를 구매하시겠습니까? (구매:1, 취소:0)"))
                if no==2:
                        print(f"{s_arr[choice-1]['p_name']} 컴퓨터 구매완료")
                my_info['money'] -= s_arr[choice-1]['price']
                my_info['bonusPoint'] += s_arr[choice-1]['bonusPoint']
                print(f"m머니 : {my_info['money']:,원}")
                print(f"m보너스포인트 : {my_info['bonusPoint']:,}원")

        if choice==3:
                no=int(input(f"{s_arr[choice-1]['p_name']} 를 구매하시겠습니까? (구매:1, 취소:0)"))
                if no==3:
                        print(f"{s_arr[choice-1]['p_name']} 컴퓨터 구매완료")
                my_info['money'] -= s_arr[choice-1]['price']
                my_info['bonusPoint'] += s_arr[choice-1]['bonusPoint']
                print(f"m머니 : {my_info['money']:,원}")
                print(f"m보너스포인트 : {my_info['bonusPoint']:,}원")

        if choice==4:
                no=int(input(f"{s_arr[choice-1]['p_name']} 를 구매하시겠습니까? (구매:1, 취소:0)"))
                if no==4:
                        print(f"{s_arr[choice-1]['p_name']} 컴퓨터 구매완료")
                my_info['money'] -= s_arr[choice-1]['price']
                my_info['bonusPoint'] += s_arr[choice-1]['bonusPoint']
                print(f"m머니 : {my_info['money']:,}원")
                print(f"m보너스포인트 : {my_info['bonusPoint']:,}원")


# title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
# k_title = ["no", "name", "kor", "eng", "math", "합계", "평균"]
# stu = []
# sno = 1 

# def s_mainPoint():
#     print("[ 학생성적프로그램 ]")
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("3. 학생성적수정")
#     print("-"*60)
#     choice=int(input("원하는 번호를 입력하세요. >>"))
#     print()
#     return choice 

# def s_input():  
#     global sno
#     while True:
#         no = sno
#         name=input("이름을 입력하세요. (0. 이전페이지로 이동합니다)")
#         if name == "0":break
#         kor = int(input("국어점수 입력 : "))
#         eng = int(input("영어점수 입력 : "))
#         math = int(input("수학점수 입력 : "))
#         total = kor+eng+math
#         avg = total / 3

#         stu.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg})
#         print(f"{name} 학생성적이 저장되었습니다.") 
#         print()
#         sno+=1 
#         s_output()

# def s_output(): 
#     print()
#     print("[ 학생성적출력 ]")
#     print("-"*60)
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
#     print("-"*60)
#     for s in stu:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
#     print()


# def s_update():
#     print("[ 학생성적수정 ]")
#     print("-"*60)
#     name = input("찾을려는 학생이름 입력 : ")
#     temp = 0
#     for i,s in enumerate(stu):
#         if s['name']==name:
#             print(f"{name} 학생을 찾았습니다.")
#             temp = 1
#             break 
#     if temp == 0:
#             print(f"{name} 학생은 없습니다.")
#     elif temp ==1:
#         print("[ 과목수정선택 ]")
#     print("1. 국어    2.영어    3.수학")
#     choice = int(input("원하는 번호를 입력하세요.>>"))
#     if choice == 1:
#                 s['kor'] = int(input("변경하려는 국어점수 입력 : "))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3 
#                 print(f"{s['kor']} 점수가 변경되었습니다.")
#     elif choice == 2:
#                 s['eng'] = int(input("변경하려는 영어점수 입력 : "))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3 
#                 print(f"{s['eng']} 점수가 변경되었습니다.")
#     elif choice == 3:
#                 s['math'] = int(input("변경하려는 수학어점수 입력 : "))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3 
#                 print(f"{s['math']} 점수가 변경되었습니다.")

    
# while True:
#     choice = s_mainPoint() 
#     if choice == 1: 
#         s_input()
#         s_output()
#     elif choice == 2: 
#         s_output()
#     elif choice == 3: 
#         s_update() 
#         s_output()


# title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
# k_title = ["no", "name", "kor", "eng", "math", "합계", "평균"]
# stu = []
# sno = 1 

# def s_mainPoint():
#     print("[ 학생성적프로그램 ]")
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("3. 학생성적수정")
#     print("-"*60)
#     choice=int(input("원하는 번호를 입력하세요. >>"))
#     print()
#     return choice 

# def s_input():  
#     global sno
#     while True:
#         no = sno
#         name=input("이름을 입력하세요. (0. 이전페이지로 이동합니다)")
#         if name == "0":break
#         kor = int(input("국어점수 입력 : "))
#         eng = int(input("영어점수 입력 : "))
#         math = int(input("수학점수 입력 : "))
#         total = kor+eng+math
#         avg = total / 3

#         stu.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg})
#         print(f"{name} 학생성적이 저장되었습니다.") 
#         print()
#         sno+=1 
#         s_output()

# def s_output(): 
#     print()
#     print("[ 학생성적출력 ]")
#     print("-"*60)
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
#     print("-"*60)
#     for s in stu:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
#     print()


# def s_update():
#     print("[ 학생성적수정 ]")
#     print("-"*60)
#     name = input("찾을려는 학생이름 입력 : ")
#     temp = 0
#     for i,s in enumerate(stu):
#         if s['name']==name:
#             print(f"{name} 학생을 찾았습니다.")
#             temp = 1
#             break 
#     if temp == 0:
#             print(f"{name} 학생은 없습니다.")
#     elif temp ==1:
#         print("[ 과목수정선택 ]")
#     print("1. 국어    2.영어    3.수학")
#     choice = int(input("원하는 번호를 입력하세요.>>"))
#     if choice == 1:
#                 s[k_title[choice+1]] = int(input("f"변경하려는 {title[choice+1]}))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3 
#                 print(f"{s['kor']} 점수가 변경되었습니다.")
#     elif choice == 2:
#                 s[k_title[choice+2]] = int(input("f"변경하려는 {title[choice+2]}))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3 
#                 print(f"{s['eng']} 점수가 변경되었습니다.")
#     elif choice == 3:
#                 s[k_title[choice+3]] = int(input("f"변경하려는 {title[choice+3]}))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total']/3 
#                 print(f"{s['math']} 점수가 변경되었습니다.")

    
# while True:
#     choice = s_mainPoint() 
#     if choice == 1: 
#         s_input()
#         s_output()
#     elif choice == 2: 
#         s_output()
#     elif choice == 3: 
#         s_update() 
#         s_output()


