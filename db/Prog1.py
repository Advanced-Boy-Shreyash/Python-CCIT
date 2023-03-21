import mysql.connector as sql

try:
    conn = sql.connect(host='', user='test', passwd='1234')
    print("Connected")
except Exception as e:
    print("Error:", e)
