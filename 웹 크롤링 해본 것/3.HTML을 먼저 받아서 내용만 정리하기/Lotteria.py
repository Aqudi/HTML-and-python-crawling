# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
import requests
import os
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

def ClickXpath(what):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, what)))
    driver.find_element_by_xpath(what).click()

def SaveFile(what):
    with open(os.getcwd() + "/working_htmls/Lotteria.html", mode='a', encoding='utf8') as f:
        f.write(str(what))

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\gjdigj145\PycharmProjects\programming project\webdriver\chromedriver.exe')
#driver = webdriver.Chrome(r'C:\Users\gjdigj145\PycharmProjects\programming project\webdriver\chromedriver.exe')

#저장할 파일 초기화
with open(os.getcwd() + "/working_htmls/Lotteria.html", mode='w', encoding='utf8') as f:
    f.write("롯데리아 주소록 필요 HTML")

regions = "서울,부산,대구,인천,광주,울산,세종특별자치시,경기,강원,충남,충북,전북,전남,경북,경남,제주특별자치도"
regions = regions.split(',')
btnXpath = ["""//*[@id="info.search.page.no1"]""", """//*[@id="info.search.page.no2"]""", """//*[@id="info.search.page.no3"]""", """//*[@id="info.search.page.no4"]""", """//*[@id="info.search.page.no5"]"""]
nextbtnXpath = """//*[@id="info.search.page.next"]"""
s = requests.Session()

#다음지도 목적페이지로 이동
storeList = ["롯데리아"]
temp = []
driver.implicitly_wait(3)


totalstore = 0
for region in regions:
    driver.get('http://map.daum.net/')
    search = driver.find_element_by_id("search.keyword.query")
    search.send_keys(region + " " + storeList[0])
    #search.send_keys("제주 롯데리아")
    print(region + "의 롯데리아 자료")
    #준비단계
    ClickXpath("""//*[@id="search.keyword.submit"]""")
    time.sleep(1.0)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    numTotal = soup.find("em", id='info.search.place.cnt')
    #numTotal은 가게의 수가 얼마나 되는지를 나타냅니다.
    if numTotal:
        #항목을 패스트푸드로 바꾸고 다시 페이지를 파싱합니다.
        ClickXpath("""//*[@id="info.search.place.list"]/li[1]/div/div[2]/span[2]""")
        time.sleep(0.7)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.find("ul", class_="placelist")
        numTotal = int(soup.find("em", id='info.search.place.cnt').string)
        lastPage = numTotal // 15 + 1
        #목록이 15개를 초과해야만 장소 더보기 버튼이 생깁니다.
        if numTotal > 15:
            ClickXpath("""//*[@id="info.search.place.more"]""")
            counter = 0
            #목록 리스트가 있을 때 1번페이지부터 누르면서 수집을 시작합니다.
            while counter < lastPage:
                for btn in btnXpath:
                    ClickXpath(btn)
                    time.sleep(0.7)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    html = soup.find("ul", class_="placelist")
                    SaveFile(html)
                    counter += 1
                    print("총 {}개의 가게 진행상황은 {}/{} 입니다. {}".format(numTotal, counter, lastPage, counter==lastPage))
                    if counter == lastPage:
                        break
                if counter == lastPage:
                    break
                ClickXpath(nextbtnXpath)

            print(counter)
        #목록이 15개를 초과하지 않을 때 그 페이지만 파싱하고 끝납니다.
        else:
            SaveFile(html)
        totalstore += numTotal
        print("총 {}개의 가게, {}개의 페이지를 파싱했습니다.".format(numTotal, lastPage))

print(totalstore)
driver.quit()