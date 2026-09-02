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

a=[1,2,3,4,5]
b=[10,20,30,40,50]
c=[]

for i in a:
    for j in b: 






















