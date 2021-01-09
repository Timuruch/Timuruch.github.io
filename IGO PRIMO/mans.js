<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Тема 14</title>
</head>
<style>
body{
	margin: 0;
	padding: 0;
	font-family: sans-serif;
}
h2{
	font-size: 30px;
}
table{
	border-spacing: 0px;
	width: 800px;
	margin: 50px auto;
}
tr:nth-child(2n){
	background: rgba(135, 138, 137, 0.1)
}
th, td{
	border-top: 1px solid gray;
	border-left: 1px solid gray;
	border-rigth: 1px solid gray;
	padding: 4px 8px;
}
th{
	padding: 18px 8px;
}
td:last-child, th:last-child {
	border-right: 1px solid gray;
}
tr:last-child td {
	border-bottom: 1px solid gray;
}
.icon{
	max-width: 30px;
	max-height: 40px;
}
.centered{
	text-align:center;
}

.links{
	display: flex;
	max-width: 1000px;
	flex-wrap: wrap;
	justify-content: center;
	margin: 0 auto;
}
.links > a {
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 5px 10px;
	background: #5b5c5a;
	text-decoration: none;
	margin: 2px;
	border-radius: 8px;
	font-weight: 800;
	color: white;
	transition: opacity 0.5s; 
}
.links > a:hover {
	opacity: 0.8;
}

.links > .active_link{
	background: #7fcf30;
	color: navy
}
</style>
<body>
	<h2 align="center">Список усіх користувачів</h2>
	
	<div class="links">
		<a href="index.html" class="active_link">Усі користувачі</a>
		<a href="mans.html">Користувачі чоловіки</a>
		<a href="girls.html">Користувачі жінки</a>
		<a href="EnterEmail.html">Користувачі з підтверженим email</a>
		<a href="GMAIL.html">Email від google</a>
		<a href="YAHOO.html">Email від yahoo</a>
		<a href="BIGMIR.html">Email від bigmir</a>
	</div>
	
	<table class="table">
		<thead>
			<tr>
				<th>№</th>
				<th>Name</th>
				<th>Gender</th>
				<th>Email</th>
				<th>Confirmed</th>
			</tr>
		</thead>
		
		<tbody>
			<tr>
				<td>1</td>
				
				<td>Petro Ivanov</td>
				
				<td class="centered"> <img src="male.svg" class="icon icon_male"> </td>
				
				<td>pertoivanov@gmail.com</td>
				
				<td class="centered"> <input type="checkbox"> </td>
			</tr>
			
			<tr>
				<td>2</td>
				
				<td>Tania Lyenko</td>
				
				<td class="centered"> <img src="female.svg" class="icon"> </td>
				
				<td>tanialy@bigmir.net</td>
				
				<td class="centered"> <input type="checkbox" checked> </td>
			</tr>	
			
			<tr>
				<td>2</td>
				
				<td>Olia Zenuk</td>
				
				<td class="centered"> <img src="female.svg" class="icon"> </td>
				
				<td>tanialy@bigmir.net</td>
				
				<td class="centered"> <input type="checkbox" > </td>
			</tr>
			
			<tr>
				<td>4</td>
				
				<td>Ivan Petrov</td>
				
				<td class="centered"> <img src="male.svg" class="icon icon_male"> </td>
				
				<td>ivan007@yahoo.com</td>
				
				<td class="centered"> <input type="checkbox" checked> </td>
			</tr>
		</tbody>
	</table>
	
	<script src="girls_main.js"></script>
</body>
</html>