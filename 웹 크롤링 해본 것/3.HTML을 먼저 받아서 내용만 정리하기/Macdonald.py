# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\gjdigj145\PycharmProjects\programming project\webdriver\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\gjdigj145\PycharmProjects\programming project\webdriver\chromedriver.exe')


btnXpath = ["""//*[@id="info.search.page.no1"]""", """//*[@id="info.search.page.no2"]""", """//*[@id="info.search.page.no3"]""", """//*[@id="info.search.page.no4"]""", """//*[@id="info.search.page.no5"]"""]

s = requests.Session()

#다음지도 목적페이지로 이동
storeList = ["맥도날드"]
driver.get('http://map.daum.net/')
search = driver.find_element_by_id("search.keyword.query")
search.send_keys(storeList[0])
try:
    time.sleep(1)
    driver.find_element_by_xpath("""//*[@id="search.keyword.submit"]""").click()
except:
    print("except1")
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="search.keyword.submit"]""").click()
try:
    time.sleep(1)
    driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
except:
    print("except2")
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
try:
    time.sleep(1)
    driver.find_element_by_xpath(("""//*[@id="info.search.place.list"]/li[1]/div/div[2]/span[2]""")).click()
except:
    print("except3")
    time.sleep(5)
    driver.find_element_by_xpath(("""//*[@id="info.search.place.list"]/li[1]/div/div[2]/span[2]""")).click()
time.sleep(5)

counter = 0
#반복횟수와 종료위치 설정
for i in range(1,100):#114
    if counter == 420:
        break
    for btn in btnXpath:
        if counter == 420:
            break
        driver.find_element_by_xpath(btn).click()
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        html = soup.find_all("ul", class_="placelist")
        with open(os.getcwd()+"/working_htmls/Macdonald.html", mode='a', encoding='utf8') as f:
            f.write(str(html[0]))
        counter += 1

    time.sleep(3.5)
    driver.find_element_by_xpath("""//*[@id="info.search.page.next"]""").click()
    time.sleep(3.5)
    print("PAGE >>", i, "number >>", counter, "content >>", counter*15)