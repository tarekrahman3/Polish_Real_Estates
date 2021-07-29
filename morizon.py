from requests_html import HTMLSession
from lxml import html
import pandas as pd
import time

df = pd.read_csv('import.csv',header=0)
list_ = df.links.to_list()

outDict = []

for url in list_:
    session = HTMLSession()
    try:
        resp = session.get(url)
    except:
        pass
    session.close()
    try:
        Title = resp.html.xpath('//section[@class="summaryTop"]//h1/strong')[0].text
    except:
        Title = 'N/A'
    try:
        Type = resp.html.xpath('//div[contains(@class,"summaryTypeTransaction")]')[0].text
    except:
        Type = 'N/A'
    try:
        Price = resp.html.xpath('//li[@class="paramIconPrice"]/em')[0].text
    except:
        Price = 'N/A'
    try:
        Price_per_Square = resp.html.xpath('//li[@class="paramIconPriceM2"]/em')[0].text
    except:
        Price_per_Square = 'N/A'
    try:
        Loan = resp.html.xpath('//a[@id="finpack-mortgage-link"]/@href')
    except:
        Loan = 'N/A'
    try:
        Surface = resp.html.xpath('//li[@class="paramIconLivingArea"]/em')[0].text
    except:
        Surface = 'N/A'
    try:
        Rooms = resp.html.xpath('//li[@class="paramIconNumberOfRooms"]/em')[0].text
    except:
        Rooms = 'N/A'
    try:
        Area = resp.html.xpath('//th[contains(text(),"Powierzchnia użytkowa:")]/following-sibling::td')[0].text
    except:
        Area = 'N/A'
    try:
        Floor = resp.html.xpath('//th[contains(text(),"Piętro:")]/following-sibling::td')[0].text
    except:
        Floor = 'N/A'
    try:
        Number_of_Floors = resp.html.xpath('//th[contains(text(),"Liczba pięter:")]/following-sibling::td')[0].text
    except:
        Number_of_Floors = 'N/A'
    try:
        Market = resp.html.xpath('//th[contains(text(),"Rynek:")]/following-sibling::td')[0].text
    except:
        Market = 'N/A'
    try:
        Offer_Number = resp.html.xpath('//th[contains(text(),"Numer oferty:")]/following-sibling::td')[0].text
    except:
        Offer_Number = 'N/A'
    try:
        Updated = resp.html.xpath('//th[contains(text(),"Zaktualizowano:")]/following-sibling::td')[0].text
    except:
        Updated = 'N/A'
    try:
        Published = resp.html.xpath('//th[contains(text(),"Opublikowano:")]/following-sibling::td')[0].text
    except:
        Published = 'N/A'
    try:
        DescriptionTitle = resp.html.xpath('//div[@class="descriptionContent__title"]/p')[0].text
    except:
        DescriptionTitle = 'N/A'
    try:
        Description = resp.html.xpath('//div[@id="description"]')[0].text
    except:
        Description = 'N/A'
    try:
        Number_of_views = resp.html.xpath('//div[@class="propertyStat"]/p/text()[1]')[0]
    except:
        Number_of_views = 'N/A'

    data = {
        'Time':time.ctime(),
        'Source':url,
        'Title':Title,
        'Type':Type,
        'Price':Price,
        'Price_per_Square':Price_per_Square,
        'Loan':Loan,
        'Surface':Surface,
        'Rooms':Rooms,
        'Area':Area,
        'Floor':Floor,
        'Number_of_Floors':Number_of_Floors,
        'Market':Market,
        'Offer_Number':Offer_Number,
        'Updated':Updated,
        'Published':Published,
        'DescriptionTitle':DescriptionTitle,
        'Description':Description,
        'Number_of_views':Number_of_views
    }
    outDict.append(data)
    print(f"{len(outDict)} : {Title} - {Price}")

pd.DataFrame(outDict).to_csv(f'morizon export at {time.ctime()}.csv')