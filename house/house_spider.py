# coding: utf-8

from house import ref_info
from bs4 import BeautifulSoup

import util
import json
import time
import os

LJ_URL = 'http://sz.lianjia.com'
LJ_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
              'Cookie': 'lianjia_uuid=10cb6276-ca79-43f9-88d7-eafacc3147b5; miyue_hide=%20index%20%20index%20%20index%20%20index%20; _jzqa=1.3615183155870864400.1472963387.1472963387.1472963387.1; _qzja=1.2083497657.1472963386956.1472963386956.1472963386956.1472963386956.1472963386956.0.0.0.1.1; lianjia_token=2.00038ff4927a9338921222dda3221234a2; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1477231980; select_city=440300; all-lj=c28812af28ef34a41ba2474a2b5c52c2; UM_distinctid=15d84c8e48c649-0fe2adb9ef30fd-1a346d54-384000-15d84c8e48dd33; CNZZDATA1255849469=1623673338-1501169462-null%7C1501169462; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1501171345; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1501171345; CNZZDATA1254525948=1923215834-1501169589-null%7C1501169589; CNZZDATA1255633284=556794542-1501169455-null%7C1501169455; CNZZDATA1255604082=638382520-1501170803-null%7C1501170803; _smt_uid=57c994b5.41f9c0ed; _gat=1; _gat_global=1; _gat_new_global=1; _ga=GA1.2.1726927867.1472828598; _gid=GA1.2.712566502.1501171346; _gat_dianpu_agent=1; lianjia_ssid=8a355d57-7162-4fa1-b2a3-b4f06493506d',
              }


def getFilename(path, page=None):
    filename = path[len('/ershoufang/'):-1]
    if page is not None:
        filename += "_%d" % page

    filename = 'data/' + filename + '.html'
    return filename


def downloadRegionPage(filename, pagePath):
    '''下载一个区域的网页'''
    url = LJ_URL + pagePath
    if os.path.exists(filename):
        print("Have Downloaded.", url)
        return 1

    print("Downloading...", url)
    html = util.getHtml(url, headers=LJ_HEADERS)
    # save saveHtml
    util.saveHtml(filename, html)
    print("Download Done.", url)
    return 0


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
        if 1 == downloadRegionPage(filename, pagePath):
            continue
        time.sleep(3)   # 要有时间间隔，不然封IP


if __name__ == '__main__':
    # downloadAllRegions()
    pagePaths = getPagePaths()
    downloadAllPage(pagePaths)
    # downloadAllPageByThread()
    pass