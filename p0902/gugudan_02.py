def gugudan_func():
for step in range(2,10,3):
    for i in range(step, min(step + 3,10)):
        print(f"[{i}단]",end="\t")
    print()
    for i in range(1,10):
        for j in range(step, min(step +3, 10)):
            print("{}X{}={}".format(j,i,i*j),end="\t") # i,j 자리변경을로 출력이 바뀜
        print()

    print()