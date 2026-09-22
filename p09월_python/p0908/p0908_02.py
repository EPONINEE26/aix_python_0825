# 일반적인 프로그램 
color = ""
speed = 0

def upSpeed():
    global speed  # 
    speed += 10

def downSpeed():
    global speed
    speed -= 10 

color = "white"
print("색상 : ", color)
print("속도 : ", speed)

upSpeed()
print("속도 : ", speed)




color2 =""
speed2 = 0

def upSpeed2():
    global speed
    speed += 10

def downSpeed2():
    global speed
    speed -= 10 

color = "white"
print("색상 : ", color2)
print("속도 : ", speed2)

upSpeed()
print("속도 : ", speed2)