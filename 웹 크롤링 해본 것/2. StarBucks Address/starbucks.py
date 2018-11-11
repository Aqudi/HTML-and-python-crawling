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
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\gjdigj145\PycharmProjects\programming project\Section3\webdriver\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\gjdigj145\PycharmProjects\programming project\Section3\webdriver\chromedriver.exe')

s = requests.Session()

for i in range(1, 18):
    driver.get('http://www.istarbucks.co.kr/store/store_map.do')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a').click()
    time.sleep(2)
    xpath = """//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li["""+ str(i) +''']/a'''
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mCSB_2_container"]/ul/li[1]/a').click()
    time.sleep(3)
    #html저장하기
    html = driver.page_source
    fulfilename = os.path.join("C:/", "C:/"+str(i)+'.html')
    with open(fulfilename, 'w', encoding='UTF8') as f:
        f.write(html)
    time.sleep(10)
driver.quit()
