import mysql.connector
mydb=mysql.connector.connect(
	host='localhost',
	user='sachin',
	password='Raoinfotech@123',
	database='test'
)
mycursor=mydb.cursor()
sql="UPDATE customers SET eddress='rajkott 05'WHERE eddress='valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) updated")
