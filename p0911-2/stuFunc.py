from student import Student
from students import Students

stus = Students()
stuNum = 1 

stuList=[]
title=["번호","이름","국어","영어","수학","합계","평균","등수"]              # ★ 등수 추가
s_title=["no","name","kor","eng","math","total","avg","rank"]             # ★ 등수 추가

def readStu():
    global stuNum
    with open ("C:/aaa/stu.txt.txt", "r", encoding="utf-8") as f:
        while True:
            str = f.readline()
            if str == "" : break
            if str.strip() == "" : continue          # ★ 빈 줄이면 건너뛰기 (IndexError 방지)
            stu = str.split(",")

            for i,s in enumerate(stu):
                if 0<=i<=1 : continue
                elif 2<=i<=5: stu[i]=int(float(s.strip()))
                elif i==6: stu[i]=float(s.strip())
                elif i==7: stu[i]=int(s.strip())         # ★ 등수 추가 (stu[7])

            if len(stu) >= 8:                            # ★ 등수까지 저장된 파일이면
                stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
            else:                                         # ★ 등수 없는 예전 파일도 읽을 수 있게
                stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6]))
            stuNum = len(stus.slist) + 1 

def writeStu():
    with open ("C:/aaa/stu.txt.txt", "w", encoding="utf-8") as f:   # "a" -> "w" : 저장할 때마다 중복 누적되는 문제 해결
        stus.set_rank()                                   # ★ 저장 전 등수 계산
        for s in stus.slist:
            line = f"{s.no},{s.name},{s.kor},{s.eng},{s.math},{s.total},{s.avg},{s.rank}"   # ★ 등수 추가
            f.write(line + "\n")
        print("성적파일이 저장되었습니다.")

def main_screen():
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력: ")
    print("2. 성적출력: ")
    print("3. 성적수정: ")
    print("91. 성적파일저장: ")
    print("8. 등수별출력: ")                                  # ★ 등수 메뉴 추가
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

        stus.add(Student(no,name,kor,eng,math,total,avg))   # 등수는 자동 계산되므로 입력받지 않음
        print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
        print()
        stuNum += 1

def stu_output():
    stus.print()

def stu_rank():                                            # ★ 등수순 출력 (신규 추가)
    stus.set_rank()
    ranked = sorted(stus.slist, key=lambda s: s.rank)
    print()
    print("-"*25, end="")
    print("[ 등수별 학생성적출력 ]")
    print("-"*60)
    print("번호","이름","국어","영어","수학","합계","평균","등수")
    for s in ranked:
        print(s)

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
            stus.set_rank()                                # ★ 점수 수정 후 등수 재계산
            print("수정이 완료되었습니다.")
            print()

    if temp==0:
        print(f"{name} 학생이 없습니다. 다시 검색하세요.")
