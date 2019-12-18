#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
from lxml import html
from spider.dbutils import DB
from datetime import datetime

from spider.Spider import Spider


class moneysupply(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }

    def get_url(self, page=None):
        url = "http://data.eastmoney.com/cjsj/hbgyl.html"
        return url

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'gb2312'
        data = req.text
        return data

    def parse(self, row):
        return row

    def insert(self, data):

        db = DB()
        sql = "select count(*) from sgba_ods_wb_kpi where kpi_month = '"+data[0].replace("年","").replace("月份","")+"' and kpi_code='M2'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            sql = "INSERT INTO SGBA_ODS_WB_KPI(KPI_MONTH,KPI_CODE,KPI_NAME,KPI_DATA,KPI_TB,KPI_HB) VALUES(" + data[0].replace("年","").replace("月份","")  +",'M2','货币和准货币(M2)',"+ data[1] +","+ data[2].replace("%","") +","+ data[3].replace("%","") +")"
            db.execute(sql)
            db.commit()
        sql = "select count(*) from sgba_ods_wb_kpi where kpi_month = '"+data[0].replace("年","").replace("月份","")+"' and kpi_code='M1'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            sql = "INSERT INTO SGBA_ODS_WB_KPI(KPI_MONTH,KPI_CODE,KPI_NAME,KPI_DATA,KPI_TB,KPI_HB) VALUES(" + data[0].replace("年","").replace("月份","")  +",'M1','货币(M1)',"+ data[4] +","+ data[5].replace("%","") +","+ data[6].replace("%","") +")"
            db.execute(sql)
            db.commit()
        sql = "select count(*) from sgba_ods_wb_kpi where kpi_month = '"+data[0].replace("年","").replace("月份","")+"' and kpi_code='M0'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            sql = "INSERT INTO SGBA_ODS_WB_KPI(KPI_MONTH,KPI_CODE,KPI_NAME,KPI_DATA,KPI_TB,KPI_HB) VALUES(" + data[0].replace("年","").replace("月份","")  +",'M0','流通中的现金(M0)',"+ data[7] +","+ data[8].replace("%","") +","+ data[9].replace("%","") +")"
            db.execute(sql)
            db.commit()
        db.close()

    def get_value(self, item):
        if isinstance(item, list):
            for str in item:
                if self.trim(str) != "":
                    return self.trim(str)
        return self.trim(item)

    def trim(self, value):
        return str.strip(value).replace("\r\n", "").replace(" ", "")

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        url = self.get_url()
        data = self.get_data(url)
        tree = html.fromstring(data)
        items = tree.xpath('//*[@id="tb"]/tr[3]/td//text()')
        j = -1
        list_data = list(range(10))
        for item in items:
            value= self.get_value(item)
            if value != "":
                j = j+1
                list_data[j] = value
        self.insert(list_data)

