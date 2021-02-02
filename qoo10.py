import requests
import re
from bs4 import BeautifulSoup


source = requests.get("https://globalshop.qoo10.com/gmkt.inc/search/?keyword=%EB%AF%B8%EC%A7%80%EC%95%84%20%EA%B0%80%EC%8A%B5%EA%B8%B0").text
soup = BeautifulSoup(source, "html.parser")
boxs = soup.select('ul#search_result_item_list > li')


datas = []

for box in boxs:

    title = box.select_one('dt.sbj > a')['title']
    market_url = box.select_one('dt.sbj > a')['href']
    price = box.select_one('dd.prc_area > strong.prc').string

    datas.append([price, title, market_url])

for data in datas:
    print(data.pop(0))