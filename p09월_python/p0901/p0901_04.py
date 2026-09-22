# 로또 맞추기 
# 학생성적 프로그램 
# 위의 2가지는 무조건 외우기 

# 학생 성적 입력 - 변수, 리스트-리스트, 리스트-딕셔너리 

# [1,2,3,4,5,6,7,8,9] 1차원 리스트 
# 리스트 생성 방법 - 직접 입력, [0]*9, list(range(1,10))
# [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # 리스트 안 리스트 (3차원 리스트)

# num_arr=list(range(1,10))
# print(num_arr) 
# all_arr=[]
# for i in num_arr:

# num_arr=list(range(1,10))
# print(num_arr) 
# all_arr=[]
# for i in range(0,9,3):
#     print(i)
#     all_arr.append(num_arr[i:i+3]) # 0,1,2 (주소값) - 0-2 번 주소값 출력 
#     all_arr.append(num_arr[i:i+3]) # 3,4,5 (주소값) - 3-5 번 주소값 출력 
#     all_arr.append(num_arr[i:i+3]) # 6,7,8 (주소값) - 6-8 번 주소값 출력 


# num_arr=list(range(1,10))
# print(num_arr) 
# all_arr=[]
# for i in range(0,9,3): # 0 ,3, 6 
#     print(i, end="  ") # 0 ,3, 6 
#     all_arr.append(num_arr[0:0+3]) # 0,1,2 (주소값) - 0-2 번 주소값 출력 
#     all_arr.append(num_arr[3:3+3]) # 3,4,5 (주소값) - 3-5 번 주소값 출력 
#     all_arr.append(num_arr[6:6+3]) # 6,7,8 (주소값) - 6-8 번 주소값 출력 

# 학생 성적 입력 
# stu_list=[ 
#     [1. "홍길동", 100, 100, 100, 300, 100, 0],
#     [2. "유관순", 100, 100, 100, 300, 100, 0],
#     [3. "이순신", 100, 100, 100, 300, 100, 0],
# ] 

# stu_list=[]
# stu_list.append([1, "홍길동", 100, 100, 100, 300, 100, 0])
# stu_list.append([2. "유관순", 100, 100, 100, 300, 100, 0])
# stu_list.append([3. "이순신", 100, 100, 100, 300, 100, 0])

# stu_list=[ 
#     [1, "홍길동", 100, 100, 100, 300, 100. 0],
#     [2. "유관순", 100, 100, 100, 300, 100. 0],
#     [3. "이순신", 100, 100, 100, 300, 100. 0],
# ] 

# stu_list=[]
# # stu_list.append([1, "홍길동", 100, 100, 100, 300, 100, 0])
# no=input("번호 입력:")
# name=input("이름 입력:")
# kor=int(input("국어점수 입력:"))
# eng=int(input("영어점수 입력:"))
# math=int(input("수학점수 입력:"))
# total=kor+eng+math
# avg=total/3
# stu_list.append([no,name,kor,eng,math,total,avg])

# stu_list=[]
# for i in range(3):
#     no=input("번호 입력:")
#     name=input("이름 입력:")
#     kor=int(input("국어점수 입력:"))
#     eng=int(input("영어점수 입력:"))
#     math=int(input("수학점수 입력:"))
#     total=kor+eng+math
#     avg=total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])

# print(stu_list)

# stu_list=[]
# while True: 
#     no=len(stu_list)+1 # 번호 자동 부여 나중에 중간 자료를 삭제할 경우 번호가 중복이 될 수 있기에 count 함수로 지정해서 처리하면 됨 
#     print("자동번호 : ", no) 
#     # no=input("번호 입력:")
#     name=input("이름 입력 (종료하려먼 0을 눌러라):")
#     if name=="0": break 
#     kor=int(input("국어점수 입력:"))
#     eng=int(input("영어점수 입력:"))
#     math=int(input("수학점수 입력:"))
#     total=kor+eng+math
#     avg=total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])

# print("입력된 학생 성적 : ", len(stu_list))
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)
# for s in stu_list:
#     print(s)
# print("-"*60)

# stu_list=[]
# while True: 
#     no=len(stu_list)+1 # 번호 자동 부여 나중에 중간 자료를 삭제할 경우 번호가 중복이 될 수 있기에 count 함수로 지정해서 처리하면 됨 
#     print("자동번호 : ", no) 
#     # no=input("번호 입력:")
#     name=input("이름 입력 (종료하려먼 0을 눌러라):")
#     if name=="0": break 
#     kor=int(input("국어점수 입력:"))
#     eng=int(input("영어점수 입력:"))
#     math=int(input("수학점수 입력:"))
#     total=kor+eng+math
#     avg=total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])

# print("입력된 학생 성적 : ", len(stu_list))
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)
# for s in stu_list:
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
# print("-"*60)


