from student import *

readStu()
while True:
    choice = main_screen

    if choice == 1:
        stu_input()
    elif choice ==2:
        stu_output()    
    elif choice ==3: 
        stu_update()
    elif choice == 8:
        print("등수 처리")
    elif choice == 9:
        writeStu()
    else:
        print("프로그램 죵료")
        break 