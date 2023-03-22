import mysql.connector as sql
try:
    conn = sql.connect(host='localhost', user='root', passwd='')
    cur = conn.cursor()
    cmd = "create database if not exists accinfo"
    cur.execute(cmd)
    print("Database Created")
    conn2 = sql.connect(database="accinfo", user="root", passwd="")
    query = "create table if not exists accmaster(accno INT,balance INT)"
    cur2 = conn2.cursor()
    cur2.execute(query)
    print("Table Created")
    for info in range(5):
        an = input("Enter accno. :")
        amt = input("Enter amount :")
        cmd2 = "INSERT INTO accmaster SET accno='"+an+"', balance='"+amt+"'"
        cur3 = conn2.cursor()
        cur3.execute(cmd2)
        conn2.commit()
        print("Accinfo Inserted")
    conn2.close()
    conn.commit()
    conn.close()
except Exception as e:
    print('Error :', e)
