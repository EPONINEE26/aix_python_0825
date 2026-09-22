# 함수 
# def 함수 이름 ():
# 소괄호 뒤 바로 : 부분이 꼭 와야함. 
# 함수를 쓰는 이유 : 반복적인 구문을 줄이기 위한 방법 

# def fun():
#     print("함수를 호출합니다.") # 함수 호출 방법 
# fun()
# fun()
# fun()

# 함수로 빼는 방법

# def cal(): 
#     num1=int(input("숫자입력 : "))
#     num2=int(input("숫자입력 : "))
#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)

# cal()
# cal()
# cal()

# 함수 사용 이유 : 긴 구문의 반복적인 명령어를 줄일 수 있고, 코드를 간결하게 하기 위해서 함수 사용. 한 번 지정해 놓으면 편리하다. 
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

  






























































