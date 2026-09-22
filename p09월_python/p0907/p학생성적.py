# import p_stu_m as pm
from p_stu_m import * # * (별표) : 모든 것을 다 가져옴이라는 의미 

# 파일불러오기 
readStu() 

while True:
    # 메인화면출력 
    choice = main_screen()

    if choice == 1: 
        stu_input()

    elif choice == 2:
        stu_output()

    elif choice == 3:
        pass 
    elif choice == 9:
        writeStu()
        
    else :
        print("프로그램 종료")
        break 