import mysql.connector
mydb=mysql.connector.connect(
	host='localhost',
	user='sachin',
	password='Raoinfotech@123',
	database='test'
)
mycursor=mydb.cursor()
mycursor.execute("SELECT *FROM customers ORDER BY name")
results=mycursor.fetchall()
for x in results:
	print(x)
