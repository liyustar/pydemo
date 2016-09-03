# -*- coding:utf-8 -*-

import house.getdata as hgd
import re
import time

i = 0

def analyPage(path, page=1):
    filename = hgd.getFilename(path, page)
    html = hgd.getHtmlFromFile(filename)

    #items = re.findall('<a.*?target="_blank".*?data-el="ershoufang">([^<].*?)</a>.*?data-el="region">(.*?)</a>', html, re.S)
    # items = re.findall('data-el="ershoufang">([^<].*?)</a>', html, re.S)
    items = re.findall('class="title"><a href="(.*?)".*?'
                       'data-el="ershoufang">([^<].*?)</a>.*?'
                       'data-el="region">(.*?)</a>(.*?)</div>.*?'
                       'class="positionIcon"></span>(.*?)<a.*?'
                       'class="starIcon"></span>(.*?)</div.*?'
                       'class="tag">(.*?)</div><div class="priceInfo".*?'
                       'class="totalPrice"><span>(.*?)</span.*?'
                       'data-price="(.*?)"', html, re.S)
    global i
    for item in items:
        print("[%d] %s" % (i, item))
        i += 1


def totalAnaly():
  pageMap = hgd.getAllRegionPage()
  for path in pageMap:
      for pg in range(pageMap[path]):
          analyPage(path, pg +1)
          pass
          # downloadPage(path, pg + 1)

if __name__ == '__main__':
    beg = time.time()
    totalAnaly()
    end = time.time()
    print(end-beg)
    pass
