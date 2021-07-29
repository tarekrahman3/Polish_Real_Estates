
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import pandas as pd
import csv
import os
import random
import time
A = (
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0"
)
options = Options()
#options.headless = True
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation","enable-logging"])
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument('user-data-dir=Profile')
start_time = time.perf_counter()
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
col31 = []
col32 = []
col33 = []
col34 = []
col35 = []
col36 = []
graph_data = []
parsed_moment =[]
df = pd.read_csv('import.csv', header=0)
list_ = df.links.to_list()

def driver_start():
	driver = webdriver.Chrome(options=options, executable_path='/home/tarek/my_Projects/chromedriver')
	
	#driver.set_window_size(1366, 768)
	driver.maximize_window()
	return driver

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def graphdata():
	for i in range(1):
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2+15);")
	circles = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'circle.recharts-dot.recharts-line-dot')))
	grph_data = []
	for circle in circles:
		actions = ActionChains(driver)
		actions.move_to_element(circle).perform()
		time.sleep(0.005)
		dat = driver.find_element_by_xpath('//div[contains(@class,"recharts-tooltip-wrapper")]').text
		grph_data.append(dat)
	
	return grph_data

driver = driver_start()



def crawl():
	#driver.get('https://www.otodom.pl/')
	#input('Accept Cookies to continue')
	for i in list_:
		source_ = f"{i}"
		#driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": A[random.randrange(len(A))]})
		driver.get(i)
		try:
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable(By.XPATH, "//span[text()='Pokaż więcej']"))
		except:
			pass
		try:
			driver.find_element_by_id('onetrust-accept-btn-handler').click()
		except:
			pass
		try:
			h1 = driver.find_element_by_xpath('//h1').text
		except:
			pass
		if h1=='403 ERROR':
			locations = ['Seine','Castle','Canal','Fjord','Alphorn','Crumpets','Custard','Ataturk','Victoria']
			
			driver.delete_all_cookies()
			
			os.system(f"windscribe connect {locations[random.randrange(len(locations))]}")
			time.sleep(4)
			'''
			timeslept = 10
			for t in range(18):
				time.sleep(10)
				print(f"time slept: {timeslept}")
				timeslept +=10 '''
			driver.get(i)
			time.sleep(4)
			try:
				driver.find_element_by_id('onetrust-accept-btn-handler').click()
			except:
				pass
		else:
			pass
		try:
			title = driver.find_element_by_xpath("//h1[contains(@data-cy, 'adPageAdTitle')]").text
		except:
			title = 'N/A'
		'''try:
			driver.find_element_by_xpath('//button[text()="Akceptuję"]').click()
		except:
			pass'''
		
		'''try:
			graph_info = graphdata()
		except:
			graph_info = "N/A"'''
		try:
			# click on more description button 
			bn_class = driver.find_element_by_xpath("//span[text()='Pokaż więcej']").get_attribute('class')
			driver.execute_script(f"var b = document.getElementsByClassName('{bn_class}');b[0].click();")
		except:
			print('Deails click failed')
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
			address = driver.find_element_by_xpath("//a[@href='#map']").text
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
			date_added = driver.find_element_by_xpath('//div[contains(text(), "Data dodania")]').text	
		except:
			date_added = 'N/A'
		try:
			footer = driver.find_element_by_xpath('//div[contains(text(), "Data aktualizacji")]').text
		except:
			footer = 'N/A'

		try:
			print('Checking Private Agent')
			private = driver.find_element_by_xpath('//button[text()="Pokaż numer"]')
			driver.execute_script(f"var b = document.getElementsByClassName('{private.get_attribute('class')}');b[0].click();")
			try:
				WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located(By.XPATH, '//*[@aria-label="Zamknij" and @role="button" and @data-cy="close-modal"]'))
			except:
				pass
			checking=check_exists_by_xpath('//*[@aria-label="Zamknij" and @role="button" and @data-cy="close-modal"]')
			if checking==True:
				# it's an agency!!
				agency_name = driver.find_element_by_xpath('//*[@aria-label="Zamknij"]/../child::div/div[2]/strong').text
				agency_phone_number = driver.find_element_by_xpath('//*[@aria-label="Zamknij"]/../child::div/div[2]//a[contains(@href,"tel")]').get_attribute('href')
				agency_agent_phone_number = driver.find_element_by_xpath('//*[@aria-label="Zamknij"]/following::div[contains(@class,"phoneNumber")]/a').get_attribute('href')
				agency_agent_name = driver.find_element_by_xpath('//*[@aria-label="Zamknij"]/..//span[contains(@class,"contactPersonName")]').text
				private_name = ''
				private_number = ''
			elif checking==False:
				# its private
				private_name = driver.find_element_by_xpath('//span[contains(@class,"contactPersonName")]').text
				private_number = driver.find_element_by_xpath('//div[contains(@class,"phoneNumber")]/a').get_attribute('href')
				agency_name = ''
				agency_phone_number = ''
				agency_agent_phone_number = ''
				agency_agent_name = ''
		except:
			agency_name = ''
			agency_phone_number = ''
			agency_agent_phone_number = ''
			agency_agent_name = ''
			private_name = ''
			private_number = ''
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
		col31.append(agency_name)
		col32.append(agency_phone_number)
		col35.append(agency_agent_phone_number)
		col36.append(agency_agent_name)
		col33.append(private_name)
		col34.append(private_number)
		#graph_data.append(graph_info)
		parsed_moment.append(time.ctime())
		print(f"{len(col2)+1}: {title}")

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
	'footer': col30,
	'agency_name':col31,
	'agency_number':col32,
	'private_name':col33,
	'private_number':col34,
	'agency_agent_phone_number':col35,
	'agency_agent_name':col36,
	#'graph_info':graph_data,
	'parsed_moment': parsed_moment
	}
	df = pd.DataFrame (data, columns = ['parsed_moment','source_', 'title', 'address', 'price', 'price_per_square_meter',
	'area', 'rooms', 'market', 'buildyng_type', '_1st_floor', 'floors', 'building_materials', 'windows', 'heating', 'year_of_build', 'trim_condition', 'rent', 'property_type',
	'description', 'first_desc_title', 'first_desc', 'second_desc_title', 'second_desc', 'third_desc_title', 'third_desc', 'fourth_desc_title', 'fourth_desc',
	'agency_name', 'agency_number','agency_agent_name','agency_agent_phone_number','private_name', 'private_number','footer','date_added'])
	exprtTime = time.ctime()
	fname = f"polish_export at{exprtTime}.csv"
	df.to_csv (fname, index = False, header=True)
	print(df)



try:
	crawl()
	export()
except:
	export()

end_time = time.perf_counter()
print(end_time-start_time)
