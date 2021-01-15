let newName = "";
let newLastName = "";
let newAge = "";
let newEmail = "";
let newCity = "";

let users = [
{
	name: 'Петро',
	lastName: 'Коваленко',
	Age: 15,
	Email: 'petro_kovalik228@gmail.com',
	city: 'Lviv'
},
{
	name: 'Петро',
	lastName: 'Коваленко',
	Age: 15,
	Email: 'petro_kovalik228@gmail.com',
	city: 'Lviv'
}
]

let name = "Петро";
let lastName = "Коваленко";
let Age = 15;
let Email = "petro_kovalik228@gmail.com";
let city = "Lviv";

let lop = ``;

const users_table = document.getElementById("users_table");

function showUsers(){
	lop += `
			<tr>
				<td id="name">${name}</td>
				<td id="lastName">${lastName}</td>
				<td id="Year">${Age}</td>
				<td id="email">${Email}</td>
				<td id="city">${city}</td>
			</tr>
	`
	users_table.innerHTML = lop;
}

function changeName(nae){
	name = nae;
	lop = `
			<tr>
				<td id="name">${name}</td>
				<td id="lastName">${lastName}</td>
				<td id="Year">${Age}</td>
				<td id="email">${Email}</td>
				<td id="city">${city}</td>
			</tr>
	`
	users_table.innerHTML = lop;
}

function changeLastname(nae){
	lastName = nae;
	lop = `
			<tr>
				<td id="name">${name}</td>
				<td id="lastName">${lastName}</td>
				<td id="Year">${Age}</td>
				<td id="email">${Email}</td>
				<td id="city">${city}</td>
			</tr>
	`
	users_table.innerHTML = lop;
}

function changeAge(nae){
	Age = nae;
	lop = `
			<tr>
				<td id="name">${name}</td>
				<td id="lastName">${lastName}</td>
				<td id="Year">${Age}</td>
				<td id="email">${Email}</td>
				<td id="city">${city}</td>
			</tr>
	`
	users_table.innerHTML = lop;
}

function changeEmail(nae){
	Email = nae;
	lop = `
			<tr>
				<td id="name">${name}</td>
				<td id="lastName">${lastName}</td>
				<td id="Year">${Age}</td>
				<td id="email">${Email}</td>
				<td id="city">${city}</td>
			</tr>
	`
	users_table.innerHTML = lop;
}

function changeCity(nae){
	city = nae;
	lop = `
			<tr>
				<td id="name">${name}</td>
				<td id="lastName">${lastName}</td>
				<td id="Year">${Age}</td>
				<td id="email">${Email}</td>
				<td id="city">${city}</td>
			</tr>
	`
	users_table.innerHTML = lop;
}

function changeUserData(nam, lasname, ag, emal, ciy){
	name = nam;
	lastName = lasname;
	Age = ag;
	Email = emal;
	city = ciy;
	lop = `
			<tr>
				<td id="name">${name}</td>
				<td id="lastName">${lastName}</td>
				<td id="Year">${Age}</td>
				<td id="email">${Email}</td>
				<td id="city">${city}</td>
			</tr>
	`
	users_table.innerHTML = lop;
}



