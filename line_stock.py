from urllib import request
import twstock 
import requests
import json
name = '6770'
url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_'+name+'.tw&json=1&delay=0'
stock = twstock.realtime.get('6770')
r = requests.get(url)
info = json.loads(r.text)
print (info['msgArray'][0]['pz'])
#print(stock['realtime']['latest_trade_price'])