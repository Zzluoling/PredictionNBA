import pymysql

db = pymysql.connect("localhost", "root", "", "db2")
cursor = db.cursor()