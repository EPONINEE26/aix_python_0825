import requests
from bs4 import BeautifulSoup
import os

# python -m pip install selenium 설치 

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() 