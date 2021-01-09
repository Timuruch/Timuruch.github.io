const users = [
	{
		name: 'Osvaldo',
		lastname: 'Mccants',
		email: 'svaldomcantos@gmail.com',
		gender: 'male',
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
		name: 'Dante',
		lastname: 'Duchesne',
		email: 'danteduch@yahoo.com',
		gender: 'male',
		confirmed: false 
	},
	{
		name: 'Duncan',
		lastname: 'Detwiler',
		email: 'detwillerd@bigmir.net',
		gender: 'male',
		confirmed: true
	},
	{
		name: 'Theron',
		lastname: 'Tisby',
		email: 'tisbyteo@gmail.com',
		gender: 'male',
		confirmed: false 
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