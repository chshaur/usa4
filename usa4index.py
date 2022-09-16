import json
import datetime
from re import A
import requests
import sys
import time
from bs4 import BeautifulSoup

final_data = {}
url = "https://tw.stock.yahoo.com/world-indices"
today = datetime.date.today()

try:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    myneed = soup.find('div', {"class":"table-body-wrapper"})
    lis = myneed.find('ul').find_all('li')

    #parsing DOW data
    dow_data = lis[0].find_all('span')
    dow_close = float(dow_data[3].contents[0].replace(',',''))
    dow_class = dow_data[3]['class'][4]
    dow_trend = 0
    if "trend-up" in dow_class:
        dow_trend = 1
    elif "trend-down" in dow_class:
        dow_trend = -1

    dow_change = dow_trend * float(dow_data[4].contents[1])
    dow_ret = dow_data[6]
    dow_ampliude = dow_ret.contents[1]
    dow_ampliude = float(dow_ampliude[0:len(dow_ampliude)-1]) * dow_trend
    dow_last_close = float(dow_data[11].contents[0].replace(',',''))
    dow_time = dow_data[15].contents[0]
    tmp = [dow_close, dow_last_close, dow_change, dow_ampliude, dow_time]
    final_data["DOW"] = tmp

    #parsing S&P 500 data    	
    sp_data = lis[1].find_all('span')
    sp_close = float(sp_data[3].contents[0].replace(',',''))
    sp_class = sp_data[3]['class'][4]
    sp_trend = 0
    if "trend-up" in sp_class:
        sp_trend = 1
    elif "trend-down" in sp_class:
        sp_trend = -1

    sp_change = sp_trend * float(sp_data[4].contents[1])
    sp_ret = sp_data[6]
    sp_ampliude = sp_ret.contents[1]
    sp_ampliude = float(sp_ampliude[0:len(sp_ampliude)-1]) * sp_trend
    sp_last_close = float(sp_data[11].contents[0].replace(',',''))
    sp_time = sp_data[15].contents[0]
    tmp = [sp_close, sp_last_close, sp_change, sp_ampliude, sp_time]
    final_data["S&P"] = tmp

    #parsing Nasdaq data    	
    nasdaq_data = lis[2].find_all('span')
    nasdaq_close = float(nasdaq_data[3].contents[0].replace(',',''))
    nasdaq_class = nasdaq_data[3]['class'][4]
    nasdaq_trend = 0
    if "trend-up" in nasdaq_class:
        nasdaq_trend = 1
    elif "trend-down" in nasdaq_class:
        nasdaq_trend = -1

    nasdaq_change = nasdaq_trend * float(nasdaq_data[4].contents[1])
    nasdaq_ret = nasdaq_data[6]
    nasdaq_ampliude = nasdaq_ret.contents[1]
    nasdaq_ampliude = float(nasdaq_ampliude[0:len(nasdaq_ampliude)-1]) * nasdaq_trend
    nasdaq_last_close = float(nasdaq_data[11].contents[0].replace(',',''))
    nasdaq_time = nasdaq_data[15].contents[0]
    tmp = [nasdaq_close, nasdaq_last_close, nasdaq_change, nasdaq_ampliude, nasdaq_time]
    final_data["Nasdaq"] = tmp
        
    #parsing SOX data    	
    sox_data = lis[3].find_all('span')
    sox_close = float(sox_data[3].contents[0].replace(',',''))
    sox_class = sox_data[3]['class'][4]
    sox_trend = 0
    if "trend-up" in sox_class:
        sox_trend = 1
    elif "trend-down" in nasdaq_class:
        sox_trend = -1

    sox_change = sox_trend * float(sox_data[4].contents[1])
    sox_ret = sox_data[6]
    sox_ampliude = sox_ret.contents[1]
    sox_ampliude = float(sox_ampliude[0:len(sox_ampliude)-1]) * sox_trend
    sox_last_close = float(sox_data[11].contents[0].replace(',',''))
    sox_time = sox_data[15].contents[0]
    tmp = [sox_close, sox_last_close, sox_change, sox_ampliude, sox_time]
    final_data["SOX"] = tmp    
except:
    final_data["ERROR"] = "ERROR"

to_file = 'D:\\Projects\\Python\\usa4\\' + datetime.datetime.today().strftime("%Y%m%d") + '.html'
fp = open(to_file, "w")
fp.write(json.dumps(final_data))
fp.close()
### print(json.dumps(final_data))
 