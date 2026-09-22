# print("[학생 성적 프로그램]")

# s1=[0,0,0,0,0,0,0]
# s1[0]=input("번호 입력:")
# s1[1]=input("이름 입력:")
# s1[2]=int(input("국어점수 입력:"))
# s1[3]=int(input("영어점수 입력:"))
# s1[4]=int(input("수학점수 입력"))
# s1[5]=s1[2]+s1[3]+s1[4]
# s1[6]=s1[5]/3


# s2=[0,0,0,0,0,0,0]
# s2[0]=input("번호 입력:")
# s2[1]=input("이름 입력:")
# s2[2]=int(input("국어점수 입력:"))
# s2[3]=int(input("영어점수 입력:"))
# s2[4]=int(input("수학점수 입력"))
# s2[5]=s2[2]+s2[3]+s2[4]
# s2[6]=s2[5]/3

# print("-"*60)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)
# print(f"{s1[0]}\t{s1[1]}\t{s1[2]}\t{s1[3]}\t{s1[4]}\t{s1[5]}\t{s1[6]:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}:2f".format(s1[0],s1[1],s1[2],s1[3],s1[4],s1[5],s1[6]))
# print("-" * 60)
# print(f"{s2[0]}\t{s2[1]}\t{s2[2]}\t{s2[3]}\t{s2[4]}\t{s2[5]}\t{s2[6]:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}:.2f".format(s2[0],s2[1],s2[2],s2[3],s2[4],s2[5],s2[6]))
# print("-" * 60)

# no=[]
# name=[]
# kor=[]
# eng=[]
# math=[]
# total=[]
# avg=[]
# for i in range(3):
#      no.append(input("번호 입력:"))
#      name.append(input("이름 입력:"))
#      kor.append(int(input("국어점수 입력:")))
#      eng.append(int(input("영어점수 입력")))
#      math.append(int(input("수학점수 입력:")))
#      total.append(int(kor[i] + eng[i] + math[i]))
#      avg.append(int(total[i] / 3))
# for i in range(3):
#      print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(no[i],name[i],kor[i],eng[i],math[i],total[i],avg[i]))

# stu=[]
# for i in range(3):
#     no=i+1
#     name=input("이름 입력:")
#     kor=int(input("국어점수 입력:"))
#     stu.append([no, name, kor])
# for i in range(3):
#     print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))

# 구구단을 출력하시오
# for i in range(2,10):
#     print("[{}]단]".format(i))
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j), end="\t")
#     print()# 

# for i in range(2, 10):
# #     print("[{}]단]".format(i))
# #     for j in range(1, 10):
# #         print("{}x{}={}".format(i,j,i*j), end="\t")
# #     print()

# for i in range(2,10):
#     print(f"[{i}단]",end="\t")
# print()
# for i in range(1,10):
#     for j in range(2,10):
#         print("{}X{}={}".format(j,i,i*j),end="\t") # i,j 자리변경을로 출력이 바뀜
#     print()
1

# no=[]
# name=[]
# kor=[]
# eng=[]
# math=[]
# total=[]
# avg=[]

# for i in range(3):
#     no.append(input("번호 입력:"))
#     name.append(input("이름 입력:"))
#     k_input=int(input("국어점수 입력:"))
#     kor.append(k_input)
#     e_input=int(input("영어점수 입력:"))
#     eng.append(e_input)
#     m_input = int(input("수학점수 입력:"))  
#     math.append(m_input)  
#     total.append(k_input + e_input + m_input)
#     avg.append(k_input + e_input + m_input)

# print("[학생 성적 프로그램]")   
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# for i in range(3):
#     print(f"{no[i]}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\t{total[i]}\t{avg[i]:2f}")


# import random
# number=[15,40,23,1,9,33,52]
# lotto=random.sample(range(1,46),6)
# print("확인로또 >> ", lotto)

# myNum=[]
# count=0
# answer=[]
# i=0

# for i in range(6):
#     no=int(input("숫자입력 : "))
#     myNum.append(no)

# for n in myNum: 
#     if n in lotto:
#         count=count+1
#         answer.append(n)

# print("로또번호 : ", lotto)
# print("입력한 번호 : ", myNum)
# print("정답번호 : ", answer)
# print("정답개수 : ", count)


# for step in range(2,10,3):
#     for i in range(step, min(step + 3,10)):
#         print(f"[{i}단]",end="\t")
#     print()
#     for i in range(1,10):
#         for j in range(step, min(step +3, 10)):
#             print("{}X{}={}".format(j,i,i*j),end="\t") # i,j 자리변경을로 출력이 바뀜
#         print()

#     print()

