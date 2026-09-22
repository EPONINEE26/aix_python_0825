# 10진수를 2진수로 변경하는 명령어 (bin)
print(bin(147)) 
print(bin(5))

# 2진수를 10진수로 출력하는 방법 
print(int("101",2))

print(100*100)

a=9
b=2
print(a/b)
print(a//b) # 몫 
print(a%b) # 나머지 

# a = 5
# 짝수, 홀수인지? 
print(5%2==0)
print(5%2==1)

a = 5
print(a%2==0)
print(a%2==1)

a = int(input("숫자를 입력하세요."))
print(a%2==0) 
print(a%2==1) 

#a,b = 1,2 
#print(a,b)

# a=b=1
#print(a,b)

# 에러
# a=1, b=2
#print(a,b)

# 국어, 영어, 수학점수를 입력받아
# 합계, 평균을 출력하시오
# 합계:300, 평균:100

name = input("이름을 입력하세요")
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
total = kor+eng+math
avg = total/3
name = "홍길동"

print("합계:{}, 평균:{}".format(300, 100))
print("합계:{}, 평균:{}".format(total, avg))
print("합계:{}, 평균:{:2f}".format(total, avg, name))
print("이름:{}, 합계:{}, 평균:{}".format(name, total, avg))



# 잔액 : 1000 고정 
# 송금금액 : 100 입력
# 총금액을 출력하시오 

# 출력되도록 하시오 
# 잔액 : 1000 
# 송금금액 : 100 
# 총금액 : 1100 

total1 = 1000
send = 100
total2 = 1100 

print("total1 = 1000")
print("send = 100")
print("total2 = 1100")
print(int(input("송금금액을 입력하세요.")))
print("total1:{}, send:{}, total2:{}".format(total1, send, total2))

print("잔액 : ", total1)
print("송금 : ", send)
print("총금액 : ", total2)


total1 = 1000
send = int(input("송금금액을 입력하세요."))
total2 = total1+send

print("잔액 : ",total1)
print("송금금액 : ",send)
print("총금액 : ",total2)
print("잔액 : {}, 송금금액 : {}, 총금액 : {}".format(total1,send,total2))
