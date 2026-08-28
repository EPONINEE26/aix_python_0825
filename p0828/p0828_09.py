# 반복문 (for, while)
# print(1) 
# print(1) 
# print(1) 
# print(1) 
# print(1) 

# # for i(변수) in 범위:
# for i in range(10): # 10번 반복 
#     print(1)

# for i in range(5):
#     print(i)

# for i in range(5):
#     print(i*10)    

# for i in range(1,6):
#       print(i) 

# for i in range(0,10,2): # 시작점, 끝점, 간격
#       print(i)

# for i in [1,5,3,2]:
#       print(i)

# for i in "안녕하세요":
#       print(i)

# arr=list(range(1,11))
# print(arr)

# for i in range(10):
#     print("안녕")

# for _ in range(10): # under bar(_) 나 i 나 둘 중 하나 사용하면 됨. 
#     print("안녕") 

# for i in range(3):
#     print("번호:", i+1)
#     name=input("이름입력:")
#     print(name)

# print("1", end="\t") # end 입력 시 옆으로 출력 
# print("2", end="\t")
# print("3", end="\t")

# for i in range(3):
#      print(i+1, "번째")
#      no = i+1
#      name=input("이름입력:")
#      kor=int(input("국어점수 입력:"))
#      print("번호:", i+1, end="\t")
#      print("{}\t{}\t{}".format(no,name,kor)) 

# for i in range(3):
#     no=i+1
#     print(i=1,"번째")
#     name=input("이름입력:")
#     kor=int(input("국어점수 입력:"))
#     print("{}\t{}\t{}".format(no,name,kor))

# for i in range(3):
#     no=i+1
#     name=input("이름입력:")
#     kor=int(input("국어점수 입력:"))
#     print("{}\t{}\t{}".format(no,name,kor))

# for i in range(1,10):
#     print(f"2 x {i} = {2*1}") # 구구단 출력 


# sum=0
# for i in range(1,11):
#     print(i)
#     sum=sum+i
#     print(sum)
# print("합계:", sum)

# sum=0
# for i in range(1,101):
#     sum=sum+i
# print("합계:", sum)

# sum이 100이 넘어가는 i가 얼마일때?

# sum=0
# for i in range(1,100):
#     sum=sum+i
#     if sum>100:
#         print("100보다 클때:",i)
#         print("100초과될때 시점:",sum)
#         break
   
# sum=0
# for i in range(1,100):
#     sum=sum+i
#     if sum>100:
#         print("100보다 클때:",i-1)
#         print("100초과될때 시점:",sum-1)
#         break
      
# sum=0
# for i in range(1,10):
#     sum=sum+i
#     if sum>100:
#         print("100보다 크기 바로 앞일때:",i-1)
#         print("100 초과전 시점:",sum-1)
        # break

# for i in range(1,10):
#     print(f"2x{i}={2*i}")

# for i in range(1,10):
#     print("2 x {i}={}".format(i,i*2))

# for i in range(2,10): # 구구단 생성 
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j, i*j))

# for i in range(1,4): 
#     for j in range(1,4): # i 한번돌때 j는 3번 돈다 
#        print(i,j)

# for i in range(1,4): 
#     for j in range(1,10): # i 한번돌때 j는 10번 돈다 
#        print(i,j)

# for i in range(0,10): 
#      for j in range(0,10): 
#          for k in range(0,10):
#               print(i,j,k)
      
# for i in range(0,10): # 1차 방정식 
#       for j in range(0,10):  
#           print((i*10), j+1,":",i,j)

# 001 로 시작되는 번호표 

# for i in range(0,10): 
#        for j in range(0,10):  
#            for k in range(0,10):
#                 print("[번호표]")
#                 print("{}{}{}".format(j,j,k)) 
 
 
 
 
stu=[]
for i in range(2):
    no=i+1
    name=input("이름입력:")
    kor=int(input("국어점수 입력:"))
    stu.append([no,name,kor]) 
for i in range(2):
    print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))
    


         