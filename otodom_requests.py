from requests_html import HTMLSession
from lxml import html
import pandas as pd
import os
import time
import random
import re

def change_ip():
    locations = ['Seine', 'Castle', 'Canal', 'Fjord', 'Alphorn', 'Crumpets', 'Custard', 'Ataturk', 'Victoria']
    os.system(f"windscribe connect {locations[random.randrange(len(locations))]}")
    time.sleep(4)

translate_dict = {
    'godzin temu': 'hours ago',
    'miesiąc':'months',
    'miesiąc temu':'one month',
    'dni':'days',
    'dzień':'one day',
    'rok temu':'one year ago',
    'lata temu':'years ago'
    }

def render_js_and_click_more_description(response):
    response.html.render(timeout=0, keep_page=False, reload=True)
    try:
        c = response.html.xpath("//span[text()='Pokaż więcej']/@class")[0]
        script = f"document.getElementsByClassName('{c}')[0].click()"
        response.html.render(script=script)
    except:
        pass

def __(response, xpath, index):
    try:
        return response.html.xpath(xpath)[index].text
    except:
        return None

def GET_PARSE(url):
    session = HTMLSession()
    response = session.get(url, timeout=20)
    print(response.status_code)
    render_js_and_click_more_description(response)
    #######
    p =                                      __(response, "//strong[contains(@data-cy, 'Price')]", 0)
    price = int(re.sub('\D', '', p)) if p != None else p
    #######
    ppsm =                                   __(response, '//div[@aria-label="Cena za metr kwadratowy"]', 0)
    if ppsm == '':
        price_per_square_meter = None
    elif ppsm == None:
        price_per_square_meter = None
    elif ppsm != None:
        price_per_square_meter = int(re.sub('\D', '', ppsm))
    #######
    a =                                      __(response, "//div[contains(@aria-label, 'Powierzchnia')]/div/following-sibling::div", 0)
    area = float(re.sub('\s.+', '', a.replace(',', '.'))) if a != None else a
    #######
    r_ =                                     __(response, "//div[contains(@aria-label, 'Liczba pokoi')]/div", 1)
    rooms = int(r_) if r_ != None else r_
    #######
    tf =                                     __(response, "//div[contains(@aria-label, 'Liczba pięter')]/div", 1)
    total_floors = int(tf) if tf != None else tf
    #######
    yb =                                     __(response, "//div[contains(@aria-label, 'Rok budowy')]/div", 1)
    year_of_build = int(yb) if yb != None else yb
    #######
    da =                                     __(response, '//div[contains(text(), "Data dodania")]', 0)
    date_added = re.sub('.+: ', '', da) if da != None else da
    #######
    du =                                     __(response, '//div[contains(text(), "Data aktualizacji")]', 0)
    date_updated = re.sub('.+: ', '', du) if du != None else du
    #######
    NrO =                                    __(response, "//div[contains(text(),'Nr oferty w Otodom:')]", 0)
    Nr_oferty_w_Otodom = re.sub('.+: ', '', NrO) if NrO != None else NrO
    #######
    NrB =                                    __(response, "//div[contains(text(),'Nr oferty w biurze nieruchomości')]", 0)
    Nr_oferty_w_biurze_nieruchomości = NrB.replace('Nr oferty w biurze nieruchomości ', '') if NrB != None else NrB
    #######
    data = {
        'time':                                 time.ctime(),
        'source':                               url,
        'title' :                            __(response, "//h1", 0),
        'address' :                          __(response, "//a[@href='#map']", 0),
        'price' :                               price,
        'price_per_square_meter' :              price_per_square_meter,
        'area' :                                area,
        'rooms' :                               rooms,
        'buildyng_type' :                    __(response, "//div[contains(@aria-label, 'Rodzaj zabudowy')]/div", 1),
        'floor' :                            __(response, "//div[contains(@aria-label, 'Piętro')]/div", 1),
        'total_floors' :                        total_floors,
        'year_of_build' :                       year_of_build,
        'date_added' :                          date_added,
        'date_updated' :                        date_updated,
        'description' :                      __(response, "//div[contains(@data-cy, 'adPageAdDescription')]", 0),
        'Media' :                            __(response, "//h3[text()='media']/following-sibling::ul", 0),
        'Zabezpieczenia' :                   __(response, "//h3[text()='zabezpieczenia']/following-sibling::ul", 0),
        'Wyposażenie' :                      __(response, "//h3[text()='wyposażenie']/following-sibling::ul", 0),
        'Informacje Dodatkowe' :             __(response, "//h3[text()='informacje dodatkowe']/following-sibling::ul", 0),
        'Materiał budynku' :                 __(response, "//div[contains(@aria-label, 'Materiał budynku')]/div", 1),
        'Forma własności' :                  __(response, "//div[contains(@aria-label, 'Forma własności')]/div", 1),
        'Okna' :                             __(response, "//div[contains(@aria-label, 'Okna')]/div", 1),
        'Stan wykończenia' :                 __(response, "//div[contains(@aria-label, 'Stan wykończenia')]/div", 1),
        'Ogrzewanie' :                      __(response, "//div[contains(@aria-label, 'Ogrzewanie')]/div", 1),
        'Czynsz' :                           __(response, "//div[contains(@aria-label, 'Czynsz')]/div", 1),
        'Rynek' :                            __(response, "//div[contains(@aria-label, 'Rynek')]/div", 1),
        'Nr oferty w Otodom' :                  Nr_oferty_w_Otodom,
        'Nr oferty w biurze nieruchomości' :    Nr_oferty_w_biurze_nieruchomości
        }
    session.close()
    return data


urls = pd.read_csv('import.csv').links.tolist()
export=[]
i=1
for url in urls:
    #change_ip() if i%50==0 else ''
    data = GET_PARSE(url)
    export.append(data)
    print(len(export))
    i+=1

#os.system("windscribe disconnect")
pd.DataFrame(export).to_csv(f'export at {time.ctime()}.csv', index=False)