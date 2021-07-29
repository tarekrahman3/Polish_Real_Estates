
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import pandas as pd
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument('--ignore-certificate-errors')
start_time = time.perf_counter()

driver = webdriver.Chrome(options=options, executable_path='/home/tarek/my_Projects/chromedriver')

driver.maximize_window()

def parse(driver,dictionary_list,source_url):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//h1/span[@itemprop="name"]')))
    except:
        pass
    source = source_url
    try:
        Title = driver.find_element_by_xpath('//h1/span[@itemprop="name"]').text
    except:
        Title = 'N/A'
    try:
        Address = driver.find_element_by_xpath('//div[@class="detials__map__location"]').text
    except:
        Address = 'N/A'
    try:
        Area = driver.find_element_by_xpath('//p[text()="POWIERZCHNIA"]/following-sibling::p').text
    except:
        Area = ''
    try:
        Rooms = driver.find_element_by_xpath('//p[text()="LICZBA POKOI"]/following-sibling::p').text
    except:
        Rooms = 'N/A'
    try:
        Parking = driver.find_element_by_xpath('//p[text()="PARKING"]/following-sibling::p[text()]').text
    except:
        Parking = 'N/A'
    try:
        Price = driver.find_element_by_xpath('//span[@itemprop="price"]').get_attribute('content')
    except:
        Price = 'N/A'
    try:
        Floor = driver.find_element_by_xpath('//p[text()="PIĘTRO"]/following-sibling::p').text
    except:
        Floor = 'N/A'
    try:
        Price_Per_Square_Meter = driver.find_element_by_xpath('//span[@class="summary__subtitle summary__subtitle--price"]').text
    except:
        Price_Per_Square_Meter = 'N/A'
    try:
        MoreDescriptionButton = driver.find_element_by_xpath('//button[contains(@class,"description__button")]').get_attribute('class')
        driver.execute_script(f"document.getElementsByClassName('{MoreDescriptionButton}')[0].click()")
        Description = driver.find_element_by_xpath('//div[@class="description__panel"]').text
    except:
        Description = 'N/A'
    try:
        Category = driver.find_element_by_xpath('//span[text()="Kategoria"]/following-sibling::span').text
    except:
        Category = 'N/A'
    try:
        Dostępne_od = driver.find_element_by_xpath('//span[text()="Dostępne od"]/following-sibling::span').text
    except:
        Dostępne_od = 'N/A'
    try:
        Lokalizacja = driver.find_element_by_xpath('//span[text()="Lokalizacja"]/following-sibling::span').text
    except:
        Lokalizacja = 'N/A'
    try:
        Cena = driver.find_element_by_xpath('//span[text()="Cena"]/following-sibling::span').text
    except:
        Cena = 'N/A'
    try:
        Cena_za_m = driver.find_element_by_xpath('//span[text()="Cena za m"]/following-sibling::span').text
    except:
        Cena_za_m = 'N/A'
    try:
        Typ_budynku = driver.find_element_by_xpath('//span[text()="Typ budynku"]/following-sibling::span').text
    except:
        Typ_budynku = 'N/A'
    try:
        Materiał = driver.find_element_by_xpath('//span[text()="Materiał "]/following-sibling::span').text
    except:
        Materiał = 'N/A'
    try:
        Liczba_pokoi = driver.find_element_by_xpath('//span[text()="Liczba pokoi "]/following-sibling::span').text
    except:
        Liczba_pokoi = 'N/A'
    try:
        Przeznaczenie = driver.find_element_by_xpath('//span[text()="Przeznaczenie "]/following-sibling::span').text
    except:
        Przeznaczenie = 'N/A'
    try:
        Numer_oferty = driver.find_element_by_xpath('//span[text()="Numer oferty"]/following-sibling::span').text
    except:
        Numer_oferty = 'N/A'
    try:
        Pietro = driver.find_element_by_xpath('//span[text()="Piętro "]/following-sibling::span').text
    except:
        Pietro ='N/A'
    try:
        Liczba_pięter_w_budynku = driver.find_element_by_xpath('//span[text()="Liczba pięter w budynku "]/following-sibling::span').text
    except:
        Liczba_pięter_w_budynku = 'N/A'
    try:
        Rok_budowy = driver.find_element_by_xpath('//span[text()="Rok budowy "]/following-sibling::span').text
    except:
        Rok_budowy = 'N/A'
    try:
        Powierzchnia_całkowita = driver.find_element_by_xpath('//span[text()="Powierzchnia całkowita"]/following-sibling::span').text
    except:
        Powierzchnia_całkowita = 'N/A'
    try:
        Visitor_Counter = driver.find_element_by_xpath('//div[@class="visits-counter"]').text
    except:
        Visitor_Counter = 'N/A'
    data = {
        'Time':time.ctime(),
        'Source':source_url,
        'Title':Title,
        'Address':Address,
        'Area':Area,
        'Floor':Floor,
        'Rooms':Rooms,
        'Parking':Parking,
        'Price':Price,
        'Price_Per_Square_Meter':Price_Per_Square_Meter,
        'Description':Description,
        'Category':Category,
        'Dostępne_od':Dostępne_od,
        'Lokalizacja':Lokalizacja,
        'Cena':Cena,
        'Cena_za_m':Cena_za_m,
        'Typ_budynku':Typ_budynku,
        'Materiał':Materiał,
        'Liczba_pokoi':Liczba_pokoi,
        'Przeznaczenie':Przeznaczenie,
        'Numer_oferty':Numer_oferty,
        'Pietro':Pietro,
        'Liczba_pięter_w_budynku':Liczba_pięter_w_budynku,
        'Rok_budowy':Rok_budowy,
        'Powierzchnia_całkowita':Powierzchnia_całkowita,
        'Visitor_Counter':Visitor_Counter
    }
    print(f"{len(dictionary_list)+1}  -  {Title} : {Price}")
    return data

df = pd.read_csv('import.csv',header=0)
list_ = df.links.to_list()

dictionary_list = []

try:
    for i in list_ :
        driver.get('https://www.domiporta.pl' + i)
        property_info = parse(driver,dictionary_list,i)
        dictionary_list.append(property_info)
finally:
    driver.quit()
    pd.DataFrame(dictionary_list).to_csv(f"domiporta export at {time.ctime()}")