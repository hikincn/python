#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import demjson
import requests
from lxml import html
import random
import time
import json
from spider.dbutils import DB
from datetime import datetime

class moneysupply():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        html = html[html.index("(") + 1:]
        html = html[:html.index(")"):]
        try:
            product_dic = demjson.decode(html)
            return product_dic
        except Exception:
            return ""

    def parse(self, row):
        return row

    def insert(self, datas):

        j = len(datas)
        for i in range(0, j - 1):
            data=datas[i].split(",")

            db = DB()
            s_month=data[0][:7].replace("-","")
            sql = "select count(*) from sgba_ods_wb_kpi where kpi_month = '"+s_month+"' and kpi_code='M2'"
            db.execute(sql)
            results = db.fetchone()
            if results[0] == 0:
                kpi_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
                sql = "INSERT INTO SGBA_ODS_WB_KPI(kpi_id,KPI_MONTH,KPI_CODE,KPI_NAME,KPI_DATA,KPI_TB,KPI_HB) VALUES("+kpi_id +"," + s_month  +",'M2','货币和准货币(M2)',"+ data[1] +","+ data[2] +","+ data[3] +")"
                db.execute(sql)
                db.commit()
            else:
                db.close()
                break
            sql = "select count(*) from sgba_ods_wb_kpi where kpi_month = '"+s_month+"' and kpi_code='M1'"
            db.execute(sql)
            results = db.fetchone()
            if results[0] == 0:
                kpi_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
                sql = "INSERT INTO SGBA_ODS_WB_KPI(kpi_id,KPI_MONTH,KPI_CODE,KPI_NAME,KPI_DATA,KPI_TB,KPI_HB) VALUES("+kpi_id +"," + s_month +",'M1','货币(M1)',"+ data[4] +","+ data[5] +","+ data[6] +")"
                db.execute(sql)
                db.commit()
            sql = "select count(*) from sgba_ods_wb_kpi where kpi_month = '"+s_month+"' and kpi_code='M0'"
            db.execute(sql)
            results = db.fetchone()
            if results[0] == 0:
                kpi_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
                sql = "INSERT INTO SGBA_ODS_WB_KPI(kpi_id,KPI_MONTH,KPI_CODE,KPI_NAME,KPI_DATA,KPI_TB,KPI_HB) VALUES("+kpi_id +"," + s_month  +",'M0','流通中的现金(M0)',"+ data[7] +","+ data[8] +","+ data[9] +")"
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
        url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?cb=jQuery112306131083743285619_1612430041677&type=GJZB&sty=ZGZB&js=(%5B(x)%5D)&p=1&ps=200&mkt=11&_=1612430041678"
        data = self.get_data(url)
        self.insert(data)

