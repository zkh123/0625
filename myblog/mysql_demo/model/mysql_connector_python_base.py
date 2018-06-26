#-*-coding:utf-8-*-
import mysql.connector

import sys  # 提供了许多函数和变量来处理 Python 运行时环境的不同部分.

reload(sys)
sys.setdefaultencoding('utf8')

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'root',
    'port':3306,
    'database':'test',
    'charset':'utf8'
}

def mysql_test():
    print('----start----')
    conn = mysql.connector.connect(host='127.0.0.1',
                                   user='root',
                                   password='root',
                                   port=3306,
                                   database='test',
                                   use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Kebi'])
    cursor.rowcount
    conn.commit()
    cursor.close()
    print('----create mysql database success----')

'''
新增数据
'''
def insert_mysql():
    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='root', port=3306, database='test',use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Jamse'])
    cursor.rowcount
    conn.commit()
    cursor.close()
    print('----insert success----')


def select_mysql():
    conn = mysql.connector.connect(host='127.0.0.1',user='root', password='root',port=3306, database='test')
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('2',))
    values = cursor.fetchall()
    print(values)
    print('----select success----')
    return values

def select_mysql2():
    conn = mysql.connector.connect(host='127.0.0.1',user='root', password='root',port=3306, database='test',use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('select * from user02 where id = %s', ('1',))
    values = cursor.fetchall()
    print('----select_mysql2 success----')
    return values

'''
条件查询 返回一条数据
'''
def select_mysql3():
    conn = mysql.connector.connect(host='127.0.0.1',user='root', password='root',port=3306, database='test',charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from user02 where id = %s', ('1',))
    values = cursor.fetchall()
    print('----select_mysql2 success----')
    return values

'''
根据条件查询 返回list  多条数据。
'''
def selectByUsername(username):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('select * from user02 where username = %s', (username,))
    values = cursor.fetchall()
    print('----selectByUsername success----')
    return values

if __name__ == '__main__':
    select_mysql()
    # insert_mysql()
    # mysql_test()
