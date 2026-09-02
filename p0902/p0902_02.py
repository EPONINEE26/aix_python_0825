# 리스트 : 한 개의 파일에 여러 개의 변수를 저장 대괄호 
# 딕셔너리 : key와 values 로 이루어짐 중괄호 

# alist=[1,2,3]
# alist2=[]
# alist2=alist # 앝은 복사. 원본에 영향이 있음 
# print(alist2) # 1,2,3

# alist=[1,2,3]
# alist[0]=100
# alist2=[]
# alist2=alist
# print(alist2)

# a=10
# a2=0
# a2=a
# print(a2)

# a=100
# print(a2) # a 값을 변경했다고 a2는 변경이 안 됨. 

# alist=[1,2,3]
# alist2=[]
# alist2=[*alist] # 깊은 복사. 원본에 영향이 없기에 복사를 할 경우 이 함수로 진행해야함 
# print(alist2) # 1,2,3 

# # 주소값만 저장이 되어지기에 그 주소값에 있는 변수를 출력함 
# # 일률적으로 출력이 됨 


# alist=[1,2,3]
# alist2=[]
# alist2=alist.copy() 
# print(alist2)

# aa=["바나나", "딸기", "사과", "딸기", "딸기", "사과"]
# print(aa.count("딸기")) # 변수의 개수를 알수 있음 

# for i in aa:
#     print(aa)

# 딕셔너리
# a_dic = {"바나나":1, "띨기":3, "사과":2}
# print(a_dic["바나나"]) # 출력방벙 

# a_dic = {"바나나":1, "띨기":3, "사과":2}
# a_dic={"배":5} # 추가 
# print(a_dic)

# a_dic = {"바나나":1, "띨기":3, "사과":2}
# del a_dic["바나나"] # 삭제 
# print(a_dic)

# a_dic = {"바나나":1, "띨기":3, "사과":2}
# a_dic["사과"]=100 # 수정
# print(a_dic)


# aa=["바나나", "딸기", "사과", "딸기", "딸기", "사과"]
# # {"바나나":1, "띨기":3, "사과":2} 로 출력하시오.
# aa_dic ={}
# for a in aa:
#     aa_dic[a]=0

# print(aa_dic)


# aa=["바나나", "딸기", "사과", "딸기", "딸기", "사과"]
# # {"바나나":1, "띨기":3, "사과":2} 로 출력하시오.
# aa_dic ={}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a]=0
#     else:
#         print("있습니다.")
# print(aa_dic)

# aa=["바나나", "딸기", "사과", "딸기", "딸기", "사과"] # 리스트 안 중복된 변수가 몇 개인지 확인하는 방법 
# # {"바나나":1, "띨기":3, "사과":2} 로 출력하시오.
# aa_dic ={}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a]=1
#     else:
#         aa_dic[a]=aa_dic[a]+1
#         print("있습니다.")
# print(aa_dic)

# aa=[1,2,3,1,1,1,2,3,1,1,1,2,2,3] 
# aa_dic ={}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a]=1
#     else:
#         aa_dic[a]=aa_dic[a]+1
#         print("있습니다.")
# print(aa_dic)

# 리스트는 주소로 처리 / 딕셔너리는 key값으로 처리 
# pop 은 주소값을 입력하지 않을 경우 맨 뒤 값이 삭제됨 

# studen1['이름'] 없는 값이 있을 경우 에러 
# student1.get('이름') 없는 값을 입력하면 None 이 출력 

# sorted(dictionary.items(), key=lambda x:x[1])

# 리스트 생성 방법 
# a1=[1,2,3,4,5]
# a2=[0]*5
# a3=list(range(1,6))
# a4=[i for i in range(1,6)]
# a5=[i for i in range(1,6) if i%2==0] # 2의 배수만 출력하라는 방법 (리스트 내포)
# a6=[i*i+2 for i in range(1,6)] 

# zip 함수 : 동시에 여러 개 리스트에 접근하여 합침 

# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# c=[]

# for i in range(len(a)):
#     c.append([a[i], b[i]])
# print(c)

# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# c=[]

# for i,j in zip(a,b): # 두 개 및 여러 개 돌릴때 zip 사용 
#     c.append([i,j])    
# print(c)

# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# c=[]

# c=list(zip(a,b)) # 두 개 및 여러 개 돌릴때 zip 사용 
# print(c)

# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# c=[]

# c=list(zip(a,b)) 
# dic=dict(zip(a,b)) # a가 key 값이 되고 b가 valuse 값이 됨 
# print(c)

