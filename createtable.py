import mysql.connector
mydb=mysql.connector.connect(
	host='localhost',
	user='sachin',
	password='Raoinfotech@123',
	database='test'
)
mycursor=mydb.cursor()
mycursor.execute("create table customers(name VARCHAR(244),eddress VARCHAR(255))")
