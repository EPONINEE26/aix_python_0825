def stu_print(): 
    for s in stu:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
stu=[ 
    [1,"홍길동",100,100,100,300,100.0],
    [2,"유관순",100,100,100,300,100.0],
    [3,"이순신",100,100,100,300,100.0],
]

while True:
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")

    choice = int(input("원하는 번호를 입력하세요.>>"))
    if choice == 1:
        name=input("학생이름입력 (0. 이전페이지 이동):")
        if name=="0": break
        
        # 학생전체출력 
        stu_print()
    elif choice == 2:
        # 학생출력하는 구문 
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        # 학생전체출력
        stu_print()
    else: 
        name = input("이름을 입력하세요.")
        # 학생전체출력 
        stu_print() 



def stu_print(): 
    for s in stu:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
# 1. 기본 데이터를 100점으로 채워둡니다.
stu = [ 
    [1, "홍길동", 100, 100, 100, 300, 100.0],
    [2, "유관순", 100, 100, 100, 300, 100.0],
    [3, "이순신", 100, 100, 100, 300, 100.0],
]

# 2. 키보드로 새 점수를 입력받아 일괄 수정 및 자동 계산합니다.
for s in stu:
    print(f"\n=== {s[1]} 학생의 새로운 점수 입력 ===")
    
    # 100점이었던 자리에 사용자가 입력한 새로운 숫자가 덮어씌워집니다.
    s[2] = int(input("변경할 국어 점수: "))
    s[3] = int(input("변경할 영어 점수: "))
    s[4] = int(input("변경할 수학 점수: "))
    
    # 새 점수를 기준으로 총점과 평균을 계산합니다.
    s[5] = s[2] + s[3] + s[4]
    s[6] = s[5] / 3

# 3. 최종 결과 출력
print("\n================ 수정 완료된 성적표 ================")
for row in stu:
    print(row)

while True:
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")

    choice = int(input("원하는 번호를 입력하세요.>>"))
    if choice == 1:
        name=input("학생이름입력 (0. 이전페이지 이동):")
        if name=="0": break
        
        # 학생전체출력 
        stu_print()
    elif choice == 2:
        # 학생출력하는 구문 
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        # 학생전체출력
        stu_print()
    else: 
        name = input("이름을 입력하세요.")
        # 학생전체출력 
        stu_print() 



