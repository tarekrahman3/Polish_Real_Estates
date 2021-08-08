from requests_html import HTMLSession
from lxml import html
import pandas as pd
import time
import  re
df = pd.read_csv('import.csv',header=0)
list_ = df.links.to_list()
outDict = []

for url in list_:
    session = HTMLSession()
    try:
        resp = session.get(url,timeout=10)
    except:
        pass
    session.close()
    try:
        Title = resp.html.xpath('//section[@class="summaryTop"]//h1/strong')[0].text
    except:
        Title = None
    try:
        Type = resp.html.xpath('//div[contains(@class,"summaryTypeTransaction")]')[0].text
    except:
        Type = None
    try:
        P = resp.html.xpath('//li[@class="paramIconPrice"]/em')[0].text
        Price = (re.sub(r'\D','',P))
    except:
        Price = None
    try:
        PS = resp.html.xpath('//li[@class="paramIconPriceM2"]/em')[0].text
        Price_per_Square=int(re.sub(r'\D','',PS))
    except:
        Price_per_Square = None
    try:
        Loan = resp.html.xpath('//a[@id="finpack-mortgage-link"]/@href')[0]
    except:
        Loan = None
    try:
        S = resp.html.xpath('//li[@class="paramIconLivingArea"]/em')[0].text
        S=S.replace(',','.')
        Surface=float(re.sub(r' .+','',S))
    except:
        Surface = None
    try:
        Rooms = resp.html.xpath('//li[@class="paramIconNumberOfRooms"]/em')[0].text
    except:
        Rooms = None
    try:
        A = resp.html.xpath('//th[contains(text(),"Powierzchnia użytkowa:")]/following-sibling::td')[0].text
        A = A.replace(',','.')
        Area=float(re.sub(r' .+','',A))
    except:
        Area = None
    try:
        F = resp.html.xpath('//th[contains(text(),"Piętro:")]/following-sibling::td')[0].text
        F=re.sub(r' /.+','',F)
        if F=='parter':
            Floor=int(0)
        else:
            Floor = int(F)
    except:
        Floor = None
    try:
        Number_of_Floors = resp.html.xpath('//th[contains(text(),"Liczba pięter:")]/following-sibling::td')[0].text
    except:
        Number_of_Floors = None
    try:
        Market = resp.html.xpath('//th[contains(text(),"Rynek:")]/following-sibling::td')[0].text
    except:
        Market = None
    try:
        Typ_kuchni = resp.html.xpath('//th[contains(text(),"Typ kuchni:")]/following-sibling::td')[0].text
    except:
        Typ_kuchni = None
    try:
        Czy_łazienka_z_WC = resp.html.xpath('//th[contains(text(),"Czy łazienka z WC:")]/following-sibling::td')[0].text
    except:
        Czy_łazienka_z_WC = None
    try:
        Balkon = resp.html.xpath('//th[contains(text(),"Balkon:")]/following-sibling::td')[0].text
    except:
        Balkon = None
    try:
        Typ_budynku = resp.html.xpath('//th[contains(text(),"Typ budynku:")]/following-sibling::td')[0].text
    except:
        Typ_budynku = None
    try:
        Rok_budowy = resp.html.xpath('//th[contains(text(),"Rok budowy:")]/following-sibling::td')[0].text
    except:
        Rok_budowy= None
    try:
        Offer_Number = resp.html.xpath('//th[contains(text(),"Numer oferty:")]/following-sibling::td')[0].text
    except:
        Offer_Number = None
    try:
        Updated = resp.html.xpath('//th[contains(text(),"Zaktualizowano:")]/following-sibling::td')[0].text
        #Updated=translator.translate(Upd, src='pl')
    except:
        Updated = None
    try:
        Published = resp.html.xpath('//th[contains(text(),"Opublikowano:")]/following-sibling::td')[0].text
        #Published=translator.translate(Pub, src='pl')
    except:
        Published = None
    try:
        DescriptionTitle = resp.html.xpath('//div[@class="descriptionContent__title"]/p')[0].text
    except:
        DescriptionTitle = None
    try:
        Description = resp.html.xpath('//div[@id="description"]')[0].text
    except:
        Description = None
    try:
        Number_of_views = resp.html.xpath('//div[@class="propertyStat"]/p/text()[1]')[0]
    except:
        Number_of_views = None
    try:
        Stan_budynku = resp.html.xpath('//th[contains(text(),"Stan budynku")]/following-sibling::td')[0].text
    except:
        Stan_budynku = None
    try:
        Ogrzewanie = resp.html.xpath('//h3[text()="Ogrzewanie"]/following-sibling::p[1]')[0].text
    except:
        Ogrzewanie =None
    try:
        Udogodnienia = resp.html.xpath('//h3[text()="Udogodnienia"]/following-sibling::p[1]')[0].text
    except:
        Udogodnienia = None
    try:
        Wyposażenie =resp.html.xpath('//h3[text()="Wyposażenie"]/following-sibling::p[1]')[0].text
    except:
        Wyposażenie = None
    try:
        Media = resp.html.xpath('//h3[text()="Media"]/following-sibling::p[1]')[0].text
    except:
        Media = None
    try:
        Materiał_budowlany = resp.html.xpath('//th[contains(text(),"Materiał budowlany")]/following-sibling::td')[0].text
    except:
        Materiał_budowlany = None
    try:
        Image_1 = resp.html.xpath('//img[@id="imageBig"]/@src')[0]
    except:
        Image_1 = None
    try:
        Image_2 = resp.html.xpath('//ul[@class="list-unstyled list-inline imageBoxList"]/li/img/@src')[0]
    except:
        Image_2 = None
    try:
        Image_3 = resp.html.xpath('//ul[@class="list-unstyled list-inline imageBoxList"]/li/img/@src')[1]
    except:
        Image_3 = None
    try:
        Image_4 = resp.html.xpath('//ul[@class="list-unstyled list-inline imageBoxList"]/li/img/@src')[2]
    except:
        Image_4 = None
    try:
        Image_5 = resp.html.xpath('//ul[@class="list-unstyled list-inline imageBoxList"]/li/img/@src')[3]
    except:
        Image_5 = None
    data = {
        'Source':url,
        'Time':time.ctime(),
        'address':Title,
        'price':Price,
        'price_per_square_meter':Price_per_Square,
        'area':Area,
        'rooms':Rooms,
        'buildyng_type':Typ_budynku,
        'floor':Floor,
        'total_floors':Number_of_Floors,
        'year_of_build':Rok_budowy,
        'date_added':Published,
        'date_updated':Updated,
        'description':Description,
        'DescriptionTitle':DescriptionTitle,
        'Type':Type,
        'Loan':Loan,
        'Market':Market,
        'Offer_Number':Offer_Number,
        'Number_of_views':Number_of_views,
        'Image_1':Image_1,
        'Image_2':Image_2,
        'Image_3':Image_3,
        'Image_4':Image_4,
        'Image_5':Image_5,
        'Typ_kuchni':Typ_kuchni,
        'Czy_łazienka_z_WC':Czy_łazienka_z_WC,
        'Balkon':Balkon,
        'Stan budynku': Stan_budynku,
        'Ogrzewanie':Ogrzewanie,
        'Udogodnienia':Udogodnienia,
        'Wyposażenie':Wyposażenie,
        'Media': Media,
        'Materiał_budowlany':Materiał_budowlany,
    }
    outDict.append(data)
    print(f"{len(outDict)} : {Title} - {Price} - {Updated}")

pd.DataFrame(outDict).to_csv(f'morizon export at {time.ctime()}.csv')
