# 딕셔너리 : key:value 로 이루어짐 (문자도 올수 있고, 숫자도 올수 있지만, 대부분 문자로 옴)
# 딕셔너리의 장점 : 데이터를 확인하기 쉽다, 
# dic={a:1,b:2,c:3} # 이런 식으로 문자가 key 값에는 문자로 옴

# stu={"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "music":100}
# stu_arr=[1,"홍길동", 100, 100, 100]

# # 딕셔너리 추가 : 없는 키 값 입력 
# stu["total"]=400 
# print(stu)

# # 딕셔너리 수정 : 있는 키 값에 값을 넣으면 수정됨 
# stu["kor"]=50
# stu["total"]=stu["kor"]+stu["eng"]+stu["math"]
# print(stu)

# 딕셔너리 삭제 : 
# del(stu["eng"])
# print(stu)

# stu_list = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
# ]

# print(stu_list[0]['no'])
# print(stu_list[0]['name']) = "홀길자" # 있는 키 입력은 수정 
# print(stu_list[0]['kor'])
# print(stu_list[0]['eng'])
# print(stu_list[0]['math'])
# print(stu_list[0]['total'])
# print(stu_list[0]['avg'])
# stu_list[0]['rank']=1 # 없는 키 입력은 추가 student.get('주소) student1['주소'] get으로 할 경우 에러가 안 남. 

# stu={"no":1, "name":"홍길동", "total":100}
# print(stu.keys())

# {"no":1, "name":"홍길동", "total":100}
# print(stu.values())


# stu={"no":1, "name":"홍길동", "total":100}
# print(stu.keys())
# print(stu.values())
# s_list=list(stu.values())
# print(s_list) # 리스트로 변환된 것

# stu={"no":1, "name":"홍길동", "total":100}
# # print(stu.items()) 

# # dict 형태로 나오려면 딕셔너리를 리스트로 변환해야 dict로 출력됨 

# for i,v in stu.items():
#     print(i,v)

# name_dic={
#     "aaa":"토마토", "ddd":"바나나", "eee":"딸기", "bbb":"배"
# }

# import operator # 예전 방법 최근엔 잘 안 씀 
# name_sort1=[]
# name_sort1=sorted(name_dic.items(), key=lambda  x:x[0]) 
# name_sort1=sorted(name_dic.items(), key=lambda  x:x[0], reverse=True) 
# print(name_sort1)

# name_dic = {
#     "aaa":'토마토',"ddd":"바나나","eee":"딸기","bbb":"배"
# }

# import operator
# name_sort1 = []
# name_sort1 = sorted(name_dic.items(),key=operator.itemgetter(0))


# engs = {
#     "car":"자동차",
#     "color":"색상",
#     "pig":"돼지",
#     "love":"사랑",
#     "phone":"전화기"
# }

# for k, v in engs.items():
#     print(k,v)
    
# engs = {
#     "car":"자동차",
#     "color":"색상",
#     "pig":"돼지",
#     "love":"사랑",
#     "phone":"전화기"
# }

# for k, v in engs.items():
#     print(k,"는(은) 한국어로 무엇일까요?")
#     answer=input("정답 : ")

# engs = {
#     "car":"자동차",
#     "color":"색상",
#     "pig":"돼지",
#     "love":"사랑",
#     "phone":"전화기"
# }

# for k, v in engs.items():
#     print(k,"는(은) 한국어로 무엇일까요?")
#     answer=input("정답 : ")
#     if answer== v:
#         print("[정답입니다. ^^]")
#     else:
#         print("[오답입니다. TT]")

# 세트는 중복된 정보는 하나만 출력 중복 없음 순서가 없음 
# 세트는 읽기 나 출력만 한다

# & 교집합
# ! 합집합
# - 차집합

# 리스트 생성 방법 
# alist=[i for i in range(1,10)] 
# print(alist)
# alist2=list(range(1,10))
# print(alist2)
# alist3=[0]*10 
# print(alist3)
# alist4=[1,2,3,4,5,6,7,8,9,]
# print(alist4)

# alist=list(range(1,21)) # c, c++ jave, 파이썬 다 사용 가능 
# nlist=[]
# for a in alist:
#     if a%3==0:nlist.append(a)

# print(nlist)

# a=[n for n in range(1,21) if n%3==0] # 이 방법은 파이썬에서만 사용 
# print(a)



