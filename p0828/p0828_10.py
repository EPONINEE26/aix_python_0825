# 반복문을 사용해서 1~10까지 있는 합을 출력하시오.
sum = 0
for i in range(1, 11):
    print(i)
    sum = sum + i
    print(sum)

print("합계:", sum)

# 200을 넘는 시점의 i의 값과 i번째의 합계를 출력하시오. 
sum = 0
for i in range(1, 200):
    sum = sum + i
    if sum > 200:
        print("200보다 큰수:", i)
        break  # 최초의 숫자만 출력하고 반복문을 바로 종료합니다.
  
print("합계:", sum)


# 200을 넘는 이전 시점의 i, 합계를 출력하시오.
sum = 0
for i in range(1, 200):
    sum = sum + i
    if sum > 200:
        print("200보다 크기 바로 앞일때:", i - 1)
        print("200 초과전 시점:", sum - i)
        break  # 이 명령어가 있어야 모든 숫자가 나오지 않고 여기서 딱 멈춥니다!
print(sum)


# 구구단을 출력하시오.
for i in range(2,10):
    for j in range(1,10):
        print("{}x{}={}".format(i,j, i*j))


name=[]
kor=[]
for i in range(2):
    name.append(input("이름입력:"))
    kor.append(input("국어점수 입력:"))
for i in range(2):
    print("{}\t{}",format(name[1],kor[1]))

stu=[]
for i in range(2):
    no=i+1
    name=input("이름입력:")
    kor=int(input("국어점수 입력:"))
    stu.append([no,name,kor]) 
for i in range(2):
    print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))



