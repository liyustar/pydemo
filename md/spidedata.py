# -*- coding:utf-8 -*-

from md.config.mysqlutil import DBUtil
from urllib.request import urlopen, Request
import re

# url = "table.finance.yahoo.com"

stocklist_file = 'stocklist.html'

def download_html():
    url = 'http://quote.eastmoney.com/stocklist.html'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    headers = {'User-Agent': user_agent}
    req = Request(url, headers = headers)
    response = urlopen(url)
    html = response.read()
    # print(html)

    file = open(stocklist_file, 'bw')
    file.write(html)

def find_item():
    file = open(stocklist_file, 'br')
    html = file.read()

    unicodePage = html.decode("cp936")
    # items = re.findall('<a target="_blank" href="(http://quote\.eastmoney\.com/[a-z]{2}[0-9]{6}\.html)">(.*?)</a>', unicodePage, re.S)
    items = re.findall('<a target="_blank" href="http://quote\.eastmoney\.com/([a-z]{2})([0-9]{6})\.html">(.*?)\(.*?\)</a>', unicodePage, re.S)

    dbutil = DBUtil()
    for item in items:
        print(item)

        market = item[0]
        symbol = item[1]
        name = item[2].encode('utf-8')
        query = "INSERT INTO stockinfo VALUES(%s,%s,%s)"
        dbutil.exec(query, (symbol, market, name))

    print("len<%d>" % len(items))
    dbutil.close()




if __name__ == '__main__':
    # download_html()
    # find_item()
    pass


