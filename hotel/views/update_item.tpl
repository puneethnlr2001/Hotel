<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/add.css">
</head>
<body>
<h2>Update hotel</h2>
<hr/>
<div class="center">
<form action="/update" method="post">
  <input type="hidden" name="id" value="{{id}}"/>
  <p>hotel_no: <input name="hotel_no" value="{{hotel_no}}"/></p>
  <p>name: <input name="name" value="{{name}}"/></p>
  <p></p>
  <p><button type="submit">Submit</button></p>
</form>
</div>
<hr/>
</body>
</html>