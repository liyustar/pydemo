# -*- coding:utf-8 -*-

import threading
import queue
import time
from urllib.request import urlopen, Request
import re

gExitFlag = 0
gQueueLock = threading.Lock()

def getRegion():
    '''获取所有区域名字'''

    luohu = ["/ershoufang/buxin/", # 布心
             "/ershoufang/baishida/", # 百仕达
             "/ershoufang/cuizhu/", # 翠竹
             "/ershoufang/chunfenglu/", # 春风路
             "/ershoufang/dongmen/", # 东门
             "/ershoufang/diwang/", # 地王
             "/ershoufang/honghu/", # 洪湖
             "/ershoufang/huangbeiling/", # 黄贝岭
             "/ershoufang/luohukouan/", # 罗湖口岸
             "/ershoufang/liantang/", # 莲塘
             "/ershoufang/qingshuihe/", # 清水河
             "/ershoufang/sungang/", # 笋岗
             "/ershoufang/wanxiangcheng/", # 万象城
             "/ershoufang/xinxiu/", # 新秀
             "/ershoufang/yinhu/"] # 银湖

    futian = ["/ershoufang/baihua/", # 百花
              "/ershoufang/bijiashan/", # 笔架山
              "/ershoufang/bagualing/", # 八卦岭
              "/ershoufang/chegongmiao/", # 车公庙
              "/ershoufang/futianzhongxin/", # 福田中心
              "/ershoufang/futianbaoshuiqu/", # 福田保税区
              "/ershoufang/huaqiangnan/", # 华强南
              "/ershoufang/huaqiangbei/", # 华强北
              "/ershoufang/huanggang/", # 皇岗
              "/ershoufang/huaqiaocheng1/", # 华侨城
              "/ershoufang/jingtian/", # 景田
              "/ershoufang/lianhua/", # 莲花
              "/ershoufang/meilin/", # 梅林
              "/ershoufang/shangxiasha/", # 上下沙
              # "/ershoufang/shangbu/", # 上步  无房源
              "/ershoufang/shixia/", # 石厦
              "/ershoufang/xiangmihu/", # 香蜜湖
              "/ershoufang/xinzhou1/", # 新洲
              "/ershoufang/yuanling/", # 园岭
              "/ershoufang/zhuzilin/"] # 竹子林

    nanshan = ["/ershoufang/baishizhou/", # 白石洲
               "/ershoufang/daxuecheng3/", # 大学城
               "/ershoufang/houhai/", # 后海
               "/ershoufang/hongshuwan/", # 红树湾
               # "/ershoufang/huaqiaocheng1/", # 华侨城
               "/ershoufang/kejiyuan/", # 科技园
               "/ershoufang/nantou/", # 南头
               "/ershoufang/nanshanzhongxin/", # 南山中心
               "/ershoufang/qianhai/", # 前海
               "/ershoufang/shekou/", # 蛇口
               # "/ershoufang/shenzhenbeizhan/", # 深圳北站
               "/ershoufang/shenzhenwan/", # 深圳湾
               "/ershoufang/xili1/"] # 西丽

    yantian = ["/ershoufang/meisha/", # 梅沙
               "/ershoufang/shatoujiao/", # 沙头角
               "/ershoufang/yantiangang/"] # 盐田港

    baoan = ["/ershoufang/baoanzhongxin/", # 宝安中心
             "/ershoufang/fuyong/", # 福永
             "/ershoufang/gongming/", # 公明
             "/ershoufang/shajing/", # 沙井
             "/ershoufang/songgang/", # 松岗
             "/ershoufang/shiyan/", # 石岩
             "/ershoufang/taoyuanju/", # 桃源居
             "/ershoufang/xixiang/", # 西乡
             "/ershoufang/xicheng1/", # 曦城
             "/ershoufang/xinan/"] # 新安

    longgang = [# "/ershoufang/bantian/", # 坂田
                "/ershoufang/buji/", # 布吉
                "/ershoufang/henggang/", # 横岗
                "/ershoufang/longgangzhongxin/", # 龙岗中心
                "/ershoufang/nanlian/", # 南联
                "/ershoufang/pingdi/", # 坪地
                "/ershoufang/pingshan/", # 坪山
                "/ershoufang/pinghu/"] # 平湖

    longhua = ["/ershoufang/bantian/", # 坂田
               "/ershoufang/dalang/", # 大浪
               "/ershoufang/guanlan/", # 观澜
               "/ershoufang/longhuazhongxin/", # 龙华中心
               "/ershoufang/minzhi/", # 民治
               "/ershoufang/qinghu/", # 清湖
               "/ershoufang/shenzhenbeizhan/"] # 深圳北站


    region = {}
    region['luohu'] = luohu
    region['futian'] = futian
    region['nanshan'] = nanshan
    region['yantian'] = yantian
    region['baoan'] = baoan
    region['longgang'] = longgang
    region['longhua'] = longhua

    return region


