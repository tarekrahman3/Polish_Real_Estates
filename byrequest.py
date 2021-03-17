from requests_html import HTMLSession
session = HTMLSession()
import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd

df = pd.read_csv('imports.csv', header=0)
list_ = df.links.to_list()
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []
col11 = []
col12 = []
col13 = []
col14 = []
col15 = []
col16 = []
col17 = []
col18 = []
col19 = []
#col20 = []

for i in range(200):
	response = session.get(list_[i])
	response.html.render()
	try:
		title = response.html.xpath("//h1/text()")
	except:
		title = "!!ERROR OCCURED"
	try:
		price = response.html.xpath("//strong[contains(@data-cy, 'Price')]/text()")
	except:
		price = ""
	try:
		address = response.html.xpath("//*[@id='__next']/main/div/div[2]/header/div[2]/a/text()")
	except:
		address = ""
	try:
		property_type = response.html.xpath("//div[contains(@aria-label, 'Rodzaj zabudowy')]/div[2]/text()")
	except:
		property_type = ""
	try:
		rooms = response.html.xpath("//div[contains(@aria-label, 'Liczba pokoi')]/div[2]/text()")
	except:
		rooms = ""
	try:
		area = response.html.xpath("//div[contains(@aria-label, 'Powierzchnia')]/div[2]/text()")
	except:
		area = ""
	try:
		year_of_cons = response.html.xpath("//div[contains(@aria-label, 'Rok budowy')]/div[2]/text()")
	except:
		year_of_cons = ""
	try:
		market = response.html.xpath("//div[contains(@aria-label, 'Rynek')]/div[2]/text()")
	except:
		market = ""
	try:
		_1st_floor = response.html.xpath("//div[contains(@aria-label, 'Piętro')]/div[2]/text()")
	except:
		_1st_floor = ""
	try:
		floors = response.html.xpath("//div[contains(@aria-label, 'Liczba pięter')]/div[2]/text()")
	except:
		floors = ""
	try:
		building_materials = response.html.xpath("//div[contains(@aria-label, 'Materiał budynku')]/div[2]/text()")
	except:
		building_materials = ""
	try:
		windows = response.html.xpath("//div[contains(@aria-label, 'Okna')]/div[2]/text()")
	except:
		windows = ""
	try:
		heating = response.html.xpath("//div[contains(@aria-label, 'Ogrzewanie')]/div[2]/text()")
	except:
		heating = ""
	try:
		trim_condition = response.html.xpath("//div[contains(@aria-label, 'Stan wykończenia')]/div[2]/text()")
	except:
		trim_condition = ""
	try:
		rent = response.html.xpath("//div[contains(@aria-label, 'Czynsz')]/div[2]/text()")
	except:
		rent = ""
	try:
		offer_numbers = response.html.xpath('//div[contains(text(), "Nr oferty w Otodom:")]/text()')
	except:
		offer_numbers = ""
	try:
		date_added = response.html.xpath('//div[contains(text(), "Data dodania: ")]/text()')
	except:
		date_added = ""
	try:
		updated = response.html.xpath('//div[contains(text(), "Data aktualizacji: ")]/text()')
	except:
		updated = ""
	print(f"{i} || {title} _ {price} _ {offer_numbers} {date_added} {updated}")
	col2.append(title)
	col1.append(list_[i])
	col3.append(price)
	col4.append(address)
	col5.append(property_type)
	col6.append(rooms)
	col7.append(area)
	col8.append(year_of_cons)
	col9.append(market)
	col10.append(_1st_floor)
	col11.append(floors)
	col12.append(building_materials)
	col13.append(windows)
	col14.append(heating)
	col15.append(trim_condition)
	col16.append(rent)
	col17.append(offer_numbers)
	col18.append(date_added)
	col19.append(updated)




data = {'link':col1,
'title':col2,
'price': col3,
'address': col4,
'property_type': col5,
'rooms': col6,
'area':col7,
'year_of_cons': col8,
'market': col9,
'_1st_floor': col10,
'floors': col11,
'building_materials': col12,
'windows': col13,
'heating': col14,
'trim_condition': col15,
'rent': col16,
'offer_numbers': col17,
'date_added': col18,
'updated': col19
}

df = pd.DataFrame(data)
print(df)
df.to_csv (r'export_byrequest.csv')




