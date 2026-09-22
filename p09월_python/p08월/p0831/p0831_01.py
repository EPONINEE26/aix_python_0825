# 반복문 
# for 변수 in range(시작값, 끝값+1,증가값) 
# range(3) 3번 반복할 거라면 3이라고 써도 가능 
# for i in range(10): 
#     print(i) # range 범위 

# for i in range(1,5+1): # 5번까지 반복하세요 # 증가값 1이 숨겨져있음 
#     print(i)

# for i in range(1,11,2): # 2씩 증가  
#     print(i)

# for i in range(0,11,2): # 2씩 증가  
#      print(i)

# name = []
# for i in range(3):
#     a = input("이름입력 : ")
#     name.append(a)  # 리스트:append,insert,extend

# print("[ 학생명단 ]")
# print(name)
# for n in name:
#     print(n)

# [ 학생명단 ]
# 홍길동
# 유관순
# 이순신

# name = []
# for i in range(3):
#     a = input("이름입력 : ")
#     name.append(a)

# print("[ 학생명단 ]")

# # n을 사용하려면 반드시 이 형태로 들여쓰기가 되어 있어야 합니다.
# for n in name:
#     print(n, end=" ")


# for i in range(0,11): # 1,2,3.... 10 -> 10, 20, 30.... 100 으로 출력하시오 
#     print(i*10)
   
# arrs=[1,3,5,7]
# for arr in arrs:
#     print(arr)

# fruits = ["사과","배","바나나"] # 리스트처럼 입력할 경우 변수에 하나씩 출력함 
# for f in fruits:
#     print(f)

# nums=[3,9,10,105,220,2,1]
# for n in nums: # range # 자리에 리스트가 올수 있음 range, 리스트 및 문자가 올수 있음 
#     print(n)

# 입력한 숫자가 홀수인지 짝수인지 출력하시오.
# nums=[3,9,10,105,220,2,1]
# a=int(input("슷자 입력:"))
# if a%2==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다")

# nums=[3,9,10,105,220,2,1]
# for n in nums:
#     #  print(n)
#     #  a=int(input("숫자입력:"))
#     # %2==0
#      if n%2==0:
#         print(n,": 짝수입니다.")
#      else: pass # break는 한번하고 바로 멈추고 pass는 이 구문은 일단 지나가라는 뜻 
#         print(n,": 홀수입니다.")
         
# 반복문
# for i in range(10) / range(1,11) / rnage(1.11,2) / [1.2.3] / "안녕하세요."

# nums = [3, 9, 10, 105, 220, 2, 1]
# for n in nums:
#      print(n)
#      n = int(input("숫자입력:"))
     
#      # 입력한 숫자 n 뒤에 ": 짝수/홀수입니다."가 바로 붙도록 수정했습니다.
#      if n % 2 == 0:
#         print(n, ": 짝수입니다.")
#      else:
#         print(n, ": 홀수입니다.")

# print(1,end="\t") # 한칸 띄우고 싶으면 한칸만 공백생긴 후 출력 옆으로 출력 
# print(2,end="\t")
# print(3) 
# 1       2       3

# 구구단을 출력하시오
# for i in range(2,10):
#     print(i, "x", 1, "=", i*1) 
#     print(f"{i}x{1}={i*1}")  
#     print("{}x{}={}".format(i,1,i*1))  

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j))

# 단을 출력하고 싶을때 
# for i in range(2,10):
#     print("[{}단]".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j))


# for i in range(2,10):
#     print("[{}단]".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="  ") # 옆으로 출력 
# print()

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="\t") 
# print()

# for i in range(2,10):
#     print("[{}단]".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="  ") 
# print()


