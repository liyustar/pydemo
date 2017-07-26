# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request

def getHtml(url, code='utf-8', headers={}):
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
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