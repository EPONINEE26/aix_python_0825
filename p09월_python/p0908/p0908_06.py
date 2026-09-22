class Student:
    # 생성자 (self 꼭 입력)
    def  __init__(self,no,name,kor,eng,math): # 객체선언시 바로 값 입력 (init)
        # print(no) # 20 출략 함수 내 정보를 먼저 출력하고 없을 경우 다른 곳에서 정보를 찾음 
        self.no = no # 함수 내 no로 인지하여 무한반복으로 출력함 
        # self.__no = no (캡슐화. 클래스 내부에서만 값을 수정 가능)
        # 캡슐화 시 값을 수정할 수 있도록 setter, getter를 만들어줌. 수정을 위해선 무조건 setter와 getter 만들어야함 
        self.no = no # self 를 사용할 경우 class 로 지정한 밖의 변수에 있는 no 값을 찾아 출력. 그렇기에 무조건 self 입력해야함. 
        self.name = name 
        self.kor = kor
        self.eng = eng
        self.math = math 
        self.total = kor+eng+math
        self.avg = self.total/3
        # self.rank = 0 

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"

    def cal_total(self):
        self.total = self.kor+self.eng+self.math

    def cal_avg(self):
        self.avg = self.total/3

# 객체선언을 하면
s1=Student(1,"홍길동",90,90,100) # s -> 3개의 변수가 생성됨. 
s2=Student(2,"유관순",100,100,99) 

# 출력 : 참조변수명.변수명 
print(s1.name)
# 수정 : 참조변수명.변수명 = 수정값 # 전체 수정은 안 하는 것이 좋음. 1개 정도 수정은 가능함. 전체 수정은 DB에서 수정하는 것이 좋음 
s1.name="홍길자"
print(s1.name)
# 추가 : 참조변수명.변수명 : 없는 변수명 입력 시 추가 # 추가도 수정과 같이 거의 하지 않음 
s1.rank = 1
print(s1.rank) 

stuList =[]
# 전체 출력
# print(s1.no,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,sep="\t")
# print(s2.no,s2.name,s2.kor,s2.eng,s2.math,s1.total,s1.avg,sep="\t")
stuList.append(s1)
stuList.append(s2)
# stu.add(s1)
# stu.add(s2)


print(s1) # def __str__(self) 로 지정하면 전체 출력 가능 
print(s2)

s1.kor = 10
s1.cal_total()
s1.cal_avg() 
print(s1)



