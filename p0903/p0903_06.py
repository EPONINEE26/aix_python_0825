# s_arr = [
#     {"prd_name":"컴퓨터","price":1000000},
#     {"prd_name":"냉장고","price":2000000},
#     {"prd_name":"오디오","price":500000},
#     {"prd_name":"세탁기","price":1500000}
#     ] # 1-0,2-1,3-2

# print("1.컴퓨터")
# print("2.냉장고")
# print("3.오디오")
# print("4.세탁기")

# for i,v in enumerate(s_arr): # 0,{"prd_name":"컴퓨터","price":1000000}
#     print(f"{i+1}.{v['prd_name']} : {v['price']:,} 원")

# choice = int(input("원하는 번호입력 : "))
# if choice == 1:
#     print("컴퓨터")
# elif choice == 2:
#     print("냉장고")
# elif choice == 3:
#     print("오디오")
# elif choice == 4:
#     print("세탁기")


# 1. 초기 데이터 설정 (bonusPoint 추가)
my_info = {"id":"aaa","pw":"1111","name":"홍길동","money":10000000, "bonusPoint":0}

# 2. 상품 리스트 (키 이름을 p_name, bonusPoint로 통일하여 매칭)
s_arr = [
    {"p_name":"컴퓨터","price":1000000, "bonusPoint":10000},
    {"p_name":"냉장고","price":2000000, "bonusPoint":20000},
    {"p_name":"오디오","price":500000, "bonusPoint":5000},
    {"p_name":"세탁기","price":1500000, "bonusPoint":15000}
]

# 상단 출력 부분
print("1.컴퓨터")
print("2.냉장고")
print("3.오디오")
print("4.세탁기")

for i,v in enumerate(s_arr):
    print(f"{i+1}.{v['p_name']} : {v['price']:,} 원")

print(f"현재 보유금액 : {my_info['money']:,}원")
print(f"현재 보너스포인트 : {my_info['bonusPoint']:,}포인트")
print("-"*40)

def p_cal(choice):
    print(f"구매상품 : {s_arr[choice-1]['p_name']}")
    print(f"가격 : {s_arr[choice-1]['price']:,} 원")

    my_info['money'] -= s_arr[choice-1]['price']
    print(f"상품구매후 보유금액 : {my_info['money']:,}원")

    return choice

# 에러 원인이던 무조건 실행되는 외곽 if문은 제거하거나 
# 아래와 같이 초기 choice 값을 임의로 지정해야 에러가 나지 않습니다.
choice = 1 
if choice == 1:
    # 아래 while문과 동일하게 처리되도록 수정
    no = int(input(f"{s_arr[choice-1]['p_name'] }를 구매하시겠습니까?(구매:1,취소:0) "))
    if no == 1:
        print(f"{s_arr[choice-1]['p_name'] } 구매완료")
        my_info['money'] -= s_arr[choice-1]['price']
        my_info['bonusPoint'] += s_arr[choice-1]['bonusPoint']
        print(f"m머니 : {my_info['money']:,}원")
        print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")

# 반복 쇼핑몰 루프
while True:
    print()
    print("[ 쇼핑몰 구매사이트 ]")
    for i,p in enumerate(s_arr):
        print(f"{i+1}. {p['p_name']} : {p['price']:,}원")
    print("9. 구매상품리스트")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        no = int(input(f"{s_arr[choice-1]['p_name'] }를 구매하시겠습니까?(구매:1,취소:0) "))
        if no == 1:
            print(f"{s_arr[choice-1]['p_name'] } 구매완료")
            my_info['money'] -= s_arr[choice-1]['price']
            my_info['bonusPoint'] += s_arr[choice-1]['bonusPoint']
            print(f"m머니 : {my_info['money']:,}원")
            print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
    else:
        pass

