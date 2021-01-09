const users = [
	{
		name: 'Maximina',
		lastname: 'Lasso',
		email: 'maximina2002@bigmir.net',
		gender: 'female',
		confirmed: false
	},
	{
		name: 'Sandee',
		lastname: 'Snelson',
		email: 'sandeesandee@yahoo.com',
		gender: 'female',
		confirmed: true
	},
	{
		name: 'Jenise' ,
		lastname: 'Jones',
		email: 'janiejo@gmail.com',
		gender: 'female',
		confirmed: true
	},
	{
		name: 'Verlie',
		lastname: 'Voigt',
		email: 'verlie007@gmail.com',
		gender: 'female',
		confirmed: true
	},
	{
		name: 'Sacha',
		lastname: 'Sherron',
		email: 'sachaato@gmail.com',
		gender: 'female',
		confirmed: true
	},
	{
		name: 'Dani',
		lastname: 'Dehoyos',
		email: 'danid@bigmir.net',
		gender: 'female',
		confirmed: true
	},
	{
		name: 'Lu',
		lastname: 'Laine',
		email: 'lulaine@yahoo.com',
		gender: 'female',
		confirmed: false
	},
	{
		name: 'Tanya',
		lastname: 'Huston',
		email: 'taniahus@bigmir.net',
		gender: 'female',
		confirmed: false 
	},
];

const users_table = document.getElementById("users_table");

let list = ``;

for( i = 0; i < users.length; i++ ){
	let icon = "female.svg";
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