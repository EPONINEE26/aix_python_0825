# import students # 같은 폴더 내에서는 import 로 불러올 수 있지만, 다른 폴더에 있는 파일은 from으로 불러와야함 
# 다른 폴더에 있는 파일 불러올때 from import 사용 from 폴더명 import 파일명 
from project import students 
from project import student 

stus = students.Students() # 파일명을 무조건 앞에 붙이고 점(.)을 찍어야함 
# stus.slits = [] 와 동일한 의미 
print(len(stus.slist))

s1 = student.Student(1,"홍길동",100,100,99)
stus.add(s1) # stus.slits = [s1] 과 동일한 의미 
stus.add(student.Student(2,"유관순",90,90,91))
stus.print()

# print(s1)

# print(stus)