# 1~100 사이 랜덤번호를 맞추는 프로그램을 구현하시오
# 랜덤번호보다 높은 수를 입력하면 낮은 숫자 입력!!, 높은 숫자 입력!!!
# 정답을 맞추면
# 정답숫자:
#입력한 숫자 모두 출력: 


import random
ran1=random.randint(1,101)
my_list=[]
myNum=0
answer=0

while True:
    myNum=int(input("1~100 사이 숫자를 입력 : "))
    my_list.append(myNum)
    print(myNum)
    if myNum==ran1:
        answer=myNum
        print("정답입니다.")
    elif myNum > ran1:
        print("랜덤번호보다 큽니다. 작은수 입력 : ")
    else: 
        print("랜덤번호보다 작습니다. 큰수 입력 : ")
        break 

print("랜덤번호 : ", myNum)
print("정답숫자 : ", answer)
print("입력숫자 : ", my_list)


