# 학생 두 명의 성적을 입력받아 출력하시오.
# 번호, 이름, 국어, 영어, 수학 점수를 입력받아 
# 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하시오

print("-"*60)
no1=input("번호를 입력하세요.")
name1=input("이름을 입력하세요.")
kor1=int(input("국어점수를 입력하세요.")) #한줄복사 : shift+alt+방향키
eng1=int(input("영어점수를 입력하세요.")) 
math1=int(input("수학점수를 입력하세요."))

no2=input("번호를 입력하세요.")
name2=input("이름을 입력하세요.")
kor2=int(input("국어점수를 입력하세요."))
eng2=int(input("영어점수를 입력하세요."))
math2=int(input("수학점수를 입력하세요."))

total1=kor1+eng1+math1
avg1=total1/3

total2=kor2+eng2+math2
avg2=total2/3

print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)

print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
    format(no1,name1, kor1, eng1, math1, total1, avg1))

print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
    format(no2,name2,kor2,eng2,math2,total2,avg2))

print("-"*60)

print("-"*60)
no2=input("번호를 입력하세요.")
name2=input("이름을 입력하세요.")
kor2=int(input("국어점수를 입력하세요."))
eng2=int(input("영어점수를 입력하세요."))
math2=int(input("수학점수를 입력하세요."))
total2=kor2+eng2+math2
avg2=total2/3
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)

print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
    format(no2,name2,kor2,eng2,math2,total2,avg2))
print("-"*60)
 