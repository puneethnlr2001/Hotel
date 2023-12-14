<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/add.css">
</head>
<body>
<h2>Update customer</h2>
<hr/>
<div class="center">
<form action="/updateb" method="post">
  <input type="hidden" name="id" value="{{id}}"/>
  <p>customer_id: <input name="customer_id" value="{{customer_id}}"/></p>
  <p>customer_name: <input name="customer_name" value="{{customer_name}}"/></p>
  <p>phone_number: <input name="phone_number" value="{{phone_number}}"/></p>
  <p>id : <imput name="id" values="{{id}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
</div>
<hr/>
</body>
</html>