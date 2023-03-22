import mysql.connector as sql
try:
    an = input("Enter accno :")
    amt = input("Enter amount :")
    conn = sql.connect(database='accinfo', user='root', passwd='')
    cmd = "Update accmaster set balance=balance+'"+amt+"' where accno='"+an+"'"
    cur = conn.cursor()
    cur.execute(cmd)
    if cur.rowcount == 1:
        print(f"Amount {amt} Deposited in account no. {an}")
        conn.commit()
    else:
        print("Account not found")
    conn.close()
except Exception as e:
    print("Error :", e)
