# -*- coding: utf-8 -*-
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\gjdigj145\PycharmProjects\programming project\Section3\webdriver\chromedriver.exe')
#driver = webdriver.Chrome(r'C:\Users\gjdigj145\PycharmProjects\programming project\Section3\webdriver\chromedriver.exe')

s = requests.Session()

baseUrl = "http://www.momstouch.co.kr/sub/store/store_01_list.html?pg="
for i in range(1,114):#114
    url = baseUrl + str(i)
    #with driver.Session() as s:
        #req = s.get(url)
        #html = req.text
    driver.get(url)
    time.sleep(2.5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    html = soup.find_all('table', class_="store_List")
    #print(html)
    print(dir(html), html)
    with open(os.getcwd()+"/Moms_htmls/html.html", mode='a', encoding='utf8') as f:
        f.write(str(html[0]))
