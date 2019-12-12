#!/usr/bin/python
# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from KPI import KPI
from qihuo_dl import qihuo_dl
from MoneySupply import MoneySupply
from qihuo_sh import qihuo_sh
from shibor import Shibor
from stock import Stock
from hl import Hl


if __name__ == '__main__':

    #scheduler = BlockingScheduler()

    # 添加任务作业，本任务设置为 每10秒钟执行一次
    #scheduler.add_job(Shibor().run, 'cron', hour='*', minute='*', second='*/10')
    # 添加任务作业，本任务设置为 每天12点执行一次
    #scheduler.add_job(Deal().run, 'cron', hour='12', minute='0', second='0')

    #scheduler.start()

    spiders = [
        Shibor()
    ]
    for spider in spiders:
        spider.__getattribute__("run")()
