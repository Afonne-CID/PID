#!/usr/bin/env python3
# Extracts

from bs4 import BeautifulSoup
import requests


def scrapping(reg_no):
    url = "https://aris.uniport.edu.ng/functions/dat_admissionAcceptance"
    postdata = {'searchData': reg_no}
    
    r_init = requests.get(url, headers=dict(referer=url))

    r = requests.post(url, data=postdata, headers=dict(referer=url))
    soup = BeautifulSoup(r.text, 'html.parser')

    return (soup.select_one('#phone')['value'] + " " + soup.select_one('#email')['value'])


if __name__ == "__main__":

    f1 = open('Embassy.txt', 'a')

    with open("Reg_nos.txt", "r") as f2:
        for each in f2:
            try:
                print("Extracting details for {}".format(each), end="")
                each = each.strip()
                f1.write(scrapping(each) + '\n')
            except Exception as e:
                print(e)

    f1.close()
    f2.close()
