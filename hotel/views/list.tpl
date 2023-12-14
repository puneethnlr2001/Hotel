<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/list.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
<h1>HOTEL RESERVATION</h1>
<br>
<h2>HOTEL</h2>
<div class="hotel">
<table >
    <tr>
      <th>S.no</th>
      <th>HOTEL</th>
      <th>hotel name</th>
      <th>phone number</th>
    </tr>
    <tr>
    %for item in hotel:
    <tr>
      
      <td>{{item['hotel_no']}}</td>
      <td>{{item['name']}}</td>
      <td>{{item['location']}}</td>
      <td><a href="/delete/{{str(item['hotel_no'])}}">Delete</a></td>
      <td><a href="/update/{{str(item['hotel_no'])}}"> Update</a></td>
    </tr>
    %end
    </tr>
</table>

<a href="/add">Add new hotel</a>
</div>
<br>
<h2>CUSTOMERS</h2>
<div class="customer">
  <form class="example" action="/search" method="post">
    <label for="search_query">Search:</label>
        <input type="text" id="search_query" name="search_query" placeholder="Search by customer id...">
    <button type="submit"><i class="fa fa-search"></i></button>
  </form>
  <table >
      <tr>
        <th>customer Id</th>
        <th>customer_name</th>
        <th>phone number</th>
        <th>customer_id</th>
      </tr>
      <tr>
      %for n in customer:
      <tr>
        <td>{{n['customer_id']}}</td>
        <td>{{n['customer_name']}}</td>
        <td>{{n['phone_number']}}</td>
        <td>{{n['id']}}</td>
        <td><a href="/deletebor/{{str(n['customer_id'])}}">Delete</a></td>
        <td><a href="/updateb/{{str(n['customer_id'])}}"> Update</a></td>

      </tr>
      %end
     
      </tr>  
  </table>
   <a href="/addb">Add new customer</a>
  </div>
<hr/>
</body>
</html>