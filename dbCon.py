import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hema@098",
    port="3306"
)
print('connected:',mydb)
my_cursor=mydb.cursor()
#my_cursor.execute("CREATE DATABASE dbname")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
