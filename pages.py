import requests
import pandas as pd
from requests_html import HTMLSession
from lxml import html

df = pd.read_csv('pages.csv', header=0)
list_ = df.links.to_list()



headers ={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}



session = HTMLSession()

a =[]
for i in list_:
    resp = requests.get(i,headers=headers)
    tree = html.fromstring(resp.content)
    url = tree.xpath('//section[contains(@class,"single-result__content")]/header/a[starts-with(@href,"https://www.morizon.pl") and @title=""]/@href')
    for s in url:
        a.append({'page':i,'links':s})
        print(s)


pd.DataFrame(a).to_csv('list.csv')
