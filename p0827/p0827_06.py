# 확인 작업 
# 원하는 값 in 리스트, 원하는 값 not in 리스트 

# arr = [1,3.,5,7,9]
# if 7 in arr:
#     print("원하는 수가 있습니다.")
# else:
#     print("원하는 수가 없습니다.")

# 리스트 순차 정렬 (sort), 역순정렬 sort(reverse=True)
# arr = [1,15,8,23,2]
# arr.sort() # 순차 정렬 
# print(arr)
# arr.sort(reverse=True) # 역순정렬 
# print(arr)


# 리스트 삭제 - del, pop, remove, clear (모두삭제할 때 사용하는 명령어)
# arr = [1,2,3,4,5]
# # pop 
# print(arr)
# arr.pop(2) # 2번 주소값 삭제 중간 값을 삭제할 경우 삭제 된 값 뒤 주소 값이 삭제된 주소값으로 변경됨 원만해서는 마지막 주소 값을 삭제하는 경우가 많음
# print(arr)

# print(arr)
# arr.append(3)
# print(arr)

# #del
# print(arr)
# del arr[0]
# print(arr)

# # remove
# arr = [1,2,3,4,5,"안녕"]
# print(arr)
# arr.remove("안녕")
# print(arr)

# 리스트 추가
# a = [1,2,3]
# b = [4,5,6]
# print(a+b) # 원본에는 전혀 영향은 없음 

# a.extend(b) 
# print(a) # extend를 사용할 경우 원본에 영향에 감. 원본의 값을 직접 변경해서 추가해줌 

# arr = [1,2]
# # append : 맨 뒤에 추가 
# arr.append(3)
# arr.append(5)
# arr.append(9)
# print(arr)

#arr=[1,2,3,5,9]
# insert : 원하는 위치에 추가 원만해서는 사용하지는 않음 
# arr = [1,2,3,5,9]
# arr.insert(1,20)
# print(arr)

# arr1 = [1,2,3]
# arr2 = [4.5]
# arr3 = arr1+arr2 # 리스트+리스트 = 리스트 합쳐짐 
# print(arr1+arr2)
# print(arr3)

# arr4 = arr1*3
# print(arr4) # 3번 반복 

# aaa = [0,0,0,0,0,0,0,0,0,0]
# aaa2 = [0]*10
# print(aaa2)

# 리스트는 역슬래시 안 해도 줄바꿈이 가능 
# arr=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# arr=[[1,2,3],[4,5,6],[7,8,9]]
# print(arr)

# print(arr[1][1]) # 1번 리스트 중 1번 출력하라
# print(arr[1])# 



# 문자열 - 리스트형태로 저장 
# name = "안녕하세요반갑습니다."
# print(name)
# print(name[0])
# print(name[5])
# print(name[5:8])
# print(name[::-1]) # 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택 가능 
# print(name[::2])
# if "하" in name:
#     print("있습니다.")
# else:
#     print("없습니다.")

import random

# r_num= random.randint(1,10)
# # 3개의 숫자입력
# arr =[]
# arr.append(int(input("1. 1-10 숫자입력:")))  # 리스트에 값을 추가할 시 append 사용 
# arr.append(int(input("2. 1-10 숫자입력:"))) 
# arr.append(int(input("3. 1-10 숫자입력:"))) 
# print(arr)

# # 1번째 방법 
# if r_num in arr:
#     print("당첨")

# else:
#     print("꽝")
# print("랜덤숫자:", r_num)
# print("입력숫자:", arr)

# fruit=["사과", "수박", "딸기", "참외", "복숭아"]
# print(fruit[2]) # 2번만 출력 
# print(fruit[1:4]) # 1번부터 시작하여 4번 전까지 출력 1,2,3
# print(fruit[2:]) # 2번부터 끝까지 출력 2,3,4,5 
# print(fruit[:3]) # 처음부터 3번전까지 출력 
# print(fruit[:]) # 모두 출력 
# print(fruit[::2]) # 처음은 시작점, 두번째는 끝점, 세번째는 간격 

