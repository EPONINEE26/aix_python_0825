from student import Student
from students import Students

stus = Students()
stuNum = 1 

stuList=[]
title=["번호","이름","국어","영어","수학","합계","평균"] 
s_title=["no","name","kor","eng","math","total","avg"]   

def readStu():
    global stuNum 
    with open("C:/aaa/stu.txt", "r", encoding="utf-8") as f:
        while True:                
            str = f.readline()
            if str.strip() =="": break
            stu = str.strip().split(",")

            for i,s in enumerate(stu): 
                if 0<=i<=1: continue
                elif 2<=i<=5: stu[i] = int(s.strip())
                elif i==6: stu[i] = float(s.strip())
                elif i==7: stu[i] = int(s.strip())

        stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
        stuNum = len(stus.slist)+1 

def writeStu():
    with open("C:/aaa/stu.txt", "r", encoding="utf-8") as f:
            for s in stus:
                str=s.s_str()
                f.write(str+"\n")
            print("성적파일이 수정되었습니다.")
            print()

def main_screen():
        print("[ 학생성적프로그램 ]")
        print("1. 학생성적입력")
        print("2. 학생성적출력")
        print("3. 학생성적수정")
        print("9. 학생성적파일저장")
        print("0. 프로그램저장")
        print("-"*60)
        choice = int(input("원하는 번호입력 : "))
        return choice

def stu_input():
    global stuNum 
    print("[ 학생성적입력 ]")
    no = stuNum
    name = input(f"{name} 번째.학생이름 입력 : ")
    kor = int(input("국어점수 입력 : "))
    eng = int(input("엉여점수 입력 : "))
    math = int(input("수학점수 입력 : "))
    total = kor+eng+math
    avg = total/3 
    stus.add(Student(no,name,kor,eng,math))
    stuNum += 1 

def stu_output():
    stus.print()

def stu_update():
    while True: 
        print()
        print("[ 학생성적수정 ]")
        no=stuNum
        name=input(f"{name} 학생이 검색되었습니다.")
        if s.name == name:
            temp = 1 
        print("[ 수정과목 ]")
        print("1.국어 2.영어 3.수학")
        choice = int(input("과목을 선택하세요. >>"))
        if choice == 1:
            print("[ 국어점수변경 ]")
            print("현재 국어점수 : ",s.kor)
            s.kor = int(input("변경점수입력 : "))
        elif choice == 2:
            print("[ 영어점수변경 ]")
            print("현재점수 : ", s.eng)
            s.eng = int(input("변경점수입력 : "))
        elif choice == 3:
            print("[ 수학점수변경 ]")
            print("현재점수 : ", s.math)
            s.math = int(input("변경점수입력 : "))
        else :
            print("프로그램종료")
            print()

        if temp == 0:
            print(f"{name} 학생이 없습니다. 다시 검색하세요.")







