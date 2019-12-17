#!/usr/bin/python
# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from kpi import kpi
from moneysupply import moneysupply
from hl import hl
from shibor import shibor
from qihuo_dl import qihuo_dl
from qihuo_sh import qihuo_sh
from stock import stock
import os


if __name__ == '__main__':

    '''
    大连、郑州商品交易所：75+60+90+150=375    
    上午09:00 -- 10:15 10:30 -- 11:30
    下午 13:30 -- 15:00
    夜盘 21:00-23:30
    
    上海期货交易所：75+60+40+40+330=545分钟
    上午 09:00 -- 10:15 10:30 -- 11:30    
    下午 13:30 -- 14:10 14:20 -- 15:00
    夜盘 21:00-次日2:30
    '''
    '''
    scheduler = BlockingScheduler()

    scheduler.add_job(kpi().run, 'cron', hour='12', minute='0', second='0')
    scheduler.add_job(moneysupply().run, 'cron', hour='12', minute='0', second='0')
    scheduler.add_job(hl().run, 'cron', hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(shibor().run, 'cron', hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='9', minute='*', second='*/10')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='10', minute='0-15,30-60', second='*/10')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='11', minute='0-30', second='*/10')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='13', minute='30-60', second='*/10')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='14', minute='0-10', second='*/10')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='14', minute='20-60', second='*/10')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='21-23', minute='*', second='*/10')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='21-23', minute='*', second='*/10')

    scheduler.add_job(qihuo_sh().run, 'cron', day_of_week='mon-fri',hour='9-11,13-15', minute='*', second='*/6')
    scheduler.add_job(stock().run, 'cron', day_of_week='mon-fri',hour='9-11,13-15', minute='*', second='*/6')
    
    print('Press Ctrl+{0} to exit'.format('C' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass
    '''

    spiders = [
        kpi()
        #moneysupply()
        #hl(),
        #shibor(),
        #qihuo_sh()
        #qihuo_dl(),
        #stock()
    ]
    for spider in spiders:
        spider.__getattribute__("run")()
