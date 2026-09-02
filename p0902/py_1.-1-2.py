# import random
# lotto=random.sample(range(1,46),6)
# print("확인로또 : " , lotto)

# arr1=[]
# no=0
# for i in range(6):
#     no=int(input("1~45사이 숫자 입력 : "))
#     arr1.append(no)

# answer_arr=[]

# for i in arr1:
#     if i in lotto:
#         answer_arr.append(i)

# print("로또 번호 : ", lotto)
# print("입력 번호 : ", arr1)
# print("정답 번호 :  ", answer_arr)
# print("정답 개수 : ", len(answer_arr))


# import random
# num1=random.randint(1,100)
# num2=random.randint(1,100)
# num3=random.randint(1,100)

# arr1=[num1, num2, num3]
# arr2=random.sample(range(1,101),3)
# arr1.sort()

# input1=int(input("숫자 입력:"))

# if input1 in arr1:
#     print("당첨!!")
# else:
#     print("꽝 ^^")

# print("랜덤숫자:", arr2)
# print("입력숫자:", input1)

import random
ran1=random.randint(1,101)
my_list=[]
myNum=0
answer=0

while True:
    myNum=int(input("1~100 사이 숫자 입력 : "))
    my_list.append(myNum)
    print(myNum)
    if myNum == ran1:
            answer=myNum
            print("정답입니다.")
    elif myNum > ran1:
        print("랜덤숫자보다 큽니다. 작은 수 입력 : ")
    else:
        print("랜덤숫자보다 작습니다. 큰 수 입력 :")
        break

print("랜덤숫자 : ", myNum)
print("정답숫자 : ", answer)
print("입력숫자 : ", my_list)

    
# import random
# ran1=random.randint(1,101)
# my_list=[]
# myNum=0
# answer=0   
    

# while True:
#     myNum=int(input("1~100 사이 숫자를 입력 : "))
#     my_list.append(myNum)
#     print(myNum)
#     if myNum==ran1:
#         answer=myNum
#         print("정답입니다.")
#     elif myNum > ran1:
#         print("랜덤번호보다 큽니다. 작은수 입력 : ")
#     else: 
#         print("랜덤번호보다 작습니다. 큰수 입력 : ")
#         break 

# print("랜덤번호 : ", myNum)
# print("정답숫자 : ", answer)
# print("입력숫자 : ", my_list)


