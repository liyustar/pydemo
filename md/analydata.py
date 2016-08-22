# -*- coding:utf-8 -*-

from md.config.mysqlutil import DBUtil
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# url = "table.finance.yahoo.com"

if __name__ == '__main__':

    dbutil = DBUtil()

    table_name = 'stockdata_yahoo'

    symbol = '000001'
    market = 'sz'

    query = "SELECT * FROM stockdata_yahoo"
    result = dbutil.exec(query)
    dbutil.close()

    df = pd.DataFrame(list(result), columns=('symbol', 'market', 'date', 'open', 'high', 'low', 'close', 'volumn', 'adj_close'))

    # print(df)

    fig = plt.figure()


    open_fig = fig.add_axes([0.05, 0.1, 0.9, 0.8])

    # x = df['date']
    x = df.index

    open_fig.plot(x, df['open'], 'r')
    open_fig.plot(x, df['high'], 'b')
    open_fig.plot(x, df['low'], 'g')

    open_fig.set_xlabel('date')
    open_fig.set_ylabel('open')
    open_fig.set_title('open')

    plt.pause(300)



