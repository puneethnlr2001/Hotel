import sqlite3

connection = sqlite3.connect("hotels.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table hotel")
    cursor.execute("drop table customer")
except:
    pass

cursor.execute("create table hotel(hotel_no integer primary key, name text, location text)")
cursor.execute("create table customer(customer_id integer primary key, customer_name text, phone_number integer, id integer, foreign key(id) references hotel(hotel_no))")
cursor.execute(""" INSERT INTO hotel VALUES(1,"kent", "kent")""")
cursor.execute("""INSERT INTO customer VALUES(1,"puneeth KUMAR", 12345,1)""")


connection.commit()
connection.close()
