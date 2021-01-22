import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup


def real_time_price(stock):
	url = ('https://finance.yahoo.com/quote/'+stock+'?p='+stock)
	r = requests.get(url)
	#print(r.text)
	web_content = BeautifulSoup(r.text , 'lxml')
	web_content = web_content.find('div',class_='My(6px) Pos(r) smartphone_Mt(6px)')
	web_content = web_content.find('span')
	return str(web_content.contents[0])


HSI = ['aapl','aame','aan','aap']

for step in range(1,101):
	price = []
	col = []
	timestamp = datetime.datetime.now()
	timestamp = timestamp.strftime('%Y-%m-%d %H-%M-%S')
	for stock in HSI:
		price.append(real_time_price(stock))
	col = [timestamp]
	col.extend(price)
	df = pd.DataFrame(col)
	df = df.T
	df.to_csv('stock_data.csv',mode = 'a', header = False)
	print(col)
