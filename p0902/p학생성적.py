# 학생성적
stu=[
    # {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100} # key값은 국어로 작성해도 되나 에러날 확률이 높음. 영어로 사용하는 것이 좋음 
    # {},
    # {}
    
]

# 화면 출력
# 1. 성적입력
# 2. 성적출력.... 이렇게 출력하게 만드시오.

c_no=1 # 학생번호로 사용 
while True: # 메인화면출력함수 
    print("[ 학생성적프로그램 ]") # tab 키 누르면 들여쓰기 가능 
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*60)
    choice=int(input("원하는 번호 입력하세요."))
    if choice == 1: # 학생성적입력함수 
        print()
        while True:
            print("[ 학생성적입력 ]")
            print("-"*60)
            no=c_no
            name=input("학생이름입력 (0. 이전페이지 이동):")
            if name=="0": break
            kor=int(input("국어점수입력:"))
            eng=int(input("영어점수입력:"))
            math=int(input("수학점수입력:"))
            total=kor+eng+math
            avg=total/3 
            stu.append(
                {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
            print(name,"학생 성적이 저장되었습니다.")
            c_no += 1 # 다음번호 1증가 
            print()
            
    elif choice == 2: # 학생성적출력함수 
            print()
            print("[ 학생성적출력 ]")
            print("-"*60)
            print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
            print("-"*60)
            for s in stu:
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
            print() 
















