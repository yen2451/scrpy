# -*- coding: utf-8 -*-
# scr2py.py
# @Author : chiayen hsu (yen_hsu's gmail:yen020224@gmail.com)
# @Date   : 8/17/2018, 10:14:01 PM
import requests
from bs4 import BeautifulSoup
def get_web(url):
    html_page =requests.get(url)
    html_page.encoding='utf-8'
    if html_page.status_code != 200:
        print("invalid url",html_page.status_code)
        return None
    else:
        return html_page.text
url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm'
result=get_web(url)
soup =BeautifulSoup(result,"html.parser")
fcstresult=soup.findAll("tbody")[0]
for i in range(0,3):
    dayandtime=fcstresult.findAll("th",scope="row")[i]
    print("時間:",dayandtime.text)
    for x in range(i*4,i*4+4):
        weatherinfo=fcstresult.findAll("td")[x]
        if x==1 or x==5 or x==9:
            continue
        else:
            if x==0 or x==4 or x==8:
                print("預測氣溫:",weatherinfo.text)
            elif x==2 or x==6 or x==10:
                print("舒適度預測:",weatherinfo.text)
            elif x==3 or x==7 or x==11:
                print("預測濕度:",weatherinfo.text)
                print()
    