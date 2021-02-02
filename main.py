# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import re
from bs4 import BeautifulSoup

source = requests.get("https://search.shopping.naver.com/search/all?query=MJJSQ02LX").text
soup = BeautifulSoup(source, "html.parser")
boxs = soup.find_all(class_=re.compile("basicList_item"))

datas = []

for box in boxs:
    price = box.find(class_=re.compile("price_num")).string
    market = box.find(class_=re.compile("basicList_mall_title")).find(class_=re.compile("basicList_mall"))
    market_name = market.string
    market_url = market.get('href')

    datas.append([price, market_name, market_url])

for data in datas:
    print(data.pop(0))