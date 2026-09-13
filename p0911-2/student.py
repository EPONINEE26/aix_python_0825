class Student:

    def __init__(self,*args):
        if len(args) == 5: 
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = self.kor+self.eng+self.math
            self.avg = self.total/3
            self.rank = 0                           # ★ 등수 추가 (아직 계산 전 초기값)

        elif len(args) == 7: 
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = args[5]
            self.avg = args[6]
            self.rank = 0                           # ★ 등수 추가 (아직 계산 전 초기값)

        elif len(args) == 8:                        # ★ 등수까지 저장된(stu[7]) 파일을 읽을 때
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = args[5]
            self.avg = args[6]
            self.rank = args[7]                     # ★ 등수 추가
 

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"   # ★ 등수 추가

    def s_total(self):
        self.total=self.kor+self.eng+self.math

    def s_avg(self):
        self.avg = self.total/3 

    def print(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"   # ★ 등수 추가
