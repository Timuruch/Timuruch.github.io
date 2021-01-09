const users = [
	{
		name: 'Sandee',
		lastname: 'Snelson',
		email: 'sandeesandee@yahoo.com',
		gender: 'female',
		confirmed: true
	},
	{
		name: 'Dante',
		lastname: 'Duchesne',
		email: 'danteduch@yahoo.com',
		gender: 'male',
		confirmed: false 
	},
	{
		name: 'Luna',
		lastname: 'Logan',
		email: 'lunalogan@yahoo.com',
		gender: 'female',
		confirmed: false
	},
	{
		name: 'Lu',
		lastname: 'Laine',
		email: 'lulaine@yahoo.com',
		gender: 'female',
		confirmed: false
	},
	{
		name: 'Daniel',
		lastname: 'Coto',
		email: 'dannyc@yahoo.com',
		gender: 'male',
		confirmed: true 
	}
];

const users_table = document.getElementById("users_table");

let list = ``;

for( i = 0; i < users.length; i++ ){
	let icon = "male.svg";
	if(users[i].gender == "female"){
		icon = "female.svg";
	}
	var chew = "";
	if(users[i].confirmed == true){
		chew = "checked";
	}
	list += 
	`
	<tr>
		<td>${i + 1}</td>
		
		<td>${users[i].name} ${users[i].lastname}</td>
		
		<td class="centered"> <img src=${icon} class="icon"> </td>
		
		<td>${users[i].email}</td>
		
		<td class="centered"> <input type="checkbox" ${chew}> </td>
	</tr>
	`
}





users_table.innerHTML = list;