import sqlite3

connection = sqlite3.connect("hotels.db")
def get_customers(id=None):
    cursor = connection.cursor()

    if id is None:
        cursor.execute("SELECT * FROM customer")
    else:
        cursor.execute(f"SELECT * FROM customer WHERE customer_id={id}")

    rows = cursor.fetchall()
    customers = [{'customer_id': row[0], 'customer_name': row[1], 'phone_number': row[2],'id':row[3]} for row in rows]

    return customers
def get_items(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select * from hotel")
    else:
        rows = cursor.execute(f"select * from hotel where hotel_no={id}")
    rows = cursor.fetchall()
    rows = list(rows)
    hotel = [{'hotel_no': row[0], 'name': row[1], 'location': row[2]} for row in rows]
    return hotel


def add_item(hotel_no,name,location):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO hotel (hotel_no, name, location) VALUES (?, ?, ?)", (hotel_no,name,location))
    connection.commit()

def add_customer(customer_id,customer_name,phone_number,id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customer (customer_id, customer_name, phone_number,id) VALUES (?, ?, ?, ?)", (customer_id,customer_name,phone_number, id))
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from hotel where hotel_no={id}")
    connection.commit()
def delete_customer(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from customer where customer_id={id}")
    connection.commit()
def update_customer(customer_id, customer_name, phone_number, id):
    cursor = connection.cursor()
    cursor.execute(f"update customer set id={id},customer_name='{customer_name}',phone_number='{phone_number}' where hotel_no={id}")
    connection.commit()    
def update_item(hotel_no,name,phone_number):
    cursor = connection.cursor()
    cursor.execute(f"update hotel set hotel_no='{hotel_no}',name='{name}',phone_number='{phone_number}' where hotel_no={id}")
    connection.commit()
def search_hotel(name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT customer.customer_id, customer.customer_name, customer.phone_number,hotel.name,customer.id FROM hotel JOIN customer ON hotel.hotel_no = customer.id WHERE hotel.name = '{name}'")
    connection.commit()
    results = cursor.fetchall()
    return results