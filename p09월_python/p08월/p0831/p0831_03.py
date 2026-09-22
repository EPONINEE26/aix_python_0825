# for i, v in enumerate(a_list):
#     print("{}:{}".format(i,v))

# a_list=["딸기", "바나나", "사과"]

# 0: 딸기
# 1: 바나나
# 2: 사과 


# nums = [3, 9, 10, 105, 220, 2, 1]

# for n in nums:
#     # print(n) 이 줄을 지우면 리스트 숫자가 미리 화면에 출력되지 않습니다.
#     n = int(input("숫자 입력: "))
    
#     if n % 2 == 0:
#         print(n, ": 짝수입니다.")
#     else:
#         print(n, ": 홀수입니다.")

# for i in range(1, 10):
#     print(f"[{i}단]", end="\t")

# print()  # 단 이름(제목) 출력이 끝났으니 줄을 한 번 바꿉니다.

# # 수식 변경 없이 들여쓰기와 줄바꿈 위치만 교정했습니다.
# for i in range(2, 10):
#     for j in range(1, 10):
#         print("{}x{}={}".format(j, i, i * j), end="\t")
#     print()

# sum = 0 
# a = int(input("숫자 입력: "))  # 사용자가 5를 입력하면 a는 5가 됩니다.

# 1. 단 이름(제목)들을 가로로 나란히 출력합니다.
# for i in range(a, 10):
#     print(f"[{i}단]", end="\t") 

# print()  # 제목 출력이 끝났으니 줄을 한 번 바꿉니다.

# # 2. b를 지우고 9곱까지 돌도록 range(1, 10)으로 수정 후 가로로 정렬합니다.
# for j in range(1, 10):
#     for i in range(a, 10):
#         print("{}x{}={}".format(i, j, i * j), end="\t")
#     print()  # 한 줄 출력이 끝날 때마다 아래로 줄바꿈

# sum = 0 
# a = int(input("숫자 입력: "))
# b = 9  # 구구단은 9곱까지 하므로 b에 9를 미리 저장해 줍니다!

# for i in range(a, 10):
#     print(f"[{i}단]", end="\t") 

# print()  # 단 이름 출력이 끝나고 줄바꿈

# # 원래 적어주신 for문 구조를 그대로 유지했습니다.
# for i in range(a, 10):
#     for j in range(1, b + 1):  # b가 9이므로 range(1, 10)이 되어 정상 작동합니다.
#         print("{}x{}={}".format(i, j, i * j), end="\t")
    
#     print()  # ★중요★ 한 단이 끝날 때마다 아래로 줄바꿈을 해줍니다.

# sum = 0 
# a = int(input("숫자 입력: "))
# b = 19  # 구구단은 9곱까지 하므로 b에 9를 미리 저장해 줍니다!

# for i in range(a, 10):
#     print(f"[{i}단]", end="\t") 

# print()  # 단 이름 출력이 끝나고 줄바꿈

# # 원래 적어주신 for문 구조를 그대로 유지했습니다.
# for i in range(a, 10):
#     for j in range(1, b + 1):  # b가 9이므로 range(1, 10)이 되어 정상 작동합니다.
#         print("{}x{}={}".format(i, j, i * j), end="\t")
    
#     print()  # ★중요★ 한 단이 끝날 때마다 아래로 줄바꿈을 해줍니다.


# alist=[]
# print(len(alist))
# alist2=[0,0,0] 
# print(len(alist2)) 
# alist3=[0]*10
# print(len(alist3))
# alist4=list(range(10))
# print((alist4))
# # 리스트 늘리는 방법 : 수동으로 입력하던지 * 수식으로 입력하던지 range 범위로 지정하여 입력하던지 할수 있음 
# alist5=[i for i in range(10)] # 리스트 내포 : i에 있는 값을 i 주소값에 넣음
# print((alist5))
# alist6=[i*i for i in range(10)] # 리스트 내포 : 연산을 포함해서 처리하는 방법 파이썬에만 가능 
# print((alist6))
# alist7=[i*3 for i in range(10)] 
# print((alist7))

# for 문 : 정해진 범위가 있을 경우
# while 문 : 조건이 있을 경우 

