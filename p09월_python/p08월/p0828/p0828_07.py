# format 함수
# a=10
# print("{}".format(a))
# print("{:10d}".format(a)) # 빈 공백 생성해서 만들어라 
# print("{:010d}".format(a)) # 빈 공백은 0으로 채워라 
# print("{:3d}".format(123456789)) 
# print("{:3,d}".format(123456789)) # 천단위 표시 
# print("{:.2f}".format(12.12345)) # 소수점제한 
# print("{:+010d}".format(a))  

# print("{:+010d}".format(-10))  # +: 숫자앞에 부호를 붙임 
# print("{:+010d}".format(-10)) # +: 숫자앞에 부호를 붙임 

# cc="aabbccddeeff"
# print(cc.upper())

# dd="AaBbCcDdEdFf"
# print(cc.lower())

#문자인지 아닌지 확인
# 이름을 입력을 받는데, 영문이름 입력 요청
# name=input("이름을 입력하세요.") # 특수문자 입력 시 에러 발생 
# print(name)

# isalpha 특부문자나 숫자인지 확인 가능 
# name=input("이름을 입력하세요.") 
# if name.isalpha():
#     print("문자 알파벳으로 되어 있습니다.")
# else:
#     print("특수문자나 숫자가 입력되었습니다.")
# print(name)


# num=input("숫자를 입력하세요.")
# if num.isdigit():
#    num = int(num)
#    num += 100 
#    print("입력숫자:", num)
# else:
#    print(num)

# name=input("이름입력:")
# kor=input("국어점수 입력:")
# if kor.isdigit():
#     kor=int(kor)
# else:
#     print("숫자가 아닙니다. 다시 입력해주세요.")
# print(name,kor)


# name=input("이름입력:")
# while(True):
#      kor=input("국어점수 입력:")
#      if kor.isdigit():
#           kor=int(kor)
#           break
# else:
#      print("숫자가 아닙니다. 다시 입력해주세요.")
# print(name,kor)

# print("[로그인페이지]")
# while(True):
#     id=input("아이디입력:")
#     pw=input("패스워드입력:")
#     if id=="aaa" and pw=="1111":
#         print("로그인성공!! 메인페이지로 이동합니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인해주세요.")

# print("메인페이지가 열립니다")

# paper = """네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 \
# 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
# 이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 \
# 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다. 
# """

# result=paper.find("홍수")
# print(result)

# find(검색내용, 시작위치, 종료위치)
# result2=paper.find("홍수",5) # 5번째 부터 다시 찾아줘 라는 명령문 
# print(result2)

# result3=paper.find("홍수",40) 
# print(result3)

# result4=paper.find("홍수",126) #-1 이 나오면 찾는 글자가 없을 때 
# print(result4)

# result2=paper.rfind("홍수")
# print(result2)

# result3=paper.count("홍수")
# print(result3)

# 홍수 라는 글자가 어디어디에 있는지 위치점을 알고 싶어요 반복문이나 find로 찾을 수 있음 

# paper = """네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 \ 
# 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
# 이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 \
# 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다. 
# """

# # split() 구분자로 분리
# str1 = "1,홍길동,100,100,99"
# s = str1.split(",")
# print(s)    # 리스트-문자열
# print(s[4]) # 타입:문자열

# in 함수
# paper = "네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
#       2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
#       이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
#           비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."

# if "코치" in paper:
#     print("있음")
# else:
#     print("없음")

# alist = ["딸기","포도","바나나"]
# if "포도" in alist:
#     print("있음")
# else:
#     print("없음")


# str1 = "1,홍길동,100,100,99"
# s=str1.split(",") # 
# s=[0,0,0,0,0,0,0] # 리스트에 입력함 
# s[0]=input("번호입력:")
# s[1]=input("이름입력:")
# s[2]=int(input("국어점수 입력:"))
# s[3]=int(input("영어점수 입력:"))
# s[4]=int(input("수학점수 입력:"))
# s[5]=s[2]+s[3]+s[4]
# s.append(s[2]+s[3]+s[4]) 
# s.append(s[5]/3) # s[6]=s[5]/3
# print("-"*60)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평권")
# print("-"*60)
# print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")
# print(f"{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s)) 
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]))
# print("-"*60)

# 구조 분해 할당 라스트를 분리해서 출력함 
# a=[1,2,3,4,5]
# print(a)
# print(*a)
# print(a[0],a[1],a[2],a[3],a[4])

# f 함수안에는 모든 함수가 포함 가능 
# "{}'.format (*data)



