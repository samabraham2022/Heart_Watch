import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="myhmsdb"
)
def updater(rate,pid):
    mycursor = mydb.cursor()
    sql = "UPDATE patreg SET Heart_Rate = '"+str(rate)+"' WHERE pid = '"+str(pid)+"'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
updater(105,11)