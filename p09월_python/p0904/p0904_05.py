# tex2.txt파일을 읽어와서 
# stu = []
# 데이터를 리스트에 저장하시오. 

stu=[]
# with : f.close() 생략 가능 
# opem : f.close() 무조건 꼭 써야함 
with = open("C:/aaa/text2.txt", "r", encoding="utf-8") # with를 사용할 경우 .close()를 안 써도 됨 

while True:
    line = f.readline()
    if line == "" : break
    line = line.sprip()
    arr = line.split(",")

    for i, a in enumerate(arr):
        if 5 > i >= 2:
            arr[i] = int(a)
        elif i == 6:
            arr[i] = float(a)

        stu.append({'no': arr[0], 'name': arr[1], 'kor': arr[2], 'eng': arr[3], 'math': arr[4], 'total': arr[5], 'avg': arr[6]:.2f})
print(stu)

