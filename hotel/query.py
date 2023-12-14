import sqlite3

connection = sqlite3.connect("hotels.db")

cursor = connection.cursor()

hotel= cursor.execute("select * from hotel")
print(hotel.fetchall())
customer=cursor.execute("select * from customer")
print(customer.fetchall())
