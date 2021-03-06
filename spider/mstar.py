# -*- coding: utf-8 -*-

from datetime import datetime

from bs4 import BeautifulSoup

import util
from spider import mysqlutil


def getFundCompanys(content):
    soup = BeautifulSoup(content, 'html.parser')

    allFund = soup.select('#ctl00_cphMain_gridResult tr')[1:]

    result = []
    for fund in allFund:
        fundInfo = {}
        contents = fund.contents
        # print(contents)
        # fundInfo['id'] = contents[1].text
        fundInfo['id'] = contents[2].contents[0]['href'].lstrip('/quickrank/default.aspx?company=')
        fundInfo['name'] = contents[2].text
        fundInfo['city'] = contents[3].text
        fundInfo['setup_time'] = datetime.strptime(contents[4].text, '%Y-%m-%d')
        fundInfo['scale'] = contents[5].text
        fundInfo['fund_num'] = contents[6].text
        fundInfo['pm_num'] = contents[7].text
        fundInfo['best_fund'] = contents[9].text
        # fundInfo['bestFundId'] = contents[9].contents[0]['href'].lstrip('/quicktake/')
        result.append(fundInfo)

    return result

if __name__ == '__main__':
    # url = 'https://cn.morningstar.com/fundcompany/default.aspx'
    # content = util.getHtml(url)
    # util.saveHtml('mstar_fundcompany.html', content)

    content = util.loadHtml('mstar_fundcompany.html')
    result = getFundCompanys(content)

    dbutil = mysqlutil.DBUtil()

    for item in result:
        dbutil.exec('insert into company(id, name, city, setup_time, scale, fund_num, pm_num, best_fund) values(%s, %s, %s, %s, %s, %s, %s, %s)',
            (item['id'], item['name'], item['city'], item['setup_time'], item['scale'], item['fund_num'], item['pm_num'], item['best_fund']))

    dbutil.close()
