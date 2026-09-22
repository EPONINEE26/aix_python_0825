# class Student: # 변수 
#     # 생성자 
#     def  __init__(self, no, name, kor, eng, math):
#         self.no = no
#         self.name = name
#         self.kor = kor
#         self.eng = eng 
#         self.math = math
#         self.total = (kor+eng+math) # 함수 내에 없는 정보는 새롭게 입력하면 변수 생성해서 만들어줌 
#         self.avg = (kor+eng+math) /3 

#     # 클래스 내 함수 매게변수 첫번째 self 입력 해야함.    
#     def sum(self):
#         self.sum = self.kor+self.eng+self.math
#     def avg (self):
#         self.avg = self.sum/3 
#     def print(self): 
#         print(self.no,self.name,self.kor,self.eng,self.math,self.total,f"{self.avg :.2f}")

# stuList = []
# # 객체선언
# s = Student(1,"홍길동",100,100,99) # 딕셔너리가 클래스로 변환됨 
# stuList.append(s)
# s.kor = 70 # 있는 정보 입력하면 수정됨. 수정방법. 클래스 변수 값 수정 
# # s.math = 100 math 라는 변수가 추가가 됨. 생성방법. 클래스 변수 추가  
# # print(s)


class Student:
    # 생성자
    def __init__(self,no,name,kor,eng,math):
        self.__no = no
        self.__name = name
        self.__kor = kor  #캡슐화:클래스내부에서만 값을 수정
        self.__eng = eng
        self.__math = math
        self.__total = kor+eng+math
        self.__avg = (kor+eng+math)/3

    def __str__(self):
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}"

    def get_kor(self):
        return self.__kor

    def set_kor(self,kor): # 캡슐화를 하면, 잘못된 값이 입력될때 에러처리
        if kor<0:
            print("잘못된 값이 들어옴.")
            return
        self.__kor = kor


    # 클래스 내 함수 매개변수 첫번째 self
    def cal_total(self):
        self.__total = self.__kor+self.__eng+self.__math

    def cal_avg(self): # -50을 입력하려고 할 때 
        self.__avg = self.__total/3
        # -50을 입력하려고 할 때 

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.__total,f"{self.__avg:.2f}",sep="\t")

stuList = []
# 객체선언
s = Student(1,"홍길동",100,100,99)
print("-"*50)
print(s)
print("-"*50)
s.__kor = 70    # 캡슐화를 시켜놓았기에 수정 불가 
s.__math = 40   
s.set_kor(-50) # setter, getter를 사용해서 수정, 확인을 해야함. 
s.cal_total()
s.cal_avg()
s.print()
print(s)


