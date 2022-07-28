# Simple currency parser for Google Finance
# You can use any currency/stock, changing EUR const
# Written by Arkadskov Arseniy 28/07/2022
# Distributed under GNU License

import requests
from bs4 import BeautifulSoup
import time

EUR = "https://www.google.com/finance/quote/EUR-RUB?hl=ru"

headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.5060.134 Safari/537.36"}

def parse():
    html = requests.get(EUR, headers) # get page

    soup = BeautifulSoup(html.content, 'html.parser') # parse data
    convert = soup.findAll('div', {'class' : 'YMlKec fxKbKc'})
    price = convert[0].text[0:27] # remove html tags
    print("EUR/RUB price =", price)

def main():
    while(True):
        parse()
        time.sleep(5)

if __name__ == '__main__':
    main()


