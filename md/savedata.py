# -*- coding:utf-8 -*-

import csv
from md.config.mysqlutil import DBUtil

# url = "table.finance.yahoo.com"

if __name__ == '__main__':

    dbutil = DBUtil()

    table_name = 'stockdata_yahoo'

    symbol = '000001'
    market = 'sz'
    filename = "st.%s.%s.csv" % (symbol, market)
    print("filename<%s>", filename)

    csvReader = csv.reader(open(filename, 'r'))
    isTitle = True

    for row in csvReader:
        if isTitle:
            isTitle = False
            continue

        date = row[0]
        open = row[1]
        high = row[2]
        low = row[3]
        close = row[4]
        volume = row[5]
        adj_close = row[6]

        query = "INSERT INTO stockdata_yahoo VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dbutil.exec(query, (symbol, market, date, open, high, low, close, volume, adj_close))

    dbutil.close()


