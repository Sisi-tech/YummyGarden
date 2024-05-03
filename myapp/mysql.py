import mysql.connector

connection = mysql.connector.connect(user='root', password='Bayside@2024')

cursor = connection.cursor()
cursor.execute("Create DATABASE SCoffee")
cursor.execute("USE SCoffee")


connection.close()
