from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc

# 쿠팡 - 검색하여 노트북 200건 리스트를 출력하시오
# 보안 때문에 안 될 수 있으나 셀레니움 방지가 적용. 해제하는 방법 
# 쿠팡 검색하여 리스트를 출력하시오. 


# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")

# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&traceId=muksjcx4"
# options = uc.ChromeOptions()
# options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
# options.add_argument("User-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
# browser = uc.Chrome(options=options)
# browser.maximize_window() 
# browser.get(url)
# print("완료") 
# input()

sum = 0 
for i in range(1,6):
    page = i
    url = f"https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    p_ul = soup.find('ul', {'class' : 'product-list'})
    lis = p_ul.find_all('li')
    # print("개수 : ", len(lis))
    prod_name = lis[0].find('p', {'class' : 'prod_name'}).get_text(strip=True)
    prod_price = lis[0].find('a', {'class' : 'click_log_product_standard_price_'}).get_text(strip=True)[:-1] # "원"자 빼고 출력 
    prod_price_int = int(prod_price.replace(",",""))
    if prod_price_int<1500000:
        print(f"{prod_name}:{prod_price} " , prod_price_int)
        print("링크 :" , "https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page=1&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A")
        print("-"*50)
    else:
        print("150만원 이상 제외")
    print("-"*50)
   

# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file/coupang1.html','a',encoding='utf-8') as f:
#     f.write(soup.prettify())

# print("완료") 

# with open('p0928/file/coupang1.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')
# print(len(soup))