# 대괄호로 되어있음 수정이 가능하나 소괄호로 되어있음 수정이 불가
# 튜플 소괄호로 구성 

# FIFO (first In, first Out) / LIFO (Last In, First Out)
# Stack : 한 쪽 끝이 막혀 먼저 들어간 것이 가장 나중에 나오는 형태의 구조 

# result=sorted(students, key=itemgetter('age'))

aa = "가나다라가가가나나다라라라라라라라"
# {가:10, 나:5, 디:11....} 이런식으로 나오게 출력하시오.

# aa_dic ={}
# for a in aa:
#     aa_dic[a]=0
# print(aa_dic)

# aa_dic ={}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a]=1
#     else:
#         aa_dic[a]=aa_dic[a]+1
# print(aa_dic)

# aa="a/b/c/d/f/g" 
# # 리스트 타입으로 변경하시오.
# aa_list=aa.split("/")
# print(aa_list)

# bb="100, 10,5,4,1"
# 모든 수의 합을 구하시오.

# bb_list=bb.split(",") # 문자열을 나누어서 리스트로 변경
# print(bb_list)

# bb="100, 10,5,4,1"
# bb_list=bb.split(",")
# bb_list2=[int(i) for i in bb_list] # int로 변경하여 리스트에 들어감 
# sum=0
# for b in bb_list:
#     sum = sum += b
# print(bb_list)
# print("합계 : ", sum)


ss="파이썬 공부!!! 열심히 합시다. 파이썬" 
# print (ss.count("공부")) 
# print (ss.count("파이썬")) 

# print (ss.find("공부")) 
# print (ss.find("파이썬")) 
# print (ss.find("자바")) # find는 없을 때 -1 
# print (ss.index("자바")) # index 는 없을 때 에러 

# print(ss.startwith("파이썬"))
# print(ss.startwith("파이썬", 10))
# print(ss.endwith('^^'))

# aa=input("이름을 입력하세요.>>")
# print(aa.split(","))

# 1. 앞뒤공백제거 - strip()
# a="      abc     "
# print(a)
# print(a.strip()) # 공백제거 -> a값은 반연은 안됨. 그러나 글자 사이의 공백은 처리 안 됨. 글자 사이는 replace로 변환 

# 2. 중간공백제거 - replace 
# aa = "[1,2,  3, 4,5]"
# aa = aa.replace(" ", "")
# print(aa.split(","))

# aa = "[1,2,  3, 4,5]"
# print(aa.replace(" ",""))

# 3. 분리 - split - 리스트타입으로 전달됨 
# aa="딸기, 수박, 바나나, 사과"
# print(aa)
# print(aa.split(","))
# print(aa.split("/"))

# ss="    파이썬"
# ss2="<<<<파<<이<썬"
# print(ss.strip())
# print(ss2.replace("<", "")) 

# 4. join
# aa="/"
# bb=aa.join(["바나나", "딸기", "사과"])
# print(bb)
# print(type(bb))

# d="1, 홍길동, 100, 100, 100, 300, 100.0"
# dlist=d.split(",")
# dlist[2]=90 
# print(dlist)

# 문자열을 숫자타입으로 변경 
# d="1, 홍길동, 100, 100, 100, 300, 100.0" 
# dlist=d.split(",")
# dlist[2]=90 
# dlist[3]=int(dlist[3])
# dlist[4]=int(dlist[4])
# dlist[5]=int(dlist[2]+dlist[3]+dlist[4])
# dlist[6]=int(dlist[5]/3)
# print(dlist)

# 특정문자로 결합 - join
# 문자열 리스트만 변경 가능 join (결합)
# test=["1","2", "3"]
# d_str=",".join(dlist) # 에러 명령문 
# print(d_str)

# d="1, 홍길동, 100, 100, 100, 300, 100.0" 
# dlist=d.split(",")
# dlist[2]=90 
# dlist[3]=int(dlist[3])
# dlist[4]=int(dlist[4])
# dlist[5]=int(dlist[2]+dlist[3]+dlist[4])
# dlist[6]=int(dlist[5]/3)

# dlist2=[str(i) for i in dlist]
# print(dlist)

# test=["1","2", "3"]
# d_str=",".join(dlist2) 
# print(d_str)

# 5. count : 문자열 안에 해당문자가 몇 개 있는지 확인
# 6. find : 문자열 안에 해당문자 위치 변환, 없으면 -1
# 7. index : find와 동일, 없으면 에러 












