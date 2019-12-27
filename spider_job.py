
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from spider.kpi import kpi
from spider.moneysupply import moneysupply
from spider.hl import hl
from spider.shibor import shibor
from spider.qihuo_dl import qihuo_dl
from spider.qihuo_sh import qihuo_sh
from spider.stock_a import stock_a
from spider.stock_hk import stock_hk
import os

"""
    大连、郑州商品交易所：  
    上午09:00 -- 10:15 10:30 -- 11:30
    下午 13:30 -- 15:00

    上海期货交易所：
    上午 09:00 -- 10:15 10:30 -- 11:30
    下午 13:30 -- 14:10 14:20 -- 15:00

    A股：9:30 — 11:30；13:00 — 15:00
    H股：10:00 — 12:30；14:30 — 16:00
"""

def spider():

    scheduler = BlockingScheduler()

    trigger = CronTrigger(hour='12', minute="0", second="0")
    scheduler.add_job(kpi().run, trigger)

    trigger = CronTrigger(hour='12', minute="0", second="0")
    scheduler.add_job(moneysupply().run, trigger)

    trigger = CronTrigger(hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(hl().run, trigger)

    trigger = CronTrigger(hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(shibor().run, trigger)

    trigger = CronTrigger(day_of_week='mon-fri', hour='9-11', minute='*', second='0')
    scheduler.add_job(qihuo_dl().run,trigger)

    trigger = CronTrigger(day_of_week='mon-fri', hour='11', minute='0-30', second='0')
    scheduler.add_job(qihuo_dl().run,trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='13', minute='30-59', second='0')
    scheduler.add_job(qihuo_dl().run,trigger)

    trigger = CronTrigger(day_of_week='mon-fri', hour='14', minute='*', second='0')
    scheduler.add_job(qihuo_dl().run,trigger)

    trigger = CronTrigger( day_of_week='mon-fri', hour='9-11', minute='*', second='0')
    scheduler.add_job(qihuo_sh().run, trigger)

    trigger = CronTrigger(day_of_week='mon-fri', hour='11', minute='0-30', second='0')
    scheduler.add_job(qihuo_sh().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='13', minute='30-59', second='0')
    scheduler.add_job(qihuo_sh().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='14', minute='*', second='0')
    scheduler.add_job(qihuo_sh().run,trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='10-11', minute='*', second='0')
    scheduler.add_job(stock_hk().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='12', minute='0-30', second='0')
    scheduler.add_job(stock_hk().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='14', minute='30-59', second='0')
    scheduler.add_job(stock_hk().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='15', minute='*', second='0')
    scheduler.add_job(stock_hk().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='10-12', minute='*', second='0')
    scheduler.add_job(stock_a().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='13-14', minute='*', second='0')
    scheduler.add_job(stock_a().run, trigger )

    trigger = CronTrigger(day_of_week='mon-fri', hour='15', minute='0-30', second='0')
    scheduler.add_job(stock_a().run, trigger )

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass



if __name__ == '__main__':
    spider()