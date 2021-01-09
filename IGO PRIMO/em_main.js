const users = [
	{
		name: 'Osvaldo',
		lastname: 'Mccants',
		email: 'svaldomcantos@gmail.com',
		gender: 'male',
		confirmed: true
	},
	{
		name: 'Sandee',
		lastname: 'Snelson',
		email: 'sandeesandee@yahoo.com',
		gender: 'female',
		confirmed: true
	},
	{
		name: 'Everette',
		lastname: 'Epperson',
		email: 'epperson24@gmail.com',
		gender: 'male',
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
		name: 'Duncan',
		lastname: 'Detwiler',
		email: 'detwillerd@bigmir.net',
		gender: 'male',
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
		name: 'Carlos',
		lastname: 'Conkle',
		email: 'carlos228@bigmir.net',
		gender: 'male',
		confirmed: true
	},
	{
		name: 'Lucio',
		lastname: 'Lobel',
		email: 'luciol@gmail.com',
		gender: 'male',
		confirmed: true
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