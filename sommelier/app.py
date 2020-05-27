import logging

import requests
from bs4 import BeautifulSoup


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
    wine_elements = soup.find_all('li', class_='item col-lg-12')
    lidl_wines = []
    # TODO Add support for pagination on lidl page
    print(f'Found {len(wine_elements)} wines')
    for wine in wine_elements:

        wine_name = wine.find('h2', class_='product-name').find('a')['title']
        print(wine_name)
        price_before_comma = wine.find('span', class_='price')
        if not price_before_comma:
            pass
            # print(wine.prettify())
        # print(price_before_comma)

        # price_after_comma = wine.find('span', class_='sub-price').text
        # lidl_wines.append(LidlWine(wine_name, f'{price_before_comma},{price_after_comma}'))

    # print(lidl_wines)
    logging.info('Application End')
