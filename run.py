#!/usr/bin/python
# -*- coding: UTF-8 -*-
from deal import Deal
from GDZCTZ import GDZCTZ
from MoneySupply import MoneySupply
from PMI import PMI
from PPI import PPI
from delaymarket import Delaymarket
from shibor import Shibor
from stock import Stock
from waihui import Waihui

if __name__ == '__main__':

    spiders = [
        Shibor()
    ]
    for spider in spiders:
        spider.__getattribute__("run")()
