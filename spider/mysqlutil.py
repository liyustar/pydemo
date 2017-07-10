# -*- coding:utf-8 -*-

import pymysql

db_host = '192.168.1.107'
db_user = 'root'
db_passwd = 'admin'
db_name = 'mstar'

class DBUtil:
    conn = None

    def __init__(self):
        self.conn = pymysql.connect(host=db_host,
                                    user=db_user,
                                    passwd=db_passwd,
                                    db=db_name,
                                    charset='utf8')

    def close(self):
        self.conn.commit()
        self.conn.close()


    def cursor(self):
        return self.conn.cursor()


    def commit(self):
        self.conn.commit()


    def exec(self, query, args=None):
        cur = self.conn.cursor()
        cur.execute(query, args)
        result = cur.fetchall()
        cur.close()
        return result

# 返回可用于multiple rows的sql拼装值
def multipleRows(params):
    ret = []
    # 根据不同值类型分别进行sql语法拼装
    for param in params:
        if isinstance(param, (int, float, bool)):
            ret.append(str(param))
        elif isinstance(param, (str)):
            ret.append('\'' + param + '\'')
        else:
            #print_log('unsupport value: %s ' % param)
            pass
    return '(' + ','.join(ret) + ')'

if __name__ == '__main__':

    dbutil = DBUtil()

    result = dbutil.exec("SELECT * FROM company")

    for row in result:
        print(row[0])

    dbutil.close()

