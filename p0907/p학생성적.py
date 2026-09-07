# import p_stu_m as pm
from p_stu_m import * # * (별표) : 모든 것을 다 가져옴이라는 의미 

# 학생성적 파일불러오기 
def readStu():
    with open("c:/aaa/stu.txt", "r", encoding="utf-8") as f:
        while True: 
            str = f.readline() # 1,홍길동,100,100,100,300,100.0 이런식으로 불러온다 
            if str == "" : break
            stu = str.split(",") 
            for i,s in enumerate(stu):
                if 0<=i<=1: continue
                elif 2<=i<=5 : stu[i]= int(s.strip())
                elif i==6 : stu[i]= float(s.strip())  
                elif i==7 : stu[i]= float(s.strip()) 
                
            stuList.append()








while True:
    # 메인화면출력 
    choice = main_screen()

    if choice == 1: 
        stu_input(choice)

    elif choice == 2:
        stu_output()

    elif choice == 3:
        pass 
        print()
    elif choice == 9:
        pass 
        print()
    else :
        print("프로그램 종료")
        break 