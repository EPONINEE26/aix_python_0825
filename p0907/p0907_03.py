# common 폴더 안에 stu.txt로 파일을 저장하시오.

# import os 

with open("common/stu.txt","a",encoding="utf-8") as f:
    allStr = ""
    no = 0 
    while True: 
        outStr = input("내용입력 : ")
        if no == 0: 
            allStr = outStr
            no += 1 
            continue
        if outStr == "":
            f.write(allStr+"\n")
            break
        allStr += ","+outStr
        no += 1 
    print(allStr)





