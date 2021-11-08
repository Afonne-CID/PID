#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://portal.jamb.gov.ng/ExamSlipPrinting/PrintExaminationSlip")


