from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv  

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() 
browser.get(url)
time.sleep(3)

#아이디와 패스워드 입력 
browser.find_element(By.XPATH,'//*[@id="id"]').click()
browser.find_element(By.XPATH,'//*[@id="id"]').send_keys('tracey212')
browser.find_element(By.XPATH,'//*[@id="pw"]').click()
browser.find_element(By.XPATH,'//*[@id="pw"]').send_keys('1111')

load_dotenv()
naver_id = os.getenv('naver_id')
naver_pw = os.getenv('naver_pw')
# 아이디 패스워드 입력 
input_js = 'document.getElementById("id").value = "{id}";\
            document.getElementById("pw").value = "{pw}";\
            '.format(id=naver_id,pw=naver_pw)

browser.execute_script(input_js)
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="loginBtn_row"]')

input()

# 1. 자바스크립트가 포함되어 있으면 selenuim 사용 
# 2. find, find_all 로 f12에서 값 찾음 
# 3. [속성값] 찾아서 입력

# 웹 변수 -> 타입은 str
# int, float 계산가능

# 문자에, 단위 표기가 포함되어 있으면 
# replace("","")

# a = '1000원'
# int(a[:-1])-> 마지막 원 자는 출력 안 함 


# sum = 0
# for i in range(1,2):
#     page = i
#     url = f"https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
#     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
#     res = requests.get(url,headers=headers)
#     res.raise_for_status() #에러시 종료
#     soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
#     p_ul = soup.find('ul',{'class':'product_list'})
#     lis = p_ul.find_all('li')
#     # prod_name = lis[0].find('p',{'class':'prod_name'}).get_text(strip=True)
#     # print(prod_name)
#     # print(len(lis))
#     for li in lis:
#         try: # 중간중간 이름없는 상품으로 인해 에러가 나는 것을 방지하기 위한 장치 
#             prod_name = li.find('p',{'class':'prod_name'}).get_text(strip=True)
#             print(prod_name)
#         except:
#             print('이름/가격없음')    
#         prod_link = li.find('a',{'class':'click_log_product_standard_price_'})['href']
#         prod_price = li.find('a',{'class':'click_log_product_standard_price_'}).get_text(strip=True)[:-1]
#         prod_price_int = int(prod_price.replace(',',''))
#         if prod_price_int<1500000:
#             print(f"{prod_name} : {prod_price} ",prod_price_int)
#             print("링크 : ",prod_link)
#         else:
#             print('150만원 이상 제외')
#         print("-"*50)
#         # print("개수 : ",len(lis))
