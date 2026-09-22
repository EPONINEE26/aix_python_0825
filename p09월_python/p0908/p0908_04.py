class Student:

    def __init__(self, no, name, kor, eng, math, total, avg): # 생성자 오타 수정
        self.__no = no
        self.__name = name
        self.__kor = kor # 캡슐화. 클래스 내부에서만 값을 수정
        self.__eng = eng
        self.__math = math
        self.__total = kor+eng+math
        self.__avg = (kor+eng+math) / 3 

    def  __str__(self): # 참조변수 
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}\t"

    def get__kor(self):
        return self.__kor
    
    def set__kor(self, kor):
        self.__kor = kor  # 값을 실제로 대입하도록 연결

    # 하단에서 호출되는 set__math 함수를 클래스 내부에 그대로 추가
    def set__math(self, math):
        self.__math = math

    def sum(self):
        self.__sum = self.__kor+self.__eng+self.__math
        # 계산된 합계가 __str__과 print에 반영되도록 __total에도 대입
        self.__total = self.__sum
        
    def avg(self):
        self.__avg = self.__sum / 3

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.__total,self.__avg)

stuList=[]
s = Student(1,"홍길동",100,100,99,0,0)
print("-"*50) 
print(s)
print("-"*50) 

# s.kor = 70 # 언더바가 있을 경우에는 처움에 넣은 정보가 그대로 유지. 
# s.math = 40 # 언더바 2칸 

s.set__kor(50)
s.set__math(50)
s.sum()
s.avg()

# s.print()
print(s)  # 💡 결과를 눈으로 확인하실 수 있도록 마지막 print(s)의 주석을 해제했습니다.
