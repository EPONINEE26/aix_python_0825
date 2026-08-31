# 입력한 숫자와 랜덤숫자와 몇 개가 맞는지 개수를 출력하시오

# ranNo=[1,5,9,7,4]
# inputNo=2
# i=0

# if inputNo in ranNo:
#     print("있음")
# else:
#     print("없음")
        
# ranNo=[1,5,9,7,4]
# inputNo=1
# count=0 

# if inputNo in ranNo:
#     count = count+1
#     print("있음")
# else:
#     print("없음")

# ranNo=[1,5,9,7,4]
# inputNo=[1,2,3,4]
# count=0 

# for i in inputNo:
#     if i in ranNo:
#         count = count+1
#         print("있음")
# else:
#     print("없음")

# print("개수 : ", count)

# ranNo=[1,5,9,7,4]
# inputNo=[1,2,3,4]
# count=0 
# answerNo=[]

# for i in inputNo:
#     if i in ranNo:
#         count = count+1
#         answerNo.append[i]
#         print("있음")
# else:
#     print("없음")

# print("개수 : ", count)

# # 입력한 숫자를 모두 저장해서 프로그램을 종료할 때 출력하시오. 
# import random
# noArr=[10.40,2,9,5]
# no=[]
# while True:
#     i_no=int(input("숫자입력 : "))
#     no.append (i_no)

#     if i_no==0: 
#         break 
#     # 0을 입력할 때 종료 


# # 종료할 때 입력된 숫자 모두 출력 
# print("입력숫자 : ", no)

import random
noArr=[10.40,2,9,5]
no=[]
i=0
count=0
answer=0
while True:
    i_no=int(input("숫자입력 : "))
    no.append (i_no)

    if i_no==0: 
        break 
    # 0을 입력할 때 종료 
for i in no:
    if i in noArr:
        count=count+1
        answer.append(i) # 입력 숫자가 정답일 때 i 값을 입력


# 종료할 때 입력된 숫자 모두 출력 
print("리스트 : ", noArr)
print("입력숫자 : ", no)
print("정답숫자 : ", answer)
print("정답개수 : ", count)





