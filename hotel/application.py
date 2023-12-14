from bottle import Bottle,template, redirect, request,static_file
import database
app = Bottle()
@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='')
@app.route("/")
def get_list():
    rows = database.get_items()
    n=database.get_customers()
    return template("list", hotel=rows,customer=n)
@app.post('/search')
def search():
    search_query = request.forms.get('search_query', '')
    results=database.search_book(search_query)
    return template('search_results', results=results, search_query=search_query)
@app.route("/add")
def get_add():
    return template("add_item.tpl")

@app.post("/add")
def post_add():
    hotel_no = request.forms.get("hotel_no")
    name=request.forms.get("name")
    location=request.forms.get("location")
    database.add_item(hotel_no,name,location)
    redirect("/")
@app.route("/update/<hotel_no>")
def get_update(hotel_no):
    rows = database.get_items(hotel_no)
    if len(rows) != 1:
        redirect("/")
    hotel_no = rows[0]['hotel_no']
    name = rows[0]['name']
    location = rows[0]['location']

    return template("update_item.tpl",hotel_no=hotel_no,name=name,location=location)

@app.post("/update")
def post_update():
    hotel_no = request.forms.get("hotel_no")
    name=request.forms.get("name")
    location=request.forms.get("location")
    database.update_item(hotel_no,name,location)
    redirect("/")
@app.route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/")
@app.route("/addb")
def get_addb():
    return template("add_customer.tpl")
@app.post("/addb")
def post_add():
    customer_id = request.forms.get("customer_id")
    customer_name = request.forms.get("customer_name")
    phone_number=request.forms.get("phone_number")
    id=request.forms.get("id")
    database.add_customer(customer_id,customer_name,phone_number,id)
    redirect("/")

@app.route("/deletecustomer/<id>")
def get_delete(id):
    database.delete_customer(id)
    redirect("/")
@app.route("/updateb/<id>")
def get_updatecustomer(id):
    b = database.update_customer(id)
    if len(b) != 1:
        redirect("/list")
    customerid = b[0]['customer_id']
    customername = b[0]['customer_name']
    phonenumber = b[0]['phone_number']
    

    return template("update_customer.tpl", customer_id=customerid,customer_name=customername,phone_number=phonenumber)

@app.post("/updateb")
def post_updatecustomer():
    customer_id = request.forms.get("customer_id")
    customer_id=int(customer_id)
    customer_name = request.forms.get("customer_name")
    phone_number=request.forms.get("phone_number")
    customer_id=request.forms.get("customer_id")
    customer_id=int(customer_id)
    database.update_customer(customer_id,customer_name,phone_number,id)
    redirect("/")
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)