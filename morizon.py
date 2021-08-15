from requests_html import HTMLSession
from lxml import html
import pandas as pd
import time
import  re
from datetime import date, datetime,timedelta

def DateFormat(String):
    if String==None:
        return None
    Yesterday = date.today() - timedelta(days=1)
    if String=='wczoraj':
        return Yesterday.strftime('%d/%m/%Y')
    PL_EN = {'stycznia': 'January','lutego': 'February','marca': 'March','kwietnia': 'April','maja': 'May','czerwca': 'June',
        'lipca': 'July','sierpnia': 'August','września': 'September','października': 'October','listopada': 'November','grudnia': 'December'}
    for i in [key for key in PL_EN]:
        if i in String.lower():
            return datetime.strptime(String.replace(i,PL_EN[i]),"%d %B %Y").date().strftime('%d/%m/%Y')

def ConvertDateFormat(Dictionary):
    DF = pd.DataFrame(Dictionary)
    for i in range(len(df)):
        A = DF.loc[i, "date_added"]
        B = DF.loc[i, "date_updated"]
        DF.loc[i, "date_added"] = DateFormat(str(A))
        DF.loc[i, "date_updated"]= DateFormat(str(B))
    return DF


def GETandPARSE():
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
            s = PS.replace('\xa0zł',"")
            t = s.replace(',',".")
            u = re.sub(r'\s','',t)
            Price_per_Square = float(u)
            # "return document.getElementsByClassName('paramIconPriceM2')[0].getElementsByTagName('em')[0].innerText"
        except:
            Price_per_Square = None
        try:
            Loan = resp.html.xpath('//a[@id="finpack-mortgage-link"]/@href')[0]
        except:
            Loan = None
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
            Typ_kuchni = resp.html.xpath('//th[contains(text(),"Typ kuchni")]/following-sibling::td')[0].text
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
        except:
            Updated = None
        try:
            Published = resp.html.xpath('//th[contains(text(),"Opublikowano:")]/following-sibling::td')[0].text
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
        try:
            Stan_nieruchomości = resp.html.xpath('//th[contains(text(),"Stan nieruchomości")]/following-sibling::td')[0].text
        except:
            Stan_nieruchomości = None
        try:
            Liczba_sypialni = resp.html.xpath('//th[contains(text(),"Liczba sypialni")]/following-sibling::td')[0].text
        except:
            Liczba_sypialni = None
        try:
            Liczba_łazienek = resp.html.xpath('//th[contains(text(),"Liczba łazienek")]/following-sibling::td')[0].text
        except:
            Liczba_łazienek = None
        try:
            Forma_własności = resp.html.xpath('//th[contains(text(),"Forma własności")]/following-sibling::td')[0].text
        except:
            Forma_własności = None
        try:
            Na_biuro = resp.html.xpath('//th[contains(text(),"Na biuro")]/following-sibling::td')[0].text
        except:
            Na_biuro = None
        try:
            Rodzaj_umowy = resp.html.xpath('//th[contains(text(),"Rodzaj umowy")]/following-sibling::td')[0].text
        except:
            Rodzaj_umowy = None
        try:
            Taras = resp.html.xpath('//th[contains(text(),"Taras")]/following-sibling::td')[0].text
        except:
            Taras = None
        try:
            Czy_przy_mieszkaniu_jest_ogródek = resp.html.xpath('//th[contains(text(),"Czy przy mieszkaniu jest ogródek")]/following-sibling::td')[0].text
        except:
            Czy_przy_mieszkaniu_jest_ogródek = None
        try:
            Wysokość_wnętrza = resp.html.xpath('//th[contains(text(),"Wysokość wnętrza")]/following-sibling::td')[0].text
        except:
            Wysokość_wnętrza = None

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
            'Stan nieruchomości':Stan_nieruchomości,
            'Liczba sypialni':Liczba_sypialni,
            'Liczba łazienek':Liczba_łazienek,
            'Forma własności':Forma_własności,
            'Na biuro':Na_biuro,
            'Rodzaj umowy':Rodzaj_umowy,
            'Taras':Taras,
            'Czy przy mieszkaniu jest ogródek':Czy_przy_mieszkaniu_jest_ogródek,
            'Wysokość wnętrza':Wysokość_wnętrza
        }
        outDict.append(data)
        print(f"{len(outDict)} : {Title} - {Price}")

df = pd.read_csv(input('type import filename: '),header=0)
list_ = df.links.to_list()
outDict = []
GETandPARSE()
ConvertDateFormat(outDict).to_csv(f'morizon export at {time.ctime()}.csv',index=False)
