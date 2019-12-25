
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


def spider():

    kpi().run(),
    moneysupply().run(),
    hl().run(),
    shibor().run(),
    qihuo_dl().run(),
    qihuo_sh().run(),
    stock_a().run(),
    stock_hk().run()

if __name__ == '__main__':
    spider()