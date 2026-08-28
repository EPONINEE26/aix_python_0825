# 학생 성적
# 번호, 이름, 국어, 영어, 수학 
# 합계, 평균 
# 성적 출력하도록 구성하시오.

# 입력 -> 변수 저장 -> DB 저장 
s=[] #리스트 타입 - append, insert / pop, del, remove (지울때에는 웬만해서는 마지막 주소값을 지우는 것이 좋음)


no=input("번호 입력:") # str 
name=input("이름 입력:")
kor=int(input("국어점수 입력:")) # int (숫자입력) kor=int(kor)
eng=int(input("영어점수 입력:")) # int 
math=int(input('수학점수 입력:')) # int 
total=kor+eng+math
avg=total/3 # 나눗셈 -> 실수로 변경되어 float 

print("번호\t이름\t국어\t영어\t수학\t합계\t평균") #shift+방향키 하면 복사 부분 형성됨 
print("-"*60) # 문자에 곱하기를 하면 반복 
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}") 
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
      format(no,name,kor,eng,math,total,avg))
# f 함수 / format 함수 사용 하는때가 다르기에 사용할 때마다 확인하고 사용
print("-"*60)

