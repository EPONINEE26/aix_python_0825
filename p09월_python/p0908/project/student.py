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