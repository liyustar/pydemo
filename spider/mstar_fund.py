# coding: utf-8

from spider import util, mysqlutil
from bs4 import BeautifulSoup
from datetime import datetime

# 基金分类
category = [
    "stock",    # 股票型
    "sector_stock-medicine",    # 行业股票 - 医药
    "sector_stock-tech",    # 行业股票 - 科技、传媒及通讯
    "sh_hk_sz_stock",    # 沪港深股票型基金
    "mix_radical",    # 激进配置型
    "mix_flexible",    # 灵活配置型
    "mix_standard",    # 标准混合型
    "mix_keep",    # 保守混合型
    "mix_sh_hk_sz",    # 沪港深混合型基金
    "bond_convertible",    # 可转债
    "bond_radical",    # 激进债券型
    "bond_general",    # 普通债券型
    "bond_pure",    # 纯债基金
    "bond_short",    # 短债基金
    "currency",    # 货币市场基金
    "market_neutral",    # 市场中性策略
    "commodities",    # 商品
    "keep",    # 保本基金
    "other",    # 其它
]

# 请求基金信息的URL
temp_utl = 'http://morningstar.cn/handler/fundranking.ashx?' \
           'date=2017-07-14' \
           '&fund=' \
           '&category=stock' \
           '&rating=' \
           '&company=' \
           '&cust=' \
           '&sort=ReturnYTD' \
           '&direction=desc' \
           '&tabindex=0' \
           '&pageindex=1' \
           '&pagesize=10000' \
           '&randomid=0.28046837032975325'


def analyContent(content):
    soup = BeautifulSoup(content, 'html.parser')
    tr_list = soup.select('.fr_tablecontent tr')[:-1]
    for tr in tr_list:
        print(tr)
        fund_id = '?'
        fund_symbol = tr.select('td')[1].text
        fund_name = tr.select('a')[0].text
        print(fund_id, fund_symbol, fund_name)
        break


if __name__ == '__main__':
    # url = 'https://cn.morningstar.com/fundcompany/default.aspx'
    # content = util.getHtml(temp_utl)
    # util.saveHtml('mstar_fund.html', content)
    
    content = util.loadHtml('mstar_fund.html')
    
    analyContent(content)
    
