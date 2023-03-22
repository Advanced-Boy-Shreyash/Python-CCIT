import mysql.connector as sql
try:
    conn = sql.connect(host="localhost", user="root",
                       passwd="", database="accinfo")
    an = input("Enter accno. :")
    amt = int(input("Enter amt to withdraw :"))
    cmd = "select balance from accmaster where accno='"+an+"'"
    cur = conn.cursor()
    cur.execute(cmd)
    row = cur.fetchone()
    if row != 0 or row != None:
        bal = row[0]
        print("Available Balance is", bal)
        if bal >= amt:
            cmd = "Update accmaster set balance = balance-%s where accno=%s"
            curx = conn.cursor()
            curx.execute(cmd, [an, amt])
            conn.commit()
            print(
                f"Amount {amt} withrawn from account no. {an} and available balance is Rs.{bal-amt}")
        else:
            print("Insufficient Balance.")
    else:
        print("Account not found")
except Exception as e:
    print("Error :", e)
