import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3
import time
import random

conn = sqlite3.connect('computers.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS computers (
info VARCHAR(150),price VARCHAR(50))''')


for num in range(1, 6):
    url = f"https://alta.ge/notebooks-page-{num}.html"
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_info = soup.find('div', class_='grid-list')
    all_computers=all_info('div', class_="ty-grid-list__item-name")
    all_prices = all_info.find_all('span', class_="ty-price-num")
    prices = []
    names = []
    for each in all_prices:
        prices.append(each.text)
    for each in all_computers:
        names.append(each.text)

    for i in range(1,len(names)):
        cur.execute('INSERT INTO computers (info,price) VALUES(?,?)', (names[i],prices[i]))
        conn.commit()
    time.sleep(random.randint(10, 20))
cur.close()