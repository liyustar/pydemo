# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request

def getHtml(url, code='utf-8'):
    # url = 'http://news.sina.com.cn/china'
    # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    # cookie = 'lianjia_uuid=10cb6276-ca79-43f9-88d7-eafacc3147b5; select_city=440300; all-lj=75cfc00b9f12050e3970154c91c12727; sample_traffic_test=controlled_50; miyue_hide=%20index%20%20index%20%20index%20%20index%20; _gat=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _smt_uid=57c994b5.41f9c0ed; CNZZDATA1255849469=2073323734-1472823652-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893938; CNZZDATA1254525948=1201803747-1472825058-http%253A%252F%252Fwww.lianjia.com%252F%7C1472895258; CNZZDATA1255633284=65980533-1472826062-http%253A%252F%252Fwww.lianjia.com%252F%7C1472890862; CNZZDATA1255604082=1245813388-1472823441-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893641; _ga=GA1.2.1726927867.1472828598; lianjia_ssid=523070a0-a1e5-4a5c-8d47-eb0bbb2c7ead'
    # headers = {'User-Agent': user_agent, 'Cookie': cookie}

    # url += path
    # req = Request(url, headers=headers)
    req = Request(url)
    response = urlopen(req)
    html = response.read()
    # unicodePage = html.decode("cp936")
    unicodePage = html.decode(code)
    return unicodePage

def saveHtml(fileName, data):
    # save saveHtml
    file = open(fileName, 'bw')
    file.write(str.encode(data))
    file.close()

def loadHtml(fileName, code='utf-8'):
    # save saveHtml
    file = open(fileName, 'br')
    html = file.read()
    unicodePage = html.decode(code)
    return unicodePage