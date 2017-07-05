# -*- coding:utf-8 -*-

import os
import glob
import csv
from md.config.mysqlutil import DBUtil

# url = "table.finance.yahoo.com"


def save_to_db_old(dbutil, path, symbol, market):
    filename = path
    print("filename<%s>" % filename)

    csvReader = csv.reader(open(filename, 'r'))
    isTitle = True

    for row in csvReader:
        if isTitle:
            isTitle = False
            continue

        date = row[0]
        open_price = row[1]
        high = row[2]
        low = row[3]
        close = row[4]
        volume = row[5]
        adj_close = row[6]

        query = "INSERT INTO stockdata_yahoo VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dbutil.exec(query, (symbol, market, date, open_price, high, low, close, volume, adj_close))

    query = "UPDATE stockinfo SET is_data=%s WHERE symbol=%s and market=%s"
    dbutil.exec(query, (True, symbol, market))

sql = "INSERT INTO mtable(field1, field2, field3...) VALUES (%s, %s, %s...)"

# 返回可用于multiple rows的sql拼装值
def multipleRows(params):
    ret = []
    # 根据不同值类型分别进行sql语法拼装
    for param in params:
        if isinstance(param, (int, float, bool)):
            ret.append(str(param))
        elif isinstance(param, (str)):
            ret.append('"' + param + '"')
        else:
            #print_log('unsupport value: %s ' % param)
            pass
    return '(' + ','.join(ret) + ')'

def save_to_db(dbutil, path, symbol, market):
    filename = path
    print("filename<%s>" % filename)

    csvReader = csv.reader(open(filename, 'r'))
    isTitle = True

    batch_list = []
    for row in csvReader:
        if isTitle:
            isTitle = False
            continue

        date = row[0]
        open_price = row[1]
        high = row[2]
        low = row[3]
        close = row[4]
        volume = row[5]
        adj_close = row[6]

        batch_list.append(multipleRows([symbol, market, date, open_price, high, low, close, volume, adj_close]))

    sql = "INSERT INTO stockdata_yahoo VALUES %s" % ','.join(batch_list)
    cur = dbutil.cursor()
    cur.execute(sql)
    dbutil.commit()

    # query = "UPDATE stockinfo SET is_data=%s WHERE symbol=%s and market=%s"
    # dbutil.exec(query, (True, symbol, market))


def find_all_csv():
    path = 'data'
    return glob.glob(path + "/*.csv")


if __name__ == '__main__':
    dbutil = DBUtil()

    path_list = find_all_csv()
    # print(rst)
    symbol_market = []
    for path in path_list:
        basename = os.path.basename(path)
        fields = basename.split(".")
        symbol = fields[1]
        market = fields[2]
        if market == "ss":
            market = "sh"

        symbol_market.append([path, symbol, market])
        # market = fields[2] == "ss" ? "sh" : fields[2]
        save_to_db(dbutil, path, symbol, market)

    print(symbol_market)
    # print (basename_list)

    dbutil.close()


