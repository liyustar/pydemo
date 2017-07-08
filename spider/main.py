# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

import pandas

import sqlite3

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

def getSinaNewsTitle(data):
    soup = BeautifulSoup(data, 'html.parser')   # html解析器
    # print(soup.text)
    news = []
    for new in soup.select('.news-item'):
        if 0 < len(new.select('h2')):
            h2 = new.select('h2')[0].text
            time = new.select('div')[1].text
            a = new.select('a')[0]['href']
            # print(time, h2, a)
            news.append((time, h2, a))

    print(len(news))
    return news


def getNewsCommentCount(url):
    m = re.search('doc-i(.+).shtml', url)
    newsid = m.group(1)

    commentURL = 'http://comment5.news.sina.com.cn/page/info?' \
                 'version=1&format=js&channel=gn&newsid=comos-{}' \
                 '&group=&compress=0&ie=utf-8&oe=utf-8' \
                 '&page=1&page_size=20'

    jsContent = getHtml(commentURL.format(newsid))
    # print(jsContent)

    jd = json.loads(jsContent.strip('var data='))
    try:
        commentCount = jd['result']['count']['total']
    except:
        commentCount = -1
    return commentCount


def getNewsDetail(url):
    result = {}
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    # result['newssource'] = soup.select('.time-source span a')[0].text
    result['newssource'] = soup.select('.time-source span')[0].text
    timesource = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource, '%Y年%m月%d日%H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
    result['comments'] = getNewsCommentCount(url)
    return result

def getNewsTitle(page, num=20):
    url = 'http://api.roll.news.sina.com.cn/zt_list' \
          '?channel=news' \
          '&cat_1=gnxw' \
          '&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj' \
          '&level==1||=2&show_ext=1&show_all=1' \
          '&show_num={}' \
          '&tag=1&format=json' \
          '&page={}' \
          '&callback=newsloadercallback&_=1499439308668'
    print(url.format(num, page))

    jsContent = getHtml(url.format(num, page))
    jd = json.loads(jsContent.lstrip('  newsloadercallback(').rstrip(');'))

    newsdetails = []
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))

    return newsdetails

def getAllTitle(pages, num=20):
    newsTotal = []
    for i in range(1, pages+1):
        newsarray = getNewsTitle(i, num)
        newsTotal.extend(newsarray)
    return newsTotal

if __name__ == '__main__':
    url = 'http://news.sina.com.cn/china'
    # html = getHtml(url)

    FILE_NAME = 'page.data'
    # 保存到文件
    # saveHtml(FILE_NAME, html)

    html = loadHtml(FILE_NAME)

    news = getSinaNewsTitle(html)

    # detail = getNewsDetail(news[0][2])
    # print(detail)

    newsTotal = getAllTitle(1)
    # print(newsTotal)

    df = pandas.DataFrame(newsTotal)
    print(df)

    df.to_excel('news.xlsx')

    with sqlite3.connect('news.sqlilte') as db:
        df.to_sql('news', con = db)



    # getNewsTitle(3, 22)

    # print(html)
    pass

