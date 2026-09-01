# number=[1,2,3,4,5,6,7,8,9,10,11,12,13] # 비교가 가능하니 숫자로 입력. (숫자와 문자는 비교가 안 됨)
# shape=["SPADE","HEART","DIANOND","CLOVER"]

# #SPADE, 1
# #SPADE, 2
# #....
# # CLOVER,13....

# for s in shape:
#     for n in number:
#         print("{},{}".format(s,n))

# number=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] # J, Q, K 로 출력 
# shape=["SPADE","HEART","DIANOND","CLOVER"]
# for s in shape:
#     for n in number:
#         print("{},{}".format(s,n))

# n_shape=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] # J, Q, K 로 출력 
# number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# shape=["SPADE","HEART","DIANOND","CLOVER"]

# for s in shape:
#     for n in number:
        
#         print("{},{}".format(s,n_shape[n-1]))

import random
n_shape=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] # J, Q, K 로 출력 
number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
shape=["SPADE","HEART","DIANOND","CLOVER"]

# [["SPADE",1]],[["SPADE,2"]]
# card=[] 
# # card 리스트 개수 : 52개의 리스트를 생성하시오.
# for s in shape:
#     for n in number:
#         card.append([s,n]) 
# print(card)

# card=[] 
# card.append([s,n]) 
# for s in shape:
#     for n in number:
#         card.append([s,n]) 
# random.shuffle(card)
# print(card)

# 숫자형-정수타입, 실수타입, 문자열타입, 불타입 
# 리스트, 딕셔너리, 튜플, 세트 

# aa=[1,2,3,4,5] # 리스트 대괄호 aa[0] 
# aa2=(1,2,3,4,5) # 튜플 - 수정이 안 됨. 소괄호 aa2[0] 
# aa3={key:value} # 딕셔너리 중괄호 



