#!/usr/bin/python
# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from KPI import KPI
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

    scheduler = BlockingScheduler()

    # 添加任务作业，本任务设置为 每10秒钟执行一次
    scheduler.add_job(Shibor().run, 'cron', hour='*', minute='*', second='*/10')
    # 添加任务作业，本任务设置为 每天12点执行一次
    scheduler.add_job(Deal().run, 'cron', hour='12', minute='0', second='0')

    scheduler.start()