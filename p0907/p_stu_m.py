stuList = []
title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
s_title = ["no", "name", "kor", "eng", "math", "total", "avg", "rank"]
stuNum = 1 

def main_screen(): # 메인화면출력함수 
    print("[ 학생성적프로그램 ]")
    print("2. 성적입력")
    print("3. 성적출력")
    print("4. 성적수정")
    print("-"*60)
    choice = int(input("원하는 번호 입력 : "))
    return choice 

# 학생성적입력함수 
def stu_input(choice):
    global stuNum 
    while True: # 무한반복 입력 가능 
                print()
                print("[ 학생성적프로그램 ]")
                no = stuNum
                name = input(f"{stuNum} 번째. 학생이름 (0. 이전페이지 이동): ")
                if name == "0" : break
                kor = int(input("국어점수 입력 : "))
                eng = int(input("영어점수 입력 : "))
                math = int(input("수학점수 입력 : "))
                total = kor+eng+math
                avg = total / 3 
                rank = 0 
                stuList.append({'no':no, 'name':name, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank})
                print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
                print()
                stuNum +=1 

# 학생성적출력 
def stu_output():
        print()
        print("-"*25, end="")
        print("[ 학생성적입력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in stuList:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
        print()