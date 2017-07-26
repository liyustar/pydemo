# -*- coding: utf-8 -*-

import json
import re
import sqlite3
from datetime import datetime

import pandas
from bs4 import BeautifulSoup

import util


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

    jsContent = util.getHtml(commentURL.format(newsid))
    # print(jsContent)

    jd = json.loads(jsContent.strip('var data='))
    try:
        commentCount = jd['result']['count']['total']
    except:
        commentCount = -1
    return commentCount


def getNewsDetail(url):
    result = {}
    html = util.getHtml(url)
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

    jsContent = util.getHtml(url.format(num, page))
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

    html = util.loadHtml(FILE_NAME)

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

