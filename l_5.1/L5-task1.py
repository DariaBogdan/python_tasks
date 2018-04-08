#!/usr/bin/env python3.6
from datetime import datetime
DAYS_IN_YEAR = 365


class Wine:
    """Stores information about wine. Can calculate wine's aging.

       Attributes:
           trade_name (str): the trade name of the wine.
           brand (str): the brand produced the wine.
           country (str): the country where the wine was produced.
           date_of_bottling (datetime.datetime): the date when the wine was bottled.
           note (str): any string containing info about the wine.

        Methods:
            calc_aging: calculates approximately age of wine in years.
    """

    def __init__(self, trade_name, brand, country, date_of_bottling, note):
        self.trade_name = trade_name
        self.brand = brand
        self.country = country
        self.date_of_bottling = date_of_bottling
        self.note = note

    def calc_aging(self):
        return (datetime.now() - self.date_of_bottling).days // DAYS_IN_YEAR


if __name__ == '__main__':
    w = Wine('Red Wine', 'Krasnodarskie Vina', 'Russia', datetime(2015, 1, 1), '18+')
    print(w.trade_name)
    w.trade_name = 'Best Wine'
    print(w.trade_name)
    print(w.calc_aging())
