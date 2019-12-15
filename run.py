#!/usr/bin/python
# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from KPI import KPI
from MoneySupply import MoneySupply
from Hl import HL
from shibor import Shibor
from qihuo_dl import qihuo_dl
from qihuo_sh import qihuo_sh
from stock import Stock
from datetime import datetime
import os
'''
def tick():
    print('*********** The time is: %s' % datetime.now())
def pick():
    print('^^^^^^^^^^^ The time is: %s' % datetime.now())
    '''
if __name__ == '__main__':
    '''
    scheduler = BlockingScheduler()

    # 添加任务作业，本任务设置为 每10秒钟执行一次
    #scheduler.add_job(tick, 'cron', hour='*', minute='*', second='*/5')
    #scheduler.add_job(tick, 'cron', hour='*', minute='*', second='*/10')
    #scheduler.add_job(tick, 'cron', hour='6', minute='*', second='1,10,20,30,40,50')
    #scheduler.add_job(pick, 'cron', hour='6', minute='*', second='1,20,40')
    #scheduler.add_job(Shibor().run, 'cron', hour='*', minute='*', second='*/10')
    # 添加任务作业，本任务设置为 每天12点执行一次
    
    scheduler.add_job(KPI().run, 'cron', hour='12', minute='0', second='0')
    scheduler.add_job(MoneySupply().run, 'cron', hour='12', minute='0', second='0')
    scheduler.add_job(HL().run, 'cron', hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(Shibor().run, 'cron', hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(qihuo_sh().run, 'cron', day_of_week='mon-fri',hour='9-11,13-15', minute='1,11,21,31,41,51', second='0')
    scheduler.add_job(qihuo_sh().run, 'cron', day_of_week='mon-fri',hour='9-11,13-15', minute='1,11,21,31,41,51', second='0')
    scheduler.add_job(Stock().run, 'cron', day_of_week='mon-fri',hour='9-11,13-15', minute='1,11,21,31,41,51', second='0')
    
    print('Press Ctrl+{0} to exit'.format('K' if os.name == 'nt' else 'L'))
    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass
    '''

    spiders = [
        #KPI()
        MoneySupply(),
        HL(),
        Shibor(),
        qihuo_dl(),
        qihuo_sh(),
        Stock()
    ]
    for spider in spiders:
        spider.__getattribute__("run")()
