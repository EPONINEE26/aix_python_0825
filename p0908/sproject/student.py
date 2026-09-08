class Student:   

    def  __init__(self,no,name,kor,eng,math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng 
        self.math = math
        self.total = self.kor+self.eng+self.math
        self.avg = self.total/3 

    def __str__(self):
        return f"Student({self.no}, '{self.name}', {self.kor}, {self.eng}, {self.math}, {self.total}, {self.avg:.2f})"

    def cal_total(self):
        self.total = self.kor+self.eng+self.math

    def cal_avg(self): 
        self.__avg = self.__total/3

    def print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,f"{self.avg:.2f}",sep="\t")