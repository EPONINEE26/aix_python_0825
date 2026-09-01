# 리스트 - 배열 (C 나 Java C++ 에선 배열(Array) 이라고 지칭. 최근에는 리스트로 지칭
# a,b,c,d=0,0,0,0 # 변수 추가할 때마다 직접 입력을 해야함 
# print(a)
# print(b)
# print(c)
# print(d)

# a_arr=[0,0,0,0,0]
# for a in a_arr:
#     print(a) # 추가할 때도 작성된 변수 모든 변수 출력 

# a_arr=[10,20,30,40,50,60,70,80,90,100]
# sum=0
# for a in a_arr:
#     print(a) 
#     sum +=a 
# print(sum)

# print(a_arr[2:5])
# print(a_arr[::-1])

# 리스트 추가 : append:맨 뒤에 입력, insert:위치지정 입력, extend: 리스트+리스트
# 리스트 수정 : a_arr[위치]=1000
# 리스트 삭제 : pop(위치):위치가 없으면 맨 뒤에, del : 위치 

# a_list=[1,2,3]
# a_list.append(4) 
# print(a_list)
# a_list.pop()
# print(a_list)
# a_list.pop(0) # 위치 값 넣어서 삭제 
# print(a_list)

# 퀴즈
# n_arr=[100,91,230,1,2,5,70,500]
# # 100 이상의 숫자만 출력하시오.
# for n in n_arr:
#     print(n_arr)

# n_arr=[100,91,230,1,2,5,70,500]
# # 100 이상의 숫자만 출력하시오.
# for n in n_arr:
#     if n >= 100: 
#         print(n)

# n_arr=[100,91,230,1,2,5,70,500]
# for n in n_arr:
#     if n >= 100: 
#         a_arr.append(n)
#         print(n)
# print(a_arr)

# 100:3자리숫자 
# 91:2자리숫자 
# 230:3자리숫자
# 1:1자리숫자 .... 이렇게 출력하고자 할 때 

n_arr=[100,91,230,1,2,5,70,500]

# a=100
# b="100"
# print(int(input(len(b))))
# print(int(input(len(b))))

# n_arr=[100,91,230,1,2,5,70,500]
# a_arr=[]
# for n in n_arr: # 정수형 타입 -> 문자열 타입으로 변환 
#     no=len(str(n))
#     print(n, ":", no, "자리숫자")

# n_arr=[100,91,230,1,2,5,70,500]
# a_arr=[]
# for n in n_arr: 
#     no=len(str(n))
#     a="{}:{}자리숫자".format(n,no) # format : 문자열로 변환 
#     a_arr.append(a)
#     print(a)
# print(a_arr)

# ['100:3자리숫자', '91:2자리숫자', '230:3자리숫자', '1:1자리숫자', '2:1자리숫자', '5:1자리숫자', '70:2자리숫자', '500:3자리숫자']

# n_arr=[100,91,230,1,2,5,70,500]
# a_arr=[]
# for n in n_arr: 
#     no=len(str(n))
#     a="{}:{}자리숫자".format(n,no) # format : 문자열로 변환 
#     a_arr.append(a)
#     print(a)
# print(a_arr)


# for i in range(0,4):
#     aa[1]=int(input(str(i+1)+"번째 숫자:"))
#     print(aa) 

