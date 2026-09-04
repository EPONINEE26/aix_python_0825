# title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
# stu = []
# sno = 1 # 학생성적인원변수 - db 에서 번호 부여 

# # # 메인화면함수선언 -------------------------------------------------
# def s_mainPrint(): # 메인화면함수 
#     print("[ 학생성적프로그램 ]")
#     print("1. 학생성적입력")
#     print("1. 학생성적출력")
#     print("-"*60)
#     choice=int(input("원하는 번호를 입력하세요.>>"))
#     print()
#     return choice # 프로그램에서 함수로 보내는 것은 매개변수 함수에서 프로그램으로 가게 하는 것은 return 

# # 학생성적입력함수선언 --------------------------------------------------
# def s_input(sno): 
#     while True: # 입력을 멈추고 싶을때까지 입력받음 
#         no = sno # 위 부분에 지정해 놓은 sno 지정 숫자로 인해 무조건 있어야만 함 지역변수로 인식하기에 숫자를 가져오지 않음 
#         print("[ 학생성적입력 ]")
#         name = input(f"{no}번째 이름 입력 (0. 이전화면 이동): ")
#         if name =="0": break 
#         kor = int(input("국어점수 입력 : "))
#         eng = int(input("영어점수 입력 : "))
#         math = int(input("수학점수 입력 : "))
#         total = kor+eng+math
#         avg = total/3 

#         # 리스트에 저장 - 파일 저장 - db에 저장 
#         stu.append({'no':no, 'name':name, 'kor':kor, \
#                     'eng':eng, 'math':math, 'total':total, \
#                         'avg':avg})
#         print(f"{name} 학생성적이 저장되었습니다.")
#         print()
#         # score = [0]*3 # 리스트 3개 생성 방법 
#         # for i in range(3): 
#         #     score [i]=int(input(f"{title[i+2]} 점수를 입력하세요. : "))           

#         sno += 1 
#     return sno 



# while True:
#     choice = s_mainPrint()
#     if choice == 1: 
#         sno = s_input(sno) # 매개변수가 동일해야만 함 
        

# title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
# k_title = ["no", "name", "kor", "eng", "math", "total", "avg"]
# stu = []
# sno = 1 # 학생성적인원변수 - db 에서 번호 부여 

# # # 메인화면함수선언 -------------------------------------------------
# def s_mainPrint(): # 메인화면함수 
#     print("[ 학생성적프로그램 ]")
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("3. 학생성적수정")
#     print("-"*60)
#     choice = int(input("원하는 번호를 입력하세요.>>"))
#     print()
#     return choice # 프로그램에서 함수로 보내는 것은 매개변수 함수에서 프로그램으로 가게 하는 것은 return 

# # 학생성적입력함수선언 --------------------------------------------------
# def s_input(): 
#     global sno #위치 주소를 가져와서 그 주소에 있는 정보를 출력해줌. 지역변수 내 젼역변수를 쓰려고 global을 쓴다 
#     while True: # 입력을 멈추고 싶을때까지 입력받음 
#         no = sno # 위 부분에 지정해 놓은 sno 지정 숫자로 인해 무조건 있어야만 함 지역변수로 인식하기에 숫자를 가져오지 않음 
#         print("[ 학생성적입력 ]")
#         name = input(f"{no}번째 이름 입력 (0. 이전화면 이동): ")
#         if name =="0": break 
#         kor = int(input("국어점수 입력 : "))
#         eng = int(input("영어점수 입력 : "))
#         math = int(input("수학점수 입력 : "))
#         total = kor+eng+math
#         avg = total/3 

#         # 리스트에 저장 - 파일 저장 - db에 저장 
#         stu.append({'no':no, 'name':name, 'kor':kor, \
#                     'eng':eng, 'math':math, 'total':total, \
#                         'avg':avg})
#         print(f"{name} 학생성적이 저장되었습니다.")
#         print()
#         # score = [0]*3 # 리스트 3개 생성 방법 
#         # for i in range(3): 
#         #     score [i]=int(input(f"{title[i+2]} 점수를 입력하세요. : "))           

