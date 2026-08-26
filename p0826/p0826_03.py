# print : 출력
# input : 입력 
# num = input("숫자를 입력하세요.")
# print("입력숫자 : {}".format(num))

a = 10
b = 3 
# input으로 받은 모든 것은 문자열 타입 
#a = int(input("1번째 숫자를 입력하세요.")) # str 타입을 int타입으로 변경 
#b = int(input("2번째 숫자를 입력하세요.")) 
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a**b) # 10*10*10 / 10에 3승

# 아이디, 패스워드를 입력받아 출력하시오
# 아이디:aaa, 패스워드:1111

id="aaa"
pw:"1111"
a=input("아이디를 입력하세요") 
b=input("패스워드를 입력하세요")
# input("아이디, 패스워드를 입력받아 출력하시오")
print("input(아이디:{}, 패스워드:{}".format(id, pw))
print("aaa==id")
print("1111==pw")

print("아이디확인:{}".format("aaa==id"))
print("패스워드확인:{}".format("1111==pw"))
print("아이디:{}, 패스워드:{}".format(id,pw))

   

num1 = 100
num2 = 100
num3 = 100
print(num1,num2,num3)
print(num1+num2+num3)
print(int(float(1.5)))
print(float(int(3)))

num4=num5=num6=1
print(num4,num5,num6) # 타입이 같을 경우에는 한 줄로 넣어도 가능하다 

#한줄에 여러 변수에 여러개 값을 넣는 것은 불가능 
# a1=1, a2=2 이런 식은 불가능 

a1=1
a2=2
print(a1,a2)

no1 = 100 # 변수선언과 동시에 값 전달 
print(10==10) # 같다는 표현은 == 
