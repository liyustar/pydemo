# -*- coding:utf-8 -*-

import house.getdata as hgd
import re
import time

from house import mysqlutil

REVREGION = hgd.getRevRegion()
i = 0

def analyPage(path, page=1):
    filename = hgd.getFilename(path, page)
    html = hgd.getHtmlFromFile(filename)

    #items = re.findall('<a.*?target="_blank".*?data-el="ershoufang">([^<].*?)</a>.*?data-el="region">(.*?)</a>', html, re.S)
    # items = re.findall('data-el="ershoufang">([^<].*?)</a>', html, re.S)
    items = re.findall('class="title"><a href="http://sz.lianjia.com/ershoufang/(.*?)\.html".*?'
                       'data-el="ershoufang">([^<].*?)</a>.*?'
                       'data-el="region">(.*?)</a>(.*?)</div>.*?'
                       'class="positionIcon"></span>(.*?)<a.*?'
                       'class="starIcon"></span>(.*?)</div.*?'
                       'class="tag">(.*?)</div><div class="priceInfo".*?'
                       'class="totalPrice"><span>(.*?)</span.*?'
                       'data-price="(.*?)"', html, re.S)
    # global i
    # for item in items:
    #     print("[%d] %s" % (i, item))
    #     i += 1
    return items


def totalSave():
    '''存库'''
    pageMap = hgd.getAllRegionPage()

    dbutil = mysqlutil.DBUtil()

    allitems = []
    for path in pageMap:
        for pg in range(pageMap[path]):
            items = analyPage(path, pg +1)
            save_to_db(dbutil, items, path)
            # allitems.extend(items)
            pass
            # downloadPage(path, pg + 1)
    # print(allitems[:10])
    dbutil.close()

gExist = set()

def save_to_db(dbutil, items, path):
    district = REVREGION[path]
    region = path[len('/ershoufang/'):-1]

    batch_list = []
    for item in items:
        id = item[0]
        if id in gExist:
            print(id)
            continue
        else:
            gExist.add(id)

        title = item[1]
        area = item[2]
        prop1 = item[3]
        prop2 = item[4]
        prop3 = item[5]
        prop4 = item[6]
        total = item[7]
        unit = item[8]
        url = "http://sz.lianjia.com/ershoufang/%s.html" % id

        batch_list.append(mysqlutil.multipleRows([id, district, region, area, title, total, unit, url, prop1, prop2, prop3, prop4]))

    if len(batch_list) == 0:
        return

    sql = "INSERT INTO houseinfo VALUES %s" % ','.join(batch_list)
    # sql = "REPLACE houseinfo VALUES %s" % ','.join(batch_list)
    print(len(batch_list), sql)

    cur = dbutil.cursor()
    cur.execute(sql)
    dbutil.commit()

if __name__ == '__main__':
    beg = time.time()
    totalSave()
    end = time.time()
    print(end-beg)
    pass
