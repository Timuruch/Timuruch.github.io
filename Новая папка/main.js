const allOrders = [
	{
		product: "Монітор Sony 8764d",
		price: 2430,
		dolar: 86,
		type: 'монітор'
	},
	{
		product: "Клавіатура Rizen 1905b",
		price: 1350,
		dolar: 48,
		type: 'клавіатура'
	},
	{
		product: "Монітор Samsung 187b",
		price: 3240,
		dolar: 115,
		type: 'монітор'
	},
	{
		product: "Роутер від Asus 094g",
		price: 1080,
		dolar: 38,
		type: 'роутер'
	},
	{
		product: "Клавіатура Rizen 2705c",
		price: 1215,
		dolar: 43,
		type: 'клавіатура'
	},
	{
		product: "Клавіатура 1905b",
		price: 1242,
		dolar: 44,
		type: 'клавіатура'
	},
	{
		product: "Монітор Sony 8764d",
		price: 2160,
		dolar: 76,
		type: 'монітор'
	},
	{
		product: "Монітор Samsung 734s",
		price: 4860,
		dolar: 173,
		type: 'монітор'
	},
	{
		product: "Роутер від Asus 091g",
		price: 810,
		dolar: 28,
		type: 'роутер'
	},
	{
		product: "Клавіатура Rizen 1905b",
		price: 1566,
		dolar: 55,
		type: 'клавіатура'
	},
	{
		product: "Монітор Samsung 187b",
		price: 2700,
		dolar: 96,
		type: 'монітор'
	},
	{
		product: "Роутер від Asus 094g",
		price: 1242,
		dolar: 44,
		type: 'роутер'
	},
];

const royter = [
{
		product: "Роутер від Asus 094g",
		price: 1080,
		dolar: 38,
		type: 'роутер'
},
{
		product: "Роутер від Asus 091g",
		price: 810,
		dolar: 28,
		type: 'роутер'
},
{
		product: "Роутер від Asus 091g",
		price: 810,
		dolar: 28,
		type: 'роутер'
},
]

const monitor = [
{
		product: "Монітор Sony 8764d",
		price: 2430,
		dolar: 86,
		type: 'монітор'
},
{
		product: "Монітор Samsung 187b",
		price: 3240,
		dolar: 115,
		type: 'монітор'
},
{
		product: "Монітор Sony 8764d",
		price: 2160,
		dolar: 76,
		type: 'монітор'
},
{
		product: "Монітор Samsung 734s",
		price: 4860,
		dolar: 173,
		type: 'монітор'
},
{
		product: "Монітор Samsung 187b",
		price: 2700,
		dolar: 96,
		type: 'монітор'
},
]

const claviat = [
{
		product: "Клавіатура Rizen 1905b",
		price: 1350,
		dolar: 48,
		type: 'клавіатура'
},
{
		product: "Клавіатура Rizen 2705c",
		price: 1215,
		dolar: 43,
		type: 'клавіатура'
},
{
		product: "Клавіатура 1905b",
		price: 1242,
		dolar: 44,
		type: 'клавіатура'
},
]
var allmomey = 0;
for(x = 0;x < allOrders.length;x++){
	var body = document.getElementById("result");
	allmomey = allmomey + allOrders[x].price;
	body.innerHTML = `Загалом витрачено - ${allmomey}UAH`;
}

function showUsers(){
	var body = document.getElementById("orders_table");
	let er = ``;
	body.innerHTML = er;
	for(x = 0;x < allOrders.length;x++){
		er += `
		<tr>
			<td>${x + 1}</td>
			<td>${allOrders[x].product}</td>
			<td>${allOrders[x].type}</td>
			<td>${allOrders[x].price}.00 UAH</td>
		</tr>
		`
	}
	body.innerHTML = er;
}
showUsers();

function showDolar(){
	let er = ``;
	var body = document.getElementById("orders_table");
	body.innerHTML = er;
		for(x = 0;x < allOrders.length;x++){
		er += `
		<tr>
			<td>${x + 1}</td>
			<td>${allOrders[x].product}</td>
			<td>${allOrders[x].type}</td>
			<td>${allOrders[x].dolar}.00 USD</td>
		</tr>
		`
	}
	body.innerHTML = er;
}

function showKl(){
	let er = ``;
	var body = document.getElementById("orders_table");
	body.innerHTML = er;
		for(x = 0;x < claviat.length;x++){
		er += `
		<tr>
			<td>${x + 1}</td>
			<td>${claviat[x].product}</td>
			<td>${claviat[x].type}</td>
			<td>${claviat[x].price}.00 UAH</td>
		</tr>
		`
	}
	body.innerHTML = er;
} 

function showMon(){
	let er = ``;
	var body = document.getElementById("orders_table");
	body.innerHTML = er;
		for(x = 0;x < monitor.length;x++){
		er += `
		<tr>
			<td>${x + 1}</td>
			<td>${monitor[x].product}</td>
			<td>${monitor[x].type}</td>
			<td>${monitor[x].price}.00 UAH</td>
		</tr>
		`
	}
	body.innerHTML = er;
} 


function showRoy(){
	let er = ``;
	var body = document.getElementById("orders_table");
	body.innerHTML = er;
		for(x = 0;x < royter.length;x++){
		er += `
		<tr>
			<td>${x + 1}</td>
			<td>${royter[x].product}</td>
			<td>${royter[x].type}</td>
			<td>${royter[x].price}.00 UAH</td>
		</tr>
		`
	}
	body.innerHTML = er;
} 

function search(){
	var op = document.getElementById("type_filter").value;
	if(op == "клавіатура"){
		showKl();
	}else if(op == "монітор"){
		showMon();
	}else if(op == "роутер"){
		showRoy();
	}
}




