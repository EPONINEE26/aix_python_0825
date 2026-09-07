def hap(): # 함수로 인해 모든 걸 다 알아서 할 때 
    num1 = int(input("숫자입력1 : "))
    num2 = int(input("숫자입력2 : "))
    for i in range(10):
        sum = num1+num2
    print(sum)

def hap2(num1,num2): # 실행 때 입력 받아 함수로 처리한 다음 함수에서 출력할 때 
    for i in range(10):
        sum = num1+num2
    print(sum)

       
def hap3(num1,num2): # 함수에서 입력 받고 수식 처리 한 다음 출력은 실행에서 출력할 때 
    num1 = int(input("숫자입력5 : "))
    num2 = int(input("숫자입력6 : "))
    for i in range(10):
        sum = num1+num2
    return sum

def hap3(num1,num2): # 함수에서 입력 받고 수식 처리 한 다음 출력은 실행에서 출력할 때 
    for i in range(10):
        sum = num1+num2
    return sum


# 1. 매개변수X, return X - hap()
hap()

# 2. 매개변수 O, return X - hap2()
num1 = int(input("숫자입력3 : "))
num2 = int(input("숫자입력4 : "))
sum=hap2(num1,num2)


# 3. 매개변수 O, return O - hap3()
sum=hap3(num1,num2)
print(sum)

# 3. 매개변수 O, return O - hap3()
num1 = int(input("숫자입력5 : "))
num2 = int(input("숫자입력6 : "))
sum=hap2(num1,num2)
print(sum)