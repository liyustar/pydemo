# -*- coding:utf-8 -*-

import pymysql

db_host = '192.168.1.109'
db_user = 'root'
db_passwd = 'root'
db_name = 'marketdata'

class DBUtil:
    conn = None

    def __init__(self):
        self.conn = pymysql.connect(host=db_host,
                               user=db_user,
                               passwd=db_passwd,
                               db=db_name)

    def close(self):
        self.conn.commit()
        self.conn.close()

    def exec(self, query, args=None):
        cur = self.conn.cursor()
        cur.execute(query, args)
        result = cur.fetchall()
        cur.close()
        return result


if __name__ == '__main__':

    dbutil = DBUtil()

    result = dbutil.exec("SELECT * FROM stockdata_yahoo")

    for row in result:
        print(row[0])

    dbutil.close()

