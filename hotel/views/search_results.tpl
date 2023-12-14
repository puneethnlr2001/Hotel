<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
    <head>
    <link rel="stylesheet" type="text/css" href="/static/search.css">
    </head>
</head>
<body>
    <h1>Search Results</h1>
    <p>Results for '{{ search_query }}':</p>
    <div class="customers">
       <table >
     
    %if results:
     <tr>
        <th>customer Id</th>
        <th>customer name</th>
        <th>phone number</th>
        
        <th>id</th>
      </tr>
      <tr>
      %for n in results:
      <tr>
        <td>{{n[0]}}</td>
        <td>{{n[1]}}</td>
        <td>{{n[2]}}</td>
        <td>{{n[3]}}</td>
        <td>{{n[4]}}</td>

      </tr>
      %end 
    %else:
      <tr>

      <td>Enter valid customer id!!</td>
      </tr>

      </tr>  
  </table>
  </div>
</body>
</html>