#         sno += 1 
#         s_output() # 한명만 출력하고 싶을 때에는 s1_output() 이런식으로 함수를 설정하면 된다 

# # 학생성적출력부분함수선언 --------------------------------------------
# def s_output(): 
#     print()
#     print("[ 학생성적출력 ]")
#     print("-"*60)
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
#     print("-"*60)
#     for s in stu:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
#     print()

# def s_update(): # 학생성적수정
#     print()
#     print("[ 학생성적수정 ]")
#     name = input("찾을려는 학생이름을 입력하세요.>> ")
#     temp = 0
#     for i,s in enumerate(stu):
#             if s['name']==name:
#                 print(f"{name} 학생을 찾았습니다.")
#                 temp = 1
#                 break

#     if temp == 0:
#             print(f"{name} 학생이 없습니다.")
#     elif temp == 1:
#             print("[ 과목수정선택 ]")
#     print("1. 국어   2. 영어   3. 수학")
#     choice = int(input("원하는 번호 입력 : "))
#     if choice == 1:
#                 print(f"현재국어점수 : {s['kor']}")
#                 # print(f"현재{title[choice+1]} 점수 : {s['k_title[choice+1]']}")
#                 s['kor'] = int(input("변경하려는 국어점수 : "))
#                 # s[k_title[choice+1]] = int(input(f" 변경하려는 {title[choice+1]}))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total'] /3 
#                 print(f"{s['kor']} 점으로 국어점수가 변경되었습니다.")
#     elif choice == 2:
#                 print(f"현재국어점수 : {s['kor']}")
#                 # print(f"현재{title[choice+2]} 점수 : {s['k_title[choice+2]']}")
#                 s['eng'] = int(input("변경하려는 영어점수 : "))
#                 print(f"{s['eng']} 점으로 영어점수가 변경되었습니다.")
#                 # s[k_title[choice+2]] = int(input(f" 변경하려는 {title[choice+2]}))
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total'] /3 
#     elif choice == 3:
#                 print(f"현재국어점수 : {s['kor']}")
#                 # print(f"현재{title[choice+3]} 점수 : {s['k_title[choice+3]']}")
#                 s['math'] = int(input("변경하려는 수학점수 : "))
#                 # s[k_title[choice+3]] = int(input(f" 변경하려는 {title[choice+3]}))
#                 print(f"{s['math']} 점으로 수학점수가 변경되었습니다.")
#                 s['total'] = s['kor']+s['eng']+s['math']
#                 s['avg'] = s['total'] /3 


# while True:
#     choice = s_mainPrint() #메인화면부분 함수호출 
#     if choice == 1: #학생성적입력부분 
#         s_input()
#         s_output()
#     elif choice == 2: # 학생성적출력부분 
#         s_output()
#     elif choice == 3: #학생성적수정부분 
#         s_update() 
#         s_output()

# while True:
#     choice = s_mainPrint() #메인화면부분 함수호출 
#     if choice == 1: #학생성적입력부분 
#         sno = s_input() # 매개변수가 동일해야만 함 
#     elif choice == 2: # 학생성적출력부분 
#         print()
#         print("[ 학생성적출력 ]")
#         print("-"*60)
#         print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
#         if len (stu) == 0:
#             print("*** 학생데이터가 없습니다.***")
#         else : 
#             for s in stu:
#                 print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}")
#         print()        

title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
k_title = ["no", "name", "kor", "eng", "math", "total", "avg"]
stu = []
sno = 1 

메인화면함수선언 -------------------------------------------------
def s_mainPrint(): # 메인화면함수 
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>>"))
    print()
    return choice # 프로그램에서 함수로 보내는 것은 매개변수 함수에서 프로그램으로 가게 하는 것은 return 

