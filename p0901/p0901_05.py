# 전개 연산잔
# 리스트의 장점 : 리스트 하나에 들어있는 모든 정보를 다 전달 가능 (리스트 안에 1억개가 있다면 한번을 보내도 정보 1억개를 보낼 수 있음)
# arr=[1,2,3,4,5] 
# print(arr)
# print(*arr) # 리스트 내에서 꺼내서 하나하나씩 출력하겠다는 의미 

# arr2=[]
# a=1
# a2=0

# a2=a
# print(a2)

# a=100
# print(a2) # 1로 출력 / a가 변해도 a2는 변하지 않음. 
# 리스트에는 주소값이 저장됨. 주소값을 찾아 보여지는 변수를 출력 
# 변수가 2개 이상일 경우 문제가 발생 

# arr=[1,2,3,4,5]
# arr2=[]
# arr3=[]

# arr[2]=1000
# arr3=[*arr] # 복사하는 방법 
# # arr3=[1,2,3,4,5]
# print(arr)
# print(arr2)
# print(arr3)

# arr=[1,2,3,4,5]
# arr2=[]
# arr3=[]
# arr2=arr # 앝은 복사 - 2개의 리스트 상관관계 있음 
# arr3=[*arr] # 깊은 복수 - 2개의 리스트 상관관계 없음 

# # 2번째 
# print(arr)
# print(arr2)
# print(arr3)
# print("-"*50)

# arr[2] = 5000
# print(arr)
# print(arr2)
# print(arr3)
# print("-"*50)

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
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
#     format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))

# print("-"*60)

