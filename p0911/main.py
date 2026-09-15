from stuFunc import *

readStu()
while True:

    choice = main_screen() # main_screen 이름 에러가 몇 시간 넘도록 되어 여러 번 재설치 후 해결이 됨 
    if choice == 1:
        stu_input()
    elif choice ==2:
        stu_output()
    elif choice ==3:
        stu_update()
    elif choice == 9:
        writeStu() 
    else:
        print("프로그램 죵료")
        break



