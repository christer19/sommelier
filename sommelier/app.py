import logging


def run():
    # set up logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')
    logging.info('Application Start')

    # read app arguments
    print('Hello World! It is Sommelier time!')

    logging.info('Application End')
