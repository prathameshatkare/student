import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="studentdbms"
)

if connection.is_connected():
    print("Connected to MySQL database")
