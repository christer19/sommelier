import logging

import requests
from bs4 import BeautifulSoup
from functional import seq
import urllib.parse
import time

from sommelier.foo import bar


class LidlWine:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'LidlWine[{self.name} ({self.price} zł)]'

    def __repr__(self):
        return self.__str__()


def run():
    # set up logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')
    logging.info('Application Start')

    logging.info('Hello World! It is Sommelier time!')

    url = 'https://winnicalidla.pl/wszystkie-wina/czerwone.html?price=19-30'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # TODO Can I somehow chain html components in single find?
    pages_count = len(soup.find('div', class_='pages').find_all('li')) - 1
    logging.info(f'There are {pages_count} pages found')
    lidl_wines = []
    for page_number in range(1, pages_count + 1):
        single_page_url = f'https://winnicalidla.pl/wszystkie-wina/czerwone.html?p={page_number}&price=19-30'
        single_page = requests.get(single_page_url)
        single_page_soup = BeautifulSoup(single_page.content, 'html.parser')
        lidl_wines.extend(process_single_vineyard_page(single_page_soup))
    logging.info(f'Found {len(lidl_wines)} wines')
    logging.info(lidl_wines)

    for lidl_wine in lidl_wines:
        # query = lidl_wine.name
        # encoded_wine_name = urllib.parse.quote(query)
        # url = f'https://www.vivino.com/search/wines?q={encoded_wine_name}'
        # print(url)
        # page = requests.get(url)
        if lidl_wine:
            page = bar(lidl_wine.name)
            time.sleep(1)
            # print(page.content)
            soup = BeautifulSoup(page.content, 'html.parser')
            first_found_wine_elem = soup.find('div', class_='wine-card__content')
            # print(first_found_wine_elem.prettify())
            rating_elem = first_found_wine_elem.find('div', class_='average__number')
            print(f'Wino:{lidl_wine.name} cena: {lidl_wine.price} rating: {rating_elem.text}')


    logging.info('Application End')


def process_single_vineyard_page(soup):
    wine_elements = soup.find_all('li', class_='item col-lg-12')
    return seq(wine_elements).map(lambda wine: process_single_wine_element(wine)).to_list()


def process_single_wine_element(wine):
    price_element = wine.find('span', class_='price')
    if price_element:
        wine_name = wine.find('h2', class_='product-name').find('a')['title']
        price = f'{price_element.text[:-2]},{price_element.text[-2:]}'
        return LidlWine(wine_name, price)
