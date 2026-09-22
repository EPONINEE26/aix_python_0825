# 람다식 - 함수요약 
# 함수사용 
# def sum(n1, n2): 
#     result = n1 + n2
#     return result 
# print(sum(10,20))

# 람다식 - 1줄만 명령어가 있어야함. 2,3줄의 명령어는 안 됨
# lambda n1, n2 : n1 + n2 
# sum=lambda n1, n2 : n1 + n2 
# print(sum(10,20))

# lambda n1, n2 : n1 * n2  # 결과 값이 하나만 가능 
# sum=lambda n1:n1+10
# print(sum(10))

# +10씩 반복적으로 하여 출력하시오.
# mList = [1,2,3,4,5] 
# mList2=[]
# for m in mList:
#     mList2.append(m+10)
# print(mList2)

# def add(num):
#     return num+10
# mList = [1,2,3,4,5] 
# a_arr=[]
# for m in mList:
#     a_arr.append(add(m))
#     print(a_arr)

# mList = [1,2,3,4,5] 
# a_arr=[]
# a_arr = [m+10 for m in mList] # 리스트 내포 
# print(a_arr)

# # map(함수, 리스트) -> map은 앞쪽에는 함수, 뒤쪽에는 리스트로 구성. 
# mList = [1,2,3,4,5] 
# a_lam = lambda num:num+10 
# mList2 = list(map(a_lam, [1,2,3,4,5])) # 이 예제는 무조건 외워야함 
# print(mList2)

# 문자열리스트를 숫자형리스트로 변환해주는 방법 
# data = ["100", "200", "300"]
# result = map(int,data) 
# print(list(result))

# a = [1,2,3]
# b = [10,20,30]
# result = map(lambda x,y: x+y, a,b) # 이 예제는 무조건 외워야함 
# print(list(result))

# factorial 재귀함수. 자기자신함수를 다시 호출 
# 1~4까지의 수의 곱을 구하시오.
# result = 1
# for i in range (1,5):
#     result *= i 
# print(result )

# def fact1(num):
#     if num <= 1: return num
#     else:return num * fact1(num-1) # 자기자신함수를 다시 호출한다는 의미 
# print(fact1(4))



