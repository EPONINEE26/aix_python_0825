# 클래스 : 데이터를 보호할 수 있다는 강점이 있음 
# 변수와 함수를 모두 포함해서 구현 
# class 클래스명 : 

# class Car: # 클래스명은 대문자로 시작 
#     color = ""
#     speed = 0
#     tire = 0
#     door = 0 

#     def upSpeed (self):
#         self.speed += 10 # 변수를 지정하려면 self 를 무조건 붙여야만 함 
#     def downSpeed(self):
#         self.speed -= 10 


# 클래스 1개 생성 
# c = Car() # 객체(인스턴트) 생성
# c.color = "white"
# print("색상 : ", c.color)
# print("속도 : ", c.speed)

# c.upSpeed()
# print("속도2 : " , c.speed)

# c2 = Car() 
# c2.upSpeed()
# c2.downSpeed()
# c.color = "white"
# speed = 10 
# print("색상 : ", c.color)
# print("속도 : ", c.speed)

# c2.upSpeed()
# print("속도2 : " , c.speed)


class Car: # 클래스명 첫글자는 대문자로 시작 
    color = ""
    speed = 0
    tire = 0
    door = 0 

# 생성자 - 생성함수 : Car() 선언할 때 실행되는 함수  (__init__ : 함수)
    def __init__(self,color,speed,tire,door): # 들여쓰기 중요함 
        self.color = color
        self.speed = speed 
        self.tire = tire 
        self.door = door 


    def upSpeed (self):
        self.speed += 10 # 변수를 지정하려면 self 를 무조건 붙여야만 함 
    def downSpeed(self):
        self.speed -= 10 

c = Car() # 객체 (인스턴트) 생성 / 4개의 변수, 2개의 함수 자동 생성 c 정보만 확인
c.color = "white"
c.speed = 100
c.tire = 5
c.door = 3 
c = Car()
c.upSpeed() # c 정보만 확인 
# 클래스 객체선언 (생성과 동일한 의미) c2 정보만 확인
c2 = Car("skyblue",200,4,5) # 선언할 때 값을 같이 선언해도 됨 
c2.color = "skyblue"
c2.speed = 200
c2.tire = 4
c2.door = 5
c2.upSpeed() 
# 클래스 객체선언 (생성과 동일한 의미) c3 정보만 확인 
c3 = Car("grey", 50, 5,5) # 선언할 때 값을 같이 선언해도 됨 
c3.color = "grey"
c3.speed = 50
c3.tire = 5
c3.door = 5
c3.upSpeed() 


