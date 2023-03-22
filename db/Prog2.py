import mysql.connector as sql

try:
    conn = sql.connect(database='accinfo', user='root', passwd='')
    query = "create table IF NOT EXISTs accmaster (accno INT,balance INT)"
    cur = conn.cursor()
    cur.execute(query)
    for i in range(2):
        an = input("Enter accno. :")
        amt = input("Enter amount :")
        info = [an, amt]
        cmd = "INSERT INTO `accmaster`(`accno`, `balance`) VALUES (%s,%s)"
        curx = cur.execute(cmd, info)
        print("Data Inserted")
        conn.commit()
    conn.close()

except Exception as e:
    print('Error :', e)
