from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import pandas as pd
import os
import random
import time
options = Options()
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation","enable-logging"])
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

def change_ip(driver):
    driver.delete_all_cookies()
    locations = ['Seine', 'Castle', 'Canal', 'Fjord', 'Alphorn', 'Crumpets', 'Custard', 'Ataturk', 'Victoria']
    os.system(f"windscribe connect {locations[random.randrange(len(locations))]}")
    time.sleep(4)
    driver.delete_all_cookies()

def driver_start():
    driver = webdriver.Chrome(options=options, executable_path='/home/tarek/my_Projects $$ ****/chromedriver')
    stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32", webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True,)
    driver.maximize_window()
    return driver

def get_xpath_text(driver,xpath):
    try:
        return driver.find_element_by_xpath(xpath).text
    except:
        return None

def click_more_description(driver):
    c = driver.find_element_by_xpath("//span[text()='Pokaż więcej']").get_attribute('class')
    script = f"document.getElementsByClassName('{c}')[0].click()"
    driver.execute_script(script)

def GET_PARSE(driver,url):
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Pokaż więcej']")))
    except:
        pass
    if get_xpath_text(driver, '//h1')=='403 ERROR':
        os.system('windscribe disconnect')
        driver.refresh()
        time.sleep(3)
    if get_xpath_text(driver, '//*[@id="onetrust-accept-btn-handler"]') != None:
        driver.execute_script("document.getElementById('onetrust-accept-btn-handler').click()")
    try:
        click_more_description(driver)
    except:
        pass
    title = get_xpath_text(driver, '//h1')
    address = get_xpath_text(driver, "//a[@href='#map']")
    price = get_xpath_text(driver, "//strong[contains(@data-cy, 'Price')]")
    price_per_square_meter = get_xpath_text(driver, '//div[@aria-label="Cena za metr kwadratowy"]')
    area = get_xpath_text(driver, "//div[contains(@aria-label, 'Powierzchnia')]/div/following-sibling::div")
    rooms = get_xpath_text(driver, "//div[contains(@aria-label, 'Liczba pokoi')]/div/following-sibling::div")
    buildyng_type = get_xpath_text(driver, "//div[contains(@aria-label, 'Rodzaj zabudowy')]/div/following-sibling::div")
    floor = get_xpath_text(driver, "//div[contains(@aria-label, 'Piętro')]/div/following-sibling::div")
    total_floors = get_xpath_text(driver, "//div[contains(@aria-label, 'Liczba pięter')]/div/following-sibling::div")
    year_of_build = get_xpath_text(driver, "//div[contains(@aria-label, 'Rok budowy')]/div/following-sibling::div")
    date_added = get_xpath_text(driver, '//div[contains(text(), "Data dodania")]')
    date_updated = get_xpath_text(driver, '//div[contains(text(), "Data aktualizacji")]')
    description = get_xpath_text(driver, "//div[contains(@data-cy, 'adPageAdDescription')]")
    Media = get_xpath_text(driver, "//h3[text()='media']/following-sibling::ul")
    Zabezpieczenia = get_xpath_text(driver, "//h3[text()='zabezpieczenia']/following-sibling::ul")
    Wyposażenie = get_xpath_text(driver, "//h3[text()='wyposażenie']/following-sibling::ul")
    Informacje_Dodatkowe = get_xpath_text(driver, "//h3[text()='informacje dodatkowe']/following-sibling::ul")
    Materiał_budynku = get_xpath_text(driver, "//div[contains(@aria-label, 'Materiał budynku')]/div/following-sibling::div")
    Forma_własności = get_xpath_text(driver, "//div[contains(@aria-label, 'Forma własności')]/div/following-sibling::div")
    Okna = get_xpath_text(driver, "//div[contains(@aria-label, 'Okna')]/div/following-sibling::div")
    Stan_wykończenia = get_xpath_text(driver, "//div[contains(@aria-label, 'Stan wykończenia')]/div/following-sibling::div")
    Ogrzewanie = get_xpath_text(driver, "//div[contains(@aria-label, 'Ogrzewanie')]/div/following-sibling::div")
    Czynsz = get_xpath_text(driver, "//div[contains(@aria-label, 'Czynsz')]/div/following-sibling::div")
    Rynek = get_xpath_text(driver, "//div[contains(@aria-label, 'Rynek')]/div/following-sibling::div")
    Nr_oferty_w_Otodom = get_xpath_text(driver, "//div[contains(text(),'Nr oferty w Otodom:')]")
    Nr_oferty_w_biurze_nieruchomości = get_xpath_text(driver, "//div[contains(text(),'Nr oferty w biurze nieruchomości')]")
    data = {
        'time' :                             time.ctime(),
        'source' :                           url,
        'title' :                            title,
        'address' :                          address,
        'price' :                            price,
        'price_per_square_meter' :           price_per_square_meter,
        'area' :                             area,
        'rooms' :                            rooms,
        'buildyng_type' :                    buildyng_type,
        'floor' :                            floor,
        'total_floors' :                     total_floors,
        'year_of_build' :                    year_of_build,
        'date_added' :                       date_added,
        'date_updated' :                     date_updated,
        'description' :                      description,
        'Media' :                            Media,
        'Zabezpieczenia' :                   Zabezpieczenia,
        'Wyposażenie' :                      Wyposażenie,
        'Informacje Dodatkowe' :             Informacje_Dodatkowe,
        'Materiał budynku' :                 Materiał_budynku,
        'Forma własności' :                  Forma_własności,
        'Okna' :                             Okna,
        'Stan wykończenia' :                 Stan_wykończenia,
        'Ogrzewanie' :                       Ogrzewanie,
        'Czynsz' :                           Czynsz,
        'Rynek' :                            Rynek,
        'Nr oferty w Otodom' :               Nr_oferty_w_Otodom,
        'Nr oferty w biurze nieruchomości' : Nr_oferty_w_biurze_nieruchomości
    }
    return data

def main():
    urls = pd.read_csv('import.csv').links.tolist()
    export=[]
    driver = driver_start()
    try:
        i=1
        for url in urls:
            change_ip(driver) if i%50==0 else ''
            DATA = GET_PARSE(driver,url)
            print(f"{i} | {DATA['title']}")
            export.append(DATA)
            i+=1
        driver.quit()
        os.system("windscribe disconnect")
    finally:
        pd.DataFrame(export).to_csv(f'export at {time.ctime()}.csv', index=False)

if __name__ == '__main__':
    main()