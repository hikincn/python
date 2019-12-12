#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from lxml import html

from Spider import Spider


class MoneySupply(Spider):
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
        print(data)

    def get_value(self, item):
        if isinstance(item, list):
            for str in item:
                if self.trim(str) != "":
                    return self.trim(str)
        return self.trim(item)

    def trim(self, value):
        return str.strip(value).replace("\r\n", "").replace(" ", "")

    def run(self):
        url = self.get_url()
        data = self.get_data(url)
        tree = html.fromstring(data)
        item = tree.xpath('//*[@id="tb"]/tr[3]/td[1]//text()')
        print(self.get_value(item))
        item = tree.xpath('//*[@id="tb"]/tr[3]/td[2]//text()')
        print(self.get_value(item))
        print("================")
        item = tree.xpath('//*[@id="tb"]/tr[4]/td[1]//text()')
        print(self.get_value(item))
        item = tree.xpath('//*[@id="tb"]/tr[4]/td[2]//text()')
        print(self.get_value(item))
        item = tree.xpath('//*[@id="tb"]/tr[4]/td[3]//text()')
        print(self.get_value(item))
        item = tree.xpath('//*[@id="tb"]/tr[4]/td[4]//text()')
        print(self.get_value(item))
        print("=====================================================")
        items = tree.xpath('//*[@id="tb"]/tr[3]/td//text()')
        for item in items:
            value = self.get_value(item)
            if value != "":
                print(value)


if __name__ == '__main__':
    MoneySupply().run()
