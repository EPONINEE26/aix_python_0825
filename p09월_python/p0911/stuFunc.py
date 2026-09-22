# 5분 전에 정상적으로 구현이 되는 코드가 5분 후 실행하게 되면 에러 발생으로 몇 시간 넘게 지속되었기에 여러 번 재 설치 끝에 겨우 구현이 되는 일이 있었음. 

from student import Student
from students import Students

stus = Students()
stuNum = 1 

stuList=[]
title=["번호","이름","국어","영어","수학","합계","평균"] 
s_title=["no","name","kor","eng","math","total","avg"]  

def readStu():
    global stuNum
    with open ("C:/aaa/stu.txt.txt", "r", encoding="utf-8") as f: # stu.txt 불러오는 에러가 몇 시간 지속되어 여러 번 저장 이름을 변경하였으며 stu.txt.txt로 변경 후 실행 가능하게 됨 
        while True:
            str = f.readline()
            if str == "" : break
            stu = str.split(",")

            for i,s in enumerate(stu):
                if 0<=i<=1 : continue
                elif 2<=i<=5: stu[i]=int(float(s.strip()))
                elif i==6: stu[i]=float(s.strip())
                                
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6]))
            stuNum = len(stus.slist) + 1 

def writeStu():
    with open ("C:/aaa/stu.txt.txt", "w", encoding="utf-8") as f:
        for s in stus.slist:
            line = f"{s.no},{s.name},{s.kor},{s.eng},{s.math},{s.total},{s.avg}"
            # 몇 시간 넘게 str로 지정하여 실행해도 에러발생이 몇 시간째 되어 이름변경 여러 번 해도 안 되기에 재설치 후 line이라는 이름으로 변경한 다음 실행이 됨 
            f.write(line + "\n")
        print("성적파일이 저장되었습니다.")

def main_screen():
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력: ")
    print("2. 성적출력: ")
    print("3. 성적수정: ")
    print("9. 성적파일저장: ")
    print("프로그램 종료")
    print("-"*60)
    choice = int(input("원하는 번호입력 : "))
    return choice 

def stu_input():
    global stuNum
    while True:
        print()
        print("[ 학생성적입력 ]")
        no = stuNum
        name = input(f"{stuNum} 학생이름 (0.이전페이지 이동 ): ")
        if name == '0': 
            break 
        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        math = int(input("수학 : "))
        total = kor+eng+math
        avg = total/3
        rank =  0

        stus.add(Student(no,name,kor,eng,math,total,avg))
        print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
        print()
        stuNum += 1

def stu_output():
    stus.print()

def stu_update():
    temp = 0
    name = input("수정할 학생 이름을 입력하세요: ")
    for s in stus.slist:
        if s.name == name :
            temp = 1 
            print(f"{name} 학생이 검색되었습니다.")
            print("[ 수정과목 ]")
            print("1. 국어  2. 영어  3. 수학")
            print("-"*60)
            choice = int(input("과목을 선택하세요 (0. 취소)>> "))
            if choice == 1:
                print("[ 국어점수 변경 ]")
                print("현재점수 : ", s.kor)
                s.kor = int(input("변경점수입력 : "))
            elif choice == 2:
                print("[ 영어점수 변경 ]")
                print("현재점수 : ", s.eng)
                s.eng = int(input("변경점수입력 : "))
            elif choice == 3:
                print("[ 수학점수 변경 ]")
                print("현재점수 : ", s.math)
                s.math = int(input("변경점수입력 : "))

            s.s_total()
            s.s_avg()
            print("수정이 완료되었습니다.")
            print()

    if temp==0:
        print(f"{name} 학생이 없습니다. 다시 검색하세요.")