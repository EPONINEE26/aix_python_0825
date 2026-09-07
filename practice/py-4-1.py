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


title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
k_title = ["no", "name", "kor", "eng", "math", "total", "avg"]
stu = []
sno = 1 

stu = []
with open("C:/aaa/test2.txt","r",encoding="utf-8") as f:
    while True:
        line=f.readline()
        if line=="":break
        line=line.sprit()

        print(line, end="\t")
        arr=line.split(",")

        for i,a in enumerate(arr):
            if 5 >= i >=2:
                arr=int(a)
            elif i == 6:
                arr=int(a)
        stu.append({'no':arr[0]}, {'name':arr[1]}, {'kor':arr[2]}, {'eng':arr[3]}, {'math':arr[4]}, {'total':arr[5]}, {'avg':arr[6]})

