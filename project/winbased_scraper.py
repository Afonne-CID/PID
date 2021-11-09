from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re


def load_page(reg_no):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging", "ignore-certificate-errors"])
    url = 'https://portal.jamb.gov.ng/ExamSlipPrinting/PrintExaminationSlip'
    s=Service("C:/Users/DOZI/Desktop/SCRAPER/chromedriver.exe")

    driver = webdriver.Chrome(service=s, options=options)
    driver.get(url)

    search_field = driver.find_element(By.ID, 'txtRegNumber')
    search_field.send_keys(reg_no)

    submit = driver.find_element(By.ID, 'lnkSearch')
    submit.click()
    time.sleep(1.5)

def scrapping(reg_no):
    url = "https://portal.jamb.gov.ng/ExamSlipPrinting/TempFiles/Main_Examination_Slip_" + str(reg_no) + ".htm"
    postdata = {
            '__EVENTTARGET': 'lnkSearch',
            '__VIEWSTATE': 'NxdDyuHuVMNRMWglTkK0Yhn5KY2R4OOMfQscO8bJyATjZcu+b3AU6k/ssKxd5m2lpjHLU08xb/GaPvoHUoBKFIA/tfY/UyoMZm8+G7ReA87pGzp37UxdSWrJ5kVfOYT20keD8E7Gg7E6ZeyAwENnww==',
           '__EVENTVALIDATION': 'cxusMBFlG/AQfwHuETuD9idUNpq9UVsO2veYcmdjk4Q/sVDx5tdMQaJbptoFYMt8GdubBxPoQzrgFCiTrjXRYStgd90Cxb6Xx5ZtOLjufRUD1TGZM4kf8/VqFDMOon704M6O7oztvfyKhSqk9lRT/4z1W7hT4JIzalzdJmF9s9o=',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
           'cookie': 'ASP.NET_SessionId=a0rh13nzcamjvitw5xmnrnrx',
           'txtRegNumber': reg_no
    }
    req = requests.Session()
    r = req.get(url, headers=postdata)
    soup = BeautifulSoup(r.content, 'html.parser')
    surname = firstname = othername = result = ""

    rows = soup.select('tr td table')
    row = rows[0]
    details = row.select_one('table')
    names = details.select('tr')
    pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')

    try:
        container = names[0]
        surname = container.select('td')
        surname = surname[1].text
    except:
        surname = ""  

    try:
        container = names[1]
        firstname = container.select('td')
        firstname = firstname[1].text
    except:
        firstname = ""
    try:
        container = names[2]
        othername = container.select('td')
        othername = othername[1].text
    except:
         othername = ""

    try:
        phone = pattern.search(str(soup))
        phone = phone.group()
    except:
        phone = 0

    result = surname + firstname + othername + ",\t\t" + str(phone)
    return (result)


if __name__ == "__main__":

    f1 = open('JAMB_EXTRACT.txt', 'a')

    with open("C:/Users/DOZI/Desktop/SCRAPER/Reg_nos.txt", "r") as f2:
        for each in f2:
            each = each.strip()
            try:
                print("Extracting details for {}".format(each))
                load_page(each)
                f1.write(str(scrapping(each)) + '\n')
            except Exception as e:
                print(e)

    f1.close()
    f2.close()
