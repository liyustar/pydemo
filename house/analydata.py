# -*- coding:utf-8 -*-

from house import mysqlutil
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getDBData():
    dbutil = mysqlutil.DBUtil()
    # query = "SELECT * FROM houseinfo"
    query = "SELECT district,region,totalprice,unitprice FROM houseinfo"
    result = dbutil.exec(query)
    dbutil.close()
    return result

def analy(ret):
    columns = ['dist', 'reg', 'total', 'unit']
    df = pd.DataFrame(ret, columns=columns)
    # print(df.head())

    impute_grp = pd.pivot_table(df, values='unit', index=['dist', 'reg'], aggfunc=np.mean)
    print(impute_grp)
    print(type(impute_grp))
    mindex = impute_grp.axes[0]
    #  pd.MultiIndex.


    colorlist = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm']
    mapcol = {}

    values = []
    xidx = []
    coloridx = []
    i = 0
    for item in mindex.tolist():
        dist = item[0]
        if dist not in mapcol:
            color = colorlist[i]
            mapcol[dist] = color
            i += 1
        else:
            color = mapcol[dist]
        coloridx.append(color)

        # print(impute_grp[item[0], item[1]])
        values.append(impute_grp[item[0], item[1]])
        xidx.append("%s_%s" % (item[0], item[1]))
        # xidx.append("%s" % (item[1]))

    plt.xlabel('平均单位价格')
    plt.ylabel('位置')
    plt.ylim(-1, len(xidx))
    plt.barh(range(len(xidx)), values, color=coloridx, align='center')
    plt.yticks(range(len(xidx)), xidx)
    plt.show()


if __name__ == '__main__':
    beg = time.time()
    ret = getDBData()
    analy(list(ret))
    end = time.time()
    print(end-beg)
    pass