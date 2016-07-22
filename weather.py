import xml.etree.ElementTree as etree
import urllib2
from datetime import datetime, timedelta
import os

response = urllib2.urlopen('http://www.yr.no/place/Czech_Republic/Zl%C3%ADn/Zl%C3%ADn/forecast_hour_by_hour.xml')
html = response.read()

root = etree.fromstring(html)

for time in root.iter('time'):
    od = datetime.strptime(time.attrib['from'], '%Y-%m-%dT%H:%M:%S')
    do = datetime.strptime(time.attrib['to'], '%Y-%m-%dT%H:%M:%S')
    ted = datetime.now() + timedelta(hours=3)
    if od < ted and do > ted:
        number = time.find('symbol').attrib['number']
        numberEx = time.find('symbol').attrib['numberEx']
        if number == "1":
            os.system("rainbow wan white auto") #Clear sky
        elif number == "2":
            os.system("rainbow wan ffff00 auto") #Fair
        elif number == "3":
            os.system("rainbow wan 00ff00 auto") #Partly cloudy
        elif number == "4":
            os.system("rainbow wan 0F97FF auto") #Cloudy
        elif number == "9" and numberEx == "46":
            os.system("rainbow wan AA11FF auto") #Light rain
        elif number == "9":
            os.system("rainbow wan 0000ff auto") #Rain
        else:
            os.system("rainbow wan red auto") #error
