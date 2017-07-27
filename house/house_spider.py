# coding: utf-8

from house import ref_info
from bs4 import BeautifulSoup

import util
import json
import time

LJ_URL = 'http://sz.lianjia.com'
LJ_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
              'Cookie': 'lianjia_uuid=10cb6276-ca79-43f9-88d7-eafacc3147b5; select_city=440300;'
                        ' all-lj=75cfc00b9f12050e3970154c91c12727; sample_traffic_test=controlled_50;'
                        ' miyue_hide=%20index%20%20index%20%20index%20%20index%20; _gat=1; _gat_global=1;'
                        ' _gat_new_global=1; _gat_dianpu_agent=1; _smt_uid=57c994b5.41f9c0ed;'
                        ' CNZZDATA1255849469=2073323734-1472823652-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893938;'
                        ' CNZZDATA1254525948=1201803747-1472825058-http%253A%252F%252Fwww.lianjia.com%252F%7C1472895258;'
                        ' CNZZDATA1255633284=65980533-1472826062-http%253A%252F%252Fwww.lianjia.com%252F%7C1472890862;'
                        ' CNZZDATA1255604082=1245813388-1472823441-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893641;'
                        ' _ga=GA1.2.1726927867.1472828598; lianjia_ssid=523070a0-a1e5-4a5c-8d47-eb0bbb2c7ead'}


def getFilename(path, page=None):
    filename = path[len('/ershoufang/'):-1]
    if page is not None:
        filename += "_%d" % page

    filename = 'data/' + filename + '.html'
    return filename


def downloadRegionPage(filename, pagePath):
    '''下载一个区域的网页'''
    url = LJ_URL + pagePath
    print("Downloading...", url)
    html = util.getHtml(url, headers=LJ_HEADERS)
    # save saveHtml
    util.saveHtml(filename, html)
    print("Download Done.", url)


def downloadAllRegions():
    '''下载所有区域网页第一页'''
    regions = ref_info.getRegions()
    for x in regions:
        for path in regions[x]:
            downloadRegionPage(getFilename(path), path)


def getRegionPageNum(regionPath):
    '''获取单个区域的所有页面URL'''
    # print(regionPath)
    filename = getFilename(regionPath)
    html = util.loadHtml(filename)

    soup = BeautifulSoup(html, 'html.parser')
    pageData = soup.select('.house-lst-page-box')[0]['page-data']
    jd = json.loads(pageData)
    return jd['totalPage']


def getPagePaths():
    '''获取所有区域页的url'''
    regions = ref_info.getRegions()
    pageNumList = [(path, getRegionPageNum(path))
               for r in regions
               for path in regions[r]]
    # print(pageNumList)
    # regionPaths, pageNums = zip(*pageNumList)
    # print(sum(pageNums))  # 路径总数

    pagePaths = [(getFilename(path, page+1), path + "pg%d" % (page + 1))
                for path,pageNum in pageNumList
                for page in range(pageNum)]
    print("pagePaths", pagePaths)

    return pagePaths


def downloadAllPage(pagePaths):
    '''下载所有二手房网页'''
    for filename,pagePath in pagePaths:
        downloadRegionPage(filename, pagePath)
        time.sleep(2)   # 要有时间间隔，不然封IP


if __name__ == '__main__':
    # downloadAllRegions()
    pagePaths = getPagePaths()
    downloadAllPage(pagePaths)
    # downloadAllPageByThread()
    pass