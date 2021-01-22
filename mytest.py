import time
import re
import requests
from bs4 import BeautifulSoup
import urllib.request as urllib2

# List of stocks and technicals to pull using the program. All the data will be stored in a dict.
def scrape_yahoo(stock):
	technicals = {}
	url = ('https://finance.yahoo.com/quote/'+stock+'?p='+stock)
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	tables = soup.findAll('table')	# Found using page inspection
							# col_val[0] is the name cell (with subscript)
	for table in tables:
		table_body = table.find('tbody')
		rows = table_body.find_all('tr')
		for row in rows:
			col_name = row.find_all('span')							# Use span to avoid supscripts
			col_name = [cell.text.strip() for cell in col_name]
			col_val = row.find_all('td')
			col_val = [cell.text.strip() for cell in col_val]
			technicals[col_name[0]] = col_val[1]
								# col_val[0] is the name cell (with subscript)
	r = requests.get(url)
	web_content = BeautifulSoup(r.text , 'lxml')
	web_content = web_content.find('div',class_='My(6px) Pos(r) smartphone_Mt(6px)')
	web_content = web_content.find('span')
	pr = str(web_content.contents[0])
	technicals['Price'] = pr							
								
	return technicals

def scrape(stock_list, interested, technicals):
	for each_stock in stock_list:
		technicals = scrape_yahoo(each_stock)
		print(each_stock.upper())
		#print('\n')
		#print(technicals)
		for ind in interested:
			print(ind + ": "+ technicals[ind])
		print("------")
		time.sleep(1)													# Use delay to avoid getting flagged as bot
	return technicals

def main():
	# stl me ticker.txt se data extract hora
	hand = open('ticker.txt')
	stl = list()
	for line in hand:
		x = re.findall('[A-Z]+',line)
		for i in x:
			stl.append(i)
	stock_list = ['aapl', 'tsla', 'ge']
	interested = ['Price','Market Cap', 'Previous Close', 'Open', 'PE Ratio (TTM)', 'Forward Dividend & Yield']
	technicals = {}
	tech = scrape(stl, interested, technicals)
	


if __name__ == "__main__":
	main()

#scrape_yahoo('aapl')
		