import mysql.connector as sql

try:
    conn = sql.connect(database='accmaster', user='root', passwd='')
    query = "create table IF NOT EXISTs accmaster (accno INT,amt INT)"
    cur = conn.cursor()
    cur.execute(query)
    for i in range(2):
        an = input("Enter accno. :")
        amt = input("Enter amount :")
        info = [an, amt]
        cmd = "INSERT INTO `accmaster`(`accno`, `amt`) VALUES (an'+','+'am)"
        curx = cur.execute(cmd, info)
        print("Data Inserted")
        conn.commit()
    conn.close()

except Exception as e:
    print('Error :', e)
