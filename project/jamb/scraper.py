#!/usr/bin/env python3
# Extracts

from bs4 import BeautifulSoup
import requests
import re
import time


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
    etag = req.post(url, data=postdata, headers=dict(referer='https://portal.jamb.gov.ng/examslipprinting/printexaminationslip'))
    return(etag.headers)
   
    """ 
    r = req.get(url, headers=postdata)
    soup = BeautifulSoup(r.content, 'html.parser')
    result = ""

    pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
    try:
        phone = pattern.search(str(soup))
        phone = phone.group()
    except:
        phone = 0

    rows = soup.select('tr td table')
    row = rows[0]
    details = row.select_one('table')
    names = details.select('tr')

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
        
    result = surname + firstname + othername + "\t" + str(phone)
    return (result)
"""

if __name__ == "__main__":

    f1 = open('JAMB_EXTRACT.txt', 'a')

    with open("Reg_nos.txt", "r") as f2:
        for each in f2:
            try:
                print("Extracting details for {}".format(each), end="")
                each = each.strip()
                f1.write(str(scrapping(each)) + '\n')
                time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(1)

    f1.close()
    f2.close()
