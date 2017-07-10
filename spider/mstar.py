# -*- coding: utf-8 -*-

from spider import util
from bs4 import BeautifulSoup


def getFundCompanys(content):
    soup = BeautifulSoup(content, 'html.parser')

    list = soup.select('.msDataText')
    for x in list:
        print(x)

if __name__ == '__main__':
    # url = 'https://cn.morningstar.com/fundcompany/default.aspx'
    # content = util.getHtml(url)
    # util.saveHtml('mstar_fundcompany.html', content)

    content = util.loadHtml('mstar_fundcompany.html')
    result = getFundCompanys(content)

    for item in result:
        print(item)


