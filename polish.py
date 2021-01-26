from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv
import os

options = Options()
#options.headless = True
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
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
col20 = []
col21 = []
col22 = []
col23 = []
col24 = []
col25 = []
col26 = []
col27 = []
col28 = []
col29 = []
col30 = []

df = pd.read_csv('import.csv', header=0)
list_ = df.links.to_list()

driver = webdriver.Chrome(options=options, executable_path='/home/tarek/Selenium_Projects/webdrivers/chromedriver')

def crawl():
	for i in list_:
		source_ = f"{i}"
		driver.get(i)
		time.sleep(5)
		try:
			more_button = driver.find_element_by_xpath("//section[2]/button/span").click()
		except:
			pass
		try:
			area = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Powierzchnia')]/div")
			area = area[1].text	
		except:
			area = 'N/A'
		try:
			rooms = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Liczba pokoi')]/div")
			rooms = rooms[1].text
		except:
			rooms = 'N/A'
		try:
			market = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Rynek')]/div")
			market = market[1].text
		except:
			market = 'N/A'
		try:
			buildyng_type = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Rodzaj zabudowy')]/div")
			buildyng_type = buildyng_type[1].text
		except:
			buildyng_type = 'N/A'
		
		try:
			_1st_floor = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Piętro')]/div")
			_1st_floor = _1st_floor[1].text
		except:
			_1st_floor = 'N/A'
		try:
			floors = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Liczba pięter')]/div")
			floors = floors[1].text
		except:
			floors = 'N/A'
		
		try:
			building_materials = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Materiał budynku')]/div")
			building_materials = building_materials[1].text
		except:
			building_materials = 'N/A'
		
		try:
			windows = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Okna')]/div")
			windows = windows[1].text
		
		except:
			windows = 'N/A'
		try:
			heating = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Ogrzewanie')]/div")
			heating = heating[1].text
		
		except:
			heating = 'N/A'
		try:
			year_of_build = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Rok budowy')]/div")
			year_of_build = year_of_build[1].text
		except:
			year_of_build = 'N/A'
		try:
			trim_condition = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Stan wykończenia')]/div")
			trim_condition = trim_condition[1].text
		except:
			trim_condition = 'N/A'
		try:
			rent = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Czynsz')]/div")
			rent = rent[1].text
		except:
			rent = 'N/A'
		try:
			property_type = driver.find_elements_by_xpath("//div[contains(@aria-label, 'Forma własności')]/div")
			property_type = property_type[1].text
		except:
			property_type = 'N/A'
		try:
			title = driver.find_element_by_xpath("//h1[contains(@data-cy, 'adPageAdTitle')]").text
		except:
			title = 'N/A'
		try:
			address = driver.find_element_by_xpath("//*[@id='__next']/main/div/div[2]/header/div[2]/a").text
		except:
			address = 'N/A'
		try:
			price = driver.find_element_by_xpath("//strong[contains(@data-cy, 'Price')]").text
		except:
			price = 'N/A'
		try:
			price_per_square_meter = driver.find_element_by_xpath("//header/div[3]").text
		except:
			price_per_square_meter = 'N/A'
		try:
			description = driver.find_element_by_xpath("//div[contains(@data-cy, 'adPageAdDescription')]").text
		except:
			description = 'N/A'
		try:
			first_desc_title = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[1]/h3").text
		except:
			first_desc_title =  'N/A'
		try:
			first_desc = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[1]/ul").text
		except:
			first_desc =  'N/A'
		try:
			second_desc_title = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[2]/h3").text
		except:
			second_desc_title =  'N/A'
		try:
			second_desc = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[2]/ul").text
		except:
			second_desc =  'N/A'
		try:
			third_desc_title = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[3]/h3").text
		except:
			third_desc_title =  'N/A'
		try:
			third_desc = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[3]/ul").text
		except:
			third_desc =  'N/A'
		try:
			fourth_desc_title = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[4]/h3").text
		except:
			fourth_desc_title =  'N/A'
		try:
			fourth_desc = driver.find_element_by_xpath("//div[contains(@data-cy, 'ad.ad-features.categorized-list')]/div[4]/ul").text
		except:
			fourth_desc =  'N/A'
		try:
			offer_number = driver.find_element_by_xpath("//main/div/div[3]/div[6]/div[1]").text
		except:
			offer_number = 'N/A'
		try:
			date_added = driver.find_element_by_xpath("//main/div/div[3]/div[6]/div[3]/font/font").text	
		except:
			date_added = 'N/A'
		try:
			footer = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div[3]/div[6]/div').text
		except:
			footer = 'N/A'
		
		col1.append(source_)
		col2.append(title)
		col3.append(address)
		col4.append(price)
		col5.append(price_per_square_meter)
		col6.append(area)
		col7.append(rooms)
		col8.append(market)
		col9.append(buildyng_type)
		col10.append(_1st_floor)
		col11.append(floors)
		col12.append(building_materials)
		col13.append(windows)
		col14.append(heating)
		col15.append(year_of_build)
		col16.append(trim_condition)
		col17.append(rent)
		col18.append(property_type)
		col19.append(description)
		col20.append(first_desc)
		col21.append(offer_number)
		col22.append(date_added)
		col23.append(second_desc)
		col24.append(third_desc)
		col25.append(fourth_desc)
		col26.append(first_desc_title)
		col27.append(second_desc_title)
		col28.append(third_desc_title)
		col29.append(fourth_desc_title)
		col30.append(footer)
		print(f"{area};,{rooms};,{market};,{_1st_floor};,{buildyng_type};,{floors};,{building_materials};,{windows};,{heating};,{year_of_build};,{trim_condition};,{rent};,{property_type}")

	driver.quit()

def export():
	data = {'source_': col1,
	'title': col2,
	'address': col3,
	'price': col4,
	'price_per_square_meter': col5,
	'area': col6,
	'rooms': col7,
	'market': col8,
	'buildyng_type': col9,
	'_1st_floor': col10,
	'floors': col11,
	'building_materials': col12,
	'windows': col13,
	'heating': col14,
	'year_of_build': col15,
	'trim_condition': col16,
	'rent': col17,
	'property_type': col18,
	'description': col19,
	'first_desc': col20,
	'offer_number': col21,
	'date_added': col22,
	'second_desc': col23,
	'third_desc': col24,
	'fourth_desc': col25,
	'first_desc_title': col26,
	'second_desc_title': col27,
	'third_desc_title': col28,
	'fourth_desc_title': col29,
	'footer': col30
	}
	df = pd.DataFrame (data, columns = ['source_', 'title', 'address', 'price', 'price_per_square_meter', 'area', 'rooms', 'market', 'buildyng_type', '_1st_floor', 'floors', 'building_materials', 'windows', 'heating', 'year_of_build', 'trim_condition', 'rent', 'property_type', 'description', 'first_desc_title', 'first_desc', 'second_desc_title', 'second_desc', 'third_desc_title', 'third_desc', 'fourth_desc_title', 'fourth_desc'])
	df.to_csv (r'polish_export_data.csv', index = False, header=True)
	print (df)
	
crawl()
export()
