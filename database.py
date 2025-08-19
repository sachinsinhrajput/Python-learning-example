import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="sachin",
    password="Raoinfotech@123",
    database="test"
)

cursor = conn.cursor()
cursor.execute("SELECT *FROM emp;")

for row in cursor.fetchall():
    print(row)

conn.close()

