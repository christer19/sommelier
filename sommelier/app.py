import logging

from sommelier.lidl_api import get_lidl_wines
from sommelier.vivino_api import get_vivino_rating


class Wine:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def __str__(self):
        return f'Wino:{self.name}, cena: {self.price} zł, rating: {self.rating}'

    def __repr__(self):
        return self.__str__()


def run():
    # set up logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')
    logging.info('Sommelier Start')

    lidl_wines = get_lidl_wines()
    wines = enrich_lidl_wines_with_rating(lidl_wines)
    print(wines)

    logging.info('Sommelier End')


def enrich_lidl_wines_with_rating(lidl_wines):
    wines = []
    for lidl_wine in lidl_wines:
        if lidl_wine:
            wine_rating = get_vivino_rating(lidl_wine.name)
            if wine_rating:
                wines.append(Wine(lidl_wine.name, lidl_wine.price, wine_rating))
    return wines
