import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


#변수명
endnum = 1
lastnum = int(input())
day = input()

PMb = []
PMs = []
danger1 = []
danger2 = []
miss = []


#while문으로 시간에 따른 미세먼지 농도를 txt파일에 저장하고 이를 다시 리스트에 저장한 뒤 그 데이터를 통해 경고메세지 출력
while endnum<lastnum + 1:
    soup = BeautifulSoup(urllib.request.urlopen('http://openapi.seoul.go.kr:8088/664a767a7368697a3430666f444370/xml/TimeAverageAirQuality/1/'+ str(endnum) + '/' + str(day)).read(), 'html.parser')
    res = soup.find_all('row')
    text = res[endnum-1].get_text()

    a = []

    with open('pm.txt', 'w') as file:
        for i in text:
            file.write(i)
    with open('pm.txt', 'r') as file1:
        for line in file1:
            a.append(line)

    if a[7] != '\n':
        PM10 = int(a[7])
    else:
        miss.append(a[1])
        PM10 = 0
    if a[8] != '\n':
        PM25 = int(a[8])
    else:
        PM25 = 0
    
    PMb.append(PM10)
    PMs.append(PM25)
    danger1.append(150)
    danger2.append(80)
    
    if 81<=PM10 and PM10<=150:
        if 36<=PM25 and PM25<=75:
            print('미세먼지 수치가 \'나쁨\'단계입니다.\n초미세먼지 수치가 \'나쁨\'단계입니다.')
        elif 76<=PM25:
            print('미세먼지 수치가 \'나쁨\'단계입니다.\n초미세먼지 수치가 \'매우나쁨\'단계입니다.')

    elif 151<=PM10:
        if 36<=PM25 and PM25<=75:
            print('미세먼지 수치가 \'매우나쁨\'단계입니다.\n초미세먼지 수치가 \'나쁨\'단계입니다.')
        elif 76<=PM25:
            print('미세먼지 수치가 \'매우나쁨\'단계입니다.\n초미세먼지 수치가 \'매우나쁨\'단계입니다.')
            
    else:
        if 36<=PM25 and PM25<=75:
            print('초미세먼지 수치가 \'나쁨\'단계입니다.')
        elif 76<=PM25:
            print('초미세먼지 수치가 \'매우나쁨\'단계입니다.')
        else:
            print('야외활동을 하기 좋은 날씨입니다.')

    endnum+=1


#pandas를 통해 미세먼지와 초미세먼지의 농도를 데이터화 시킨 후 html 파일에 넣어 저장
data = {
    'PM10': PMb,
    'PM25': PMs
    }

df = pd.DataFrame(data)
html = df.to_html()
with open('termproject.html', 'w') as htmlfile:
    htmlfile.write("<title>미세먼지 농도 정보</title>")
    htmlfile.write("<H1>미세먼지 농도 표</H1>")
    for i in html:
        htmlfile.write(i)
    htmlfile.write("<br><br><br><H1>미세먼지 농도 그래프<H1>\n<img src = \"finedust.png\">")
    
print(df)


#matplot을 통해 그래프 그리고 저장
plt.plot(PMb, color = 'skyblue', label = 'PM10')
plt.plot(PMs, color = 'pink', label = 'PM2.5')
plt.plot(danger1, color = 'black', label = 'danger 1')
plt.plot(danger2, color = 'black', label = 'danger 2')
plt.legend()
plt.savefig('finedust.png',dpi=75)

def average(list):
    return (sum(list) / len(list))

print('평균값: ', average(PMb))
print('누락된 시점: ', miss)
