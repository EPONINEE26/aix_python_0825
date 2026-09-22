# # 파일 쓰기 (w 명령어) 
# with open("c:/aaa/abc.txt","w",encoding="utf-8") as f: # 파일 덮어쓰기 
#     while True:
#         line = input("글을 입력하세요. >> ")
#         if line !="":
#             f.writelines(line+"\r\n")  #\r:문장끝으로, \n:줄바꿈
#         else:
#             break

# print("파일이 저장되었습니다.")



with open("c:/aaa/abc.txt","a",encoding="utf-8") as f: # 파일 이어쓰기 
    while True:
        line = input("글을 입력하세요. >> ")
        if line !="":
            f.writelines(line+"\r\n")  #\r:문장끝으로, \n:줄바꿈
        else:
            break

print("파일이 저장되었습니다.")



