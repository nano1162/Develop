import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="0000", db="societydb", charset="utf8")
cur = db.cursor()
sql = f"UPDATE society_table set date_d = date_d + 1"
cur.execute(sql)

db.commit()
cur.close()
db.close()
