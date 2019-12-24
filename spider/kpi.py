#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import http
import json
import os
import pickle
import urllib

import requests

from spider.dbutils import DB
from datetime import datetime

class kpi():
    data = {"id": "zb", "dbcode": "hgyd", "wdcode": "zb", "m": "getTree"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    code = ''
    tree = {}

    def get_tree(self, parent=None):
        url = 'http://data.stats.gov.cn/easyquery.htm'
        if parent is not None:
            self.data["id"] = parent['id']
        req = requests.post(url=url, data=self.data, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        product_dic = json.loads(html)
        if len(product_dic) > 0:
            if product_dic[0]["isParent"]:
                for product in product_dic:
                    self.get_tree(product)
            else:
                for product in product_dic:
                    url2 = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"' + product[
                        "id"] + '"}]&k1=1575347790952&h=1'
                    self.tree[product['name']] = url2

    def get_url(self, param=None):
        if os.path.exists("dict.file"):
            with open("dict.file", "rb") as f:
                self.tree = pickle.load(f)
        else:
            self.get_tree()
            self.dump()
        return self.tree[param]

    def get_data(self, url):
        cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        request = urllib.request.Request(url)
        reponse = opener.open(request)
        html = reponse.read().decode('utf8')
        try:
            product_dic = json.loads(html)
            return product_dic
        except Exception:
            return ""

    def parse(self, rows, param):
        nodes = rows['returndata']['wdnodes'][0]['nodes']
        for node in nodes:
            if param in node['cname']:
                self.code = node['code']
                break

        code = 'zb.' + self.code + '_sj'
        for item in rows['returndata']['datanodes']:
            if code in item['code'] and item['data']['hasdata']:
                date = item['code'][len(item['code']) - 6:]
                return {"strdata": item['data']['strdata'], "date": date}
                break

    def insert(self, code,name,data):
        db = DB()
        sql = "select count(*)  as cnt from sgba_ods_wb_kpi where kpi_month = '"+data['date']+"' and kpi_code='"+code+"'"
        db.execute(sql)
        results = db.fetchone()
        if results[0]==0:
            sql = "INSERT INTO SGBA_ODS_WB_KPI(KPI_MONTH,KPI_CODE,KPI_NAME,KPI_DATA) VALUES(" +data['date']+",'"+ code+ "','"+name+"',"+data['strdata']+")"
            db.execute(sql)
            db.commit()
        db.close()

    def dump(self):
        with open("dict.file", "wb") as f:
            pickle.dump(self.tree, f)

    def get_data_by_item(self, menu, key):
        url = self.get_url(menu)
        rows = self.get_data(url)
        return self.parse(rows, key)

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        value = self.get_data_by_item('制造业采购经理指数', '制造业采购经理指数')
        self.insert('pmi','制造业采购经理指数',value)

        value = self.get_data_by_item('工业生产者出厂价格指数(上年同月=100)', '工业生产者出厂价格指数(上年同月=100)')
        self.insert('ppi_snty','工业生产者出厂价格指数(上年同月=100)',value)
        value = self.get_data_by_item('工业生产者出厂价格指数(上年同期=100)', '工业生产者出厂价格指数(上年同期=100)')
        self.insert('ppi_sntq','工业生产者出厂价格指数(上年同期=100)',value)
        value = self.get_data_by_item('工业生产者出厂价格指数(上月=100)', '工业生产者出厂价格指数(上月=100)')
        self.insert('ppi_sy','工业生产者出厂价格指数(上月=100)',value)

        value = self.get_data_by_item('全国居民消费价格分类指数(上年同月=100)(2016-)', '居民消费价格指数(上年同月=100)')
        self.insert('cpi_snty','居民消费价格指数(上年同月=100)',value)
        value = self.get_data_by_item('全国居民消费价格分类指数(上年同期=100)(2016-)', '居民消费价格指数(上年同期=100)')
        self.insert('cpi_sntq','居民消费价格指数(上年同期=100)',value)
        value = self.get_data_by_item('全国居民消费价格分类指数(上月=100)(2016-)', '居民消费价格指数(上月=100)')
        self.insert('cpi_sy','居民消费价格指数(上年同月=100)',value)

        value = self.get_data_by_item('按行业分固定资产投资增速（2018-）', '采矿业固定资产投资额_累计增长')
        self.insert('cky','采矿业固定资产投资额_累计增长(%)',value)
        value = self.get_data_by_item('按行业分固定资产投资增速（2018-）', '黑色金属矿采选业固定资产投资额')
        self.insert('hsjs','黑色金属矿采选业固定资产投资额_累计增长(%)',value)
        value = self.get_data_by_item('按行业分固定资产投资增速（2018-）', '汽车制造业固定资产投资额')
        self.insert('qczz','汽车制造业固定资产投资额_累计增长(%)',value)
        value = self.get_data_by_item('按行业分固定资产投资增速（2018-）', '房地产业固定资产投资额')
        self.insert('fdc','房地产业固定资产投资额_累计增长(%)',value)
        value = self.get_data_by_item('按行业分固定资产投资增速（2018-）', '制造业固定资产投资额')
        self.insert('zzy','制造业固定资产投资额_累计增长(%)',value)
