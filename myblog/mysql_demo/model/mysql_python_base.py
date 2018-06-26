#-*-coding:utf-8-*-

import MySQLdb as mdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class DBCont(object):

    def __init__(self):
        self.getCon()

    #获取连接
    def getCon(self):
        try:
            self.conn = mdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='root',
                port=3306,
                db='test',
                charset='utf8'
            )
            print('数据库已经连接')
        except mdb.Error as e:
            print('Error is %s,数据库连接出错啦！！！'%e)

    #关闭连接
    def closeCon(self):
        if self.conn:
            self.conn.close()
            print('数据库已关闭')

    #取出单个值
    def findOne(self):
        sql = "select * from user02 Limit 1"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        print (rest)
        cursor.close()
        self.closeCon()

    # 取出多个值
    def findMore(self):
        sql = "select * from user02 authority"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        for i in rest:
            print (i)
            print ("------")
        cursor.close()
        self.closeCon()

    # 添加一个值
    def addOne(self):
        try:
            sql = "INSERT INTO user02(username,password) VALUES(%s,%s);"
            cursor = self.conn.cursor()
            cursor.execute(sql, ("aa", "bb"))
            self.conn.commit()
            cursor.close()
            print ("插入数据成功")
        except Exception as e:
            print (e + "插入数据库异常")
            self.conn.rollback()
        self.closeCon()



# def select_mysql(username):
#     conn = mdb.connect(**config)
#     cursor = conn.cursor()
#     cursor.execute('select * from user02 where username = %s', (username,))
#     values = cursor.fetchall()
#     print(values)
#     print('----select_mysql success----')
#     return values

