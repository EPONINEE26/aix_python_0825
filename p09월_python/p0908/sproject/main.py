# import student 

# stuList = []

# # student -> Student 클래스
# # 홍길동성적 -> stuList.append(s1)
# # 유관순성적 -> stuList.append(s2)

# s1 = student.Student(1,"홍길동",100,100,100)
# s2 = student.Student(2,"유관순",100,100,100)

# stuList.append(s1)
# stuList.append(s2)

# for s in stuList:
#     s.print()


from student import Student
from students import Students 

stu = Students() 

s1 = Student(1,"홍길동",100,100,99)
s2 = Student(2,"유관순",90,90,91)

stu.add(s1) 
stu.add(s2) 

for s in stu.slist:
    print(s)