# # 슬라이싱 [시작:끝:간격]
# arr=[1,2,3,4,5,6,7,8,9]
# print(arr[::2])
# print(arr[1::2])
# print(arr[1],arr[8]) # 특정번호 출력 시에는 각각의 arr 로 지정해서 출력 지정
# print(arr[:-1]) # 맨 끝을 제외하고 출력하고 싶을 때 마지막 제외할 때 
# print(arr[::-1]) # 꺼꾸로 시작하라는 명령어 리스트 역순정렬 





# # 2번째 방법 
# if r_num in arr : print("당첨") 
# else: print("꽝")

# # 3번째 방법 
# print("당첨") if r_num in arr else print("꽝")

# r_num = random.randint(1,10)
# # 3개 숫자입력
# arr = []
# # 리스트에 값을 추가할시 append사용
# arr.append(int(input("1. 1-10 숫자입력 : ")))
# arr.append(int(input("2. 1-10 숫자입력 : ")))
# arr.append(int(input("3. 1-10 숫자입력 : ")))
# # 1
# if r_num in arr:
#     print("당첨")
# else:
#     print("꽝")
# # 2
# if r_num in arr: print("당첨")
# else: print("꽝")
# # 3
# print("당첨") if r_num in arr else print("꽝")

# 비교시 리스트는 ("검색내용" in 리스트) 하면 됨 
# a="사과"
# b="딸기"
# c="수박"
# d="참외"
# e="복숭아"

# a,b,c,d,e 중 참외가 있는지 확인하고
# 있으면 참외가 있습니다 언급 
# 없으면 참외가 없습니다 언급

# if a=="참외" or b=="참외" or c=="참외" or d=="참외" or e=="참외": 
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")

# # 리스트
# fruit=["사과", "수박", "딸기", "참외", "복숭아"]
# if "참외" in fruit:
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")

# 1~10 사이의 숫자 3개를 입력받아 
# 랜덤숫자를 맞추면 당첨, 그렇지 않으면 꽝

# no1=int(input("1.숫자입력:"))
# no2=int(input("2.숫자입력:"))
# no3=int(input("3.숫자입력:"))
# print("입력숫자:", no1, no2, no3)

# # 반복문을 사용할 수 없음
# # 일반 변수는 반복문을 사용하기 힘듬 

# num=[0,0,0]
# num=[0]=int(input("1.숫자입력:"))
# num=[1]=int(input("2.숫자입력:"))
# num=[2]=int(input("3.숫자입력:"))


# 리스트 추가 가능 타임 : 모든  타입 
# arr = [1, "안녕", 1.2, True, [1,2,3]]
# print(["안녕", True, [1,2,3,4]])
# print(arr[1])
# print(arr[3])
# print(arr[4])
# print(arr [4][1])
# a=arr[4]
# print(a[1])

# 리스트 = 배열 
# a=1
# arr = [1, 2, 3, 4, 5]
# print(a) # 1
# print(type(arr)) # <class 'list'>
# print(arr) # [1, 2, 3, 4, 5] # 1 = 주소값 0 ....이렇게 해서 5 = 주소값 4 파이썬은 0부터 시작하고 끝은 -1로도 확인 가능함 
# print(arr[1]+1) # 3 
# print(arr[4]+1)
# print(arr[2])

# print(len(arr)) # 리스트 개수 length 줄임 
# # 리스트는 대괄화 [] 로 시작
# # 리스트는 0번부터 주소가 시작 
# # 리스트를 print하면 모두 출력 가능 
# # 리스트의 특정주소로 그 값을 출력할 수 있음
# # 리스트의 개수 : len() 
# # 리스트 안에는 모든 타입을 넣을 수 있음 - 정수, 실수, 문자열, 불, 리스트, 튜플, 딕셔너리 다 넣을 수 있음







 