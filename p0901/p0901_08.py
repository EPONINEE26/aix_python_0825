# aa=[]
# bb=[]
# value=0
# for i in range(0,100):
#     aa.append(value)
#     value+=2 
# print(aa)

# for i in range(0,100):
#     bb.append(aa[99-1]) # 역순으로 들어감 
# print(bb)

# cc=list(range(0,200,2))
# print(cc)

# dd=[i+2 for i in range(0,200,2)] # 2부터 시작함 (i+2 로 시작하기에) 리스트 내포 
# print(dd)

# dd=[i+2 for i in range(-2,198,2)] 
# print(dd)

# dd=[i for i in range(0,200,2)] 
# print(dd)

# aa=[10,20,30]
# print(aa*3)

# aa=[10,20,30]
# bb=[1,2,3]
# print(aa+bb) # extend와 동일 aa와 bb가 값이 변경이 안 됨

# aa.extend(bb) # aa의 값이 변경됨. 
# print(aa)

# 리스트 함수 중 append, extend, insert, pop, del 함수인 경우 값이 변경됨. 원본 수정 

# a=1
# b=2
# print(a+b)

# aa=[1,2,3,4,5,6,7]
# print(aa[::-1])
# print(aa[::-2])

# aa=[10,20,30]
# aa[1]=200
# print(aa)

# aa=[10,20,30]
# aa[1:2]=[200,300]
# print(aa) # 2의 앞에 숫자 추가 


# stu_list=[ 
#     [1, "홍길동", 100, 100, 100, 300, 100, 0],
#     [2, "유관순", 100, 100, 100, 300, 100, 0],
#     [3, "이순신", 100, 100, 100, 300, 100, 0],
# ]

# stu_list[0][1] = "홍길자" # 이름 수정 
# print(stu_list) '
# print(stu_list[0][2],stu_list[0][2],stu_list[0][2])


stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]

# 유관순 국어점수를 100점으로 영어점수를 70점으로 수정하여 출력하시오. 점수 수정 위치 값을 입력하여 바로 수정 
stu_list[1][2]=100
stu_list[1][3]=70
print(stu_list) 

# 합계 및 평균 수정 
stu_list[1][2]=100
stu_list[1][3]=50
stu_list[1][5]=stu_list[1][2]+stu_list[1][3]+stu_list[1][4]
stu_list[1][6]=stu_list[1][5]/3
print(stu_list) 










