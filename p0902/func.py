import random 
def main_print():
    print("1. 랜덤숫자 5개 가져오기")
    print("2. 랜덤숫자 3개 가져오기")
    print("3. 랜덤숫자 1개 가져오기")
    choice = int(input("원하는 번호를 입력하세요."))
    return choice

def ran_number(choice): 
    if choice == 1 :
        # 랜덤 숫자 5개 
        result = random.sample(range(1, 101), 5)
    elif choice == 2:     
        # 랜덤 숫자 3개 
        result = random.sample(range(1, 101), 3)
    else:
        # 랜덤숫자 1개 
        result = random.sample(range(1, 101), 1) 
    return result    
    
  

    