def getHtml(path, code='utf-8'):
    '''通过区域名请求网页'''
    url = 'http://sz.lianjia.com'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    cookie = 'lianjia_uuid=10cb6276-ca79-43f9-88d7-eafacc3147b5; select_city=440300; all-lj=75cfc00b9f12050e3970154c91c12727; sample_traffic_test=controlled_50; miyue_hide=%20index%20%20index%20%20index%20%20index%20; _gat=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _smt_uid=57c994b5.41f9c0ed; CNZZDATA1255849469=2073323734-1472823652-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893938; CNZZDATA1254525948=1201803747-1472825058-http%253A%252F%252Fwww.lianjia.com%252F%7C1472895258; CNZZDATA1255633284=65980533-1472826062-http%253A%252F%252Fwww.lianjia.com%252F%7C1472890862; CNZZDATA1255604082=1245813388-1472823441-http%253A%252F%252Fwww.lianjia.com%252F%7C1472893641; _ga=GA1.2.1726927867.1472828598; lianjia_ssid=523070a0-a1e5-4a5c-8d47-eb0bbb2c7ead'
    headers = {'User-Agent': user_agent, 'Cookie': cookie}

    url += path
    req = Request(url, headers = headers)
    response = urlopen(req)
    html = response.read()
    # unicodePage = html.decode("cp936")
    unicodePage = html.decode(code)

    return unicodePage

def getHtmlFromFile(path, code='utf-8'):
    '''通过区域名字获取网页文件'''
    file = open(path, 'br')
    html = file.read()
    unicodePage = html.decode(code)
    return unicodePage


def getFilename(path, page=None):
    filename = path[len('/ershoufang/'):-1]
    if page is not None:
        filename += "_%d" % page

    filename = 'data/' + filename + '.html'
    return filename

def downloadAllRegion():
    '''下载所有区域网页第一页'''
    regions = getRegion()
    for x in regions:
        for path in regions[x]:
            filename = getFilename(path)

            html = getHtml(path)

            # save saveHtml
            file = open(filename, 'bw')
            file.write(str.encode(html))
            file.close()


def downloadPage(path, page=None):
    '''下载指定页数的页面'''
    print(path, page)
    filename = getFilename(path, page)

    if page is not None:
        path += "pg%d" % page

    html = getHtml(path)

    # save saveHtml
    file = open(filename, 'bw')
    file.write(str.encode(html))
    file.close()


def downloadAllPage():
    '''下载所有二手房网页'''
    pageMap = getAllRegionPage()
    for path in pageMap:
        for pg in range(pageMap[path]):
            downloadPage(path, pg + 1)


def downloadAllPageByThread():
    '''下载所有二手房网页'''
    # pageMap = getAllRegionPage()

    # 入队
    pageQueue = queue.Queue(3000)

    # 通过总页数来下载
    # for path in pageMap:
    #     for pg in range(pageMap[path]):
    #         # downloadPage(path, pg + 1)
    #         pageQueue.put([path, pg+1])

    # 下载失败后,补全
    for line in open('data/errdata.dat', 'r'):
        line = line[:-1]
        # print(line)
        fields = line.split('_')
        pageQueue.put(["/ershoufang/%s/"%fields[0], int(fields[1])])

    print(pageQueue.qsize())

    # 启动线程
    threads = []
    threadNum = 1
    for i in range(threadNum):
        thread = MyThread(i, "T%d" % i, pageQueue)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def test1(path):
    '''测试获取item'''
    html = getHtml(path)

    # < a
    # href = "http://sz.lianjia.com/ershoufang/105100384171.html"
    # target = "_blank"
    # data - bl = "list"
    # data - log_index = "1"
    # data - el = "ershoufang" > 雍翠华府高层观山看景俯瞰泳池厅出阳台 < / a >

    items = re.findall('<a.*?target="_blank".*?data-el="ershoufang">([^<].*?)</a>', html, re.S)
    i = 0
    for item in items:
        print("%s" % (item))
        i += 1


def getTotalPage(path=''):
    '''测试获取page'''
    filename = getFilename(path)
    print(filename)

    # html = getHtml(path)
    html = getHtmlFromFile(filename)

    # file = open(filename, 'bw')
    # file.write(str.encode(html))

    # print(html)

    # /html/body/div[4]/div[1]/div[5]/div[2]/div
    items = re.findall('page-data=\'{"totalPage":([0-9]*?),', html, re.S)
    return int(items[0])

def getAllRegionPage():
    '''获取区域页码数'''
    region = getRegion()
    totalPage = 0
    pagemap = {}
    for x in region:
        for y in region[x]:
            # print(y)
            page = getTotalPage(y)
            # print(page)
            pagemap[y] = page
            totalPage += page
            # test1('/ershoufang/yinhu/')
    print(totalPage)
    return pagemap

class MyThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("start:", self.name)
        process_data(self.name, self.q)
        print("end:", self.name)

def process_data(threadName, q):
    while not gExitFlag:
        gQueueLock.acquire()
        data = None
        if not q.empty():
            data = q.get()
        gQueueLock.release()

        if data is not None:
            path = data[0]
            page = data[1]
            print(threadName, page, path)
            downloadPage(path, page)
            time.sleep(2)
            pass
        else:
            break

if __name__ == '__main__':
    # downloadAllRegion()
    # downloadAllPage()
    # downloadAllPageByThread()
    pass
