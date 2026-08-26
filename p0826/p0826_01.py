print("안녕")
# 10+5=15, 10-5=5 
# 더하기 : 15, 빼기 : 5
print("더하기 : {}, 빼기 : {}".format(10+5,10-5))

print("-"*60)
no1=input("번호를 입력하세요.")
name1=input("이름을 입력하세요.")
kor1=int(input("국어점수를 입력하세요."))
eng1=int(input("영어점수를 입력하세요."))
math1=int(input("수학점수를 입력하세요."))
total1=kor1+eng1+math1
avg1=total1/3
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{}".\
      format(no1, name1, kor1, eng1, math1, total1, avg1))
print("-"*60)


print("-"*60)
no2=input("번호를 입력하세요.")
name2=input("이름을 입력하세요.")
kor2=int(input("국어점수를 입력하세요."))
eng2=int(input("영어점수를 입력하세요."))
math2=int(input("수학점수를 입력하세요."))
total2=kor2+eng2+math2
avg2=total2/3
print("-"*60)
print("번호{}\t이름{}\t국어{}\t영어{}\t수학{}\t합ㅖ{}\t평균{}".\
      format(no2, name2, kor2, eng2, math2, total2, avg2))
print("-"*60)


# name = input("이름을 입력하세요")
# kor = int(input("국어점수를 입력하세요."))
# eng = int(input("영어점수를 입력하세요."))
# math = int(input("수학점수를 입력하세요."))
# total = kor+eng+math
# avg = total/3
# name = "홍길동"

# print("합계:{}, 평균:{}".format(300, 100))
# print("합계:{}, 평균:{}".format(total, avg))
# print("합계:{}, 평균:{:2f}".format(total, avg, name))
# print("이름:{}, 합계:{}, 평균:{}".format(name, total, avg))

