# 在sqlite3数据库“Student.db”中，新建一张名为“userinfo”的表，并插入以下记录后，
# 将王五的Email修改更新为Wangwu@163.com后，将所有的记录打印输出。
import sqlite3

conn = sqlite3.connect('Student.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS userinfo")

sql_text_1 = '''CREATE TABLE userinfo
             (
             StuNumber NUMBER,
             Name TEXT,
             ClassNumber TEXT,
             Email TEXT
             )
             '''
cur.execute(sql_text_1)

sql_text_2 = "INSERT INTO userinfo VALUES (20190001,'张三', 'C01', 'Zhangsan@163.com')"
cur.execute(sql_text_2)

data = [
    (20190002, '李四', 'C02', 'Lisi@163.com'),
    (20190003, '王五', 'C03', 'Wangwu@qq.com'),
    (20190004, '小明', 'C04', 'Xiaoming@qq.com')
]
cur.executemany('INSERT INTO userinfo VALUES(?,?,?,?)', data)
conn.commit()

cur.execute('SELECT * FROM userinfo')
rows = cur.fetchall()
for row in rows:
    print(row)

print('------------------------------------------')
cur.execute("UPDATE userinfo SET Email = 'Wangwu@163.com' WHERE Name = '王五'")
cur.execute('SELECT * FROM userinfo')
rows = cur.fetchall()
for row in rows:
    print(row)