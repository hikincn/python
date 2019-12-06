#!/usr/bin/python
# -*- coding: UTF-8 -*-
from A01 import A01
from PMI import PMI
from PPI import PPI
from stock import Stock
from waihui import Waihui

if __name__ == '__main__':

    # a01 = A01()
    pmi = Waihui()
    spiders = [
        pmi
    ]
    for spider in spiders:
        spider.__getattribute__("run")()