# 학생성적입력함수선언 --------------------------------------------------
def s_input(): 
    global sno #위치 주소를 가져와서 그 주소에 있는 정보를 출력해줌. 지역변수 내 젼역변수를 쓰려고 global을 쓴다 
    while True: # 입력을 멈추고 싶을때까지 입력받음 
        no = sno # 위 부분에 지정해 놓은 sno 지정 숫자로 인해 무조건 있어야만 함 지역변수로 인식하기에 숫자를 가져오지 않음 
        print("[ 학생성적입력 ]")
        name = input(f"{no}번째 이름 입력 (0. 이전화면 이동): ")
        if name =="0": break 
        kor = int(input("국어점수 입력 : "))
        eng = int(input("영어점수 입력 : "))
        math = int(input("수학점수 입력 : "))
        total = kor+eng+math
        avg = total/3 

        #리스트에 저장 - 파일 저장 - db에 저장 
        stu.append({'no':no, 'name':name, 'kor':kor, \
                    'eng':eng, 'math':math, 'total':total, \
                        'avg':avg})
        print(f"{name} 학생성적이 저장되었습니다.")
        print()
        # score = [0]*3 # 리스트 3개 생성 방법 
        # for i in range(3): 
        #     score [i]=int(input(f"{title[i+2]} 점수를 입력하세요. : "))           

        sno += 1 
        s_output() # 한명만 출력하고 싶을 때에는 s1_output() 이런식으로 함수를 설정하면 된다 

# 학생성적출력부분함수선언 --------------------------------------------
def s_output(): 
    print()
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
    print("-"*60)
    for s in stu:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
    print()

def s_update(): # 학생성적수정
    print()
    print("[ 학생성적수정 ]")
    name = input("찾을려는 학생이름을 입력하세요.>> ")
    temp = 0
    for i,s in enumerate(stu):
            if s['name']==name:
                print(f"{name} 학생을 찾았습니다.")
                temp = 1
                break

    if temp == 0:
            print(f"{name} 학생이 없습니다.")
    elif temp == 1:
            print("[ 과목수정선택 ]")
    print("1. 국어   2. 영어   3. 수학")
    choice = int(input("원하는 번호 입력 : "))
    if choice == 1:
                print(f"현재국어점수 : {s['kor']}")
                # print(f"현재{title[choice+1]} 점수 : {s['k_title[choice+1]']}")
                s['kor'] = int(input("변경하려는 국어점수 : "))
                # s[k_title[choice+1]] = int(input(f" 변경하려는 {title[choice+1]}))
                s['total'] = s['kor']+s['eng']+s['math']
                s['avg'] = s['total'] /3 
                print(f"{s['kor']} 점으로 국어점수가 변경되었습니다.")
    elif choice == 2:
                print(f"현재국어점수 : {s['kor']}")
                # print(f"현재{title[choice+2]} 점수 : {s['k_title[choice+2]']}")
                s['eng'] = int(input("변경하려는 영어점수 : "))
                print(f"{s['eng']} 점으로 영어점수가 변경되었습니다.")
                # s[k_title[choice+2]] = int(input(f" 변경하려는 {title[choice+2]}))
                s['total'] = s['kor']+s['eng']+s['math']
                s['avg'] = s['total'] /3 
    elif choice == 3:
                print(f"현재국어점수 : {s['kor']}")
                # print(f"현재{title[choice+3]} 점수 : {s['k_title[choice+3]']}")
                s['math'] = int(input("변경하려는 수학점수 : "))
                # s[k_title[choice+3]] = int(input(f" 변경하려는 {title[choice+3]}))
                print(f"{s['math']} 점으로 수학점수가 변경되었습니다.")
                s['total'] = s['kor']+s['eng']+s['math']
                s['avg'] = s['total'] /3 

while True:
    choice = s_mainPrint() #메인화면부분 함수호출 
    if choice == 1: #학생성적입력부분 
        s_input()
        s_output()
    elif choice == 2: # 학생성적출력부분 
        s_output()
    elif choice == 3: #학생성적수정부분 
        s_update() 
        s_output()







