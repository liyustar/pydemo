# coding: utf-8

from house import ref_info

import util


def getFilename(path, page=None):
    filename = path[len('/ershoufang/'):-1]
    if page is not None:
        filename += "_%d" % page

    filename = 'data/' + filename + '.html'
    return filename

def downloadRegion(regionPath):
    filename = getFilename(regionPath)

    url = 'http://sz.lianjia.com'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    cookie = 'lianjia_uuid=10cb6276-ca79-43f9-88d7-eafacc3147b5; select_city=440300; all-lj=75cfc00b9f12050e3970154c91c12727; sample_traffic_test=controlled_50; miyue_hide=%20index%20%20index%20%20index%20%20index%20; _gat=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _smt_uid=57c994b5.41f9c0ed; CNZZDATA1255849469=2073323734-1472823652-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893938; CNZZDATA1254525948=1201803747-1472825058-http%253A%252F%252Fwww.lianjia.com%252F%7C1472895258; CNZZDATA1255633284=65980533-1472826062-http%253A%252F%252Fwww.lianjia.com%252F%7C1472890862; CNZZDATA1255604082=1245813388-1472823441-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893641; _ga=GA1.2.1726927867.1472828598; lianjia_ssid=523070a0-a1e5-4a5c-8d47-eb0bbb2c7ead'
    headers = {'User-Agent': user_agent, 'Cookie': cookie}
    print(url + regionPath)
    html = util.getHtml(url + regionPath, headers=headers)
    # save saveHtml
    util.saveHtml(filename, html)

def downloadAllRegions():
    '''下载所有区域网页第一页'''
    regions = ref_info.getRegions()
    for x in regions:
        for path in regions[x]:
            downloadRegion(path)

if __name__ == '__main__':
    downloadAllRegions()
    # downloadAllPage()
    # downloadAllPageByThread()
    pass