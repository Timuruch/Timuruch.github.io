function drawPeople(){
    var body = document.getElementById("users_table");
    let text = ``;
    for(var x = 0;x < users.length;x++){
        text += `
        <tr>
			<td>${x+1}</td>
			<td>${users[x].name}</td>
			<td>${users[x].email}</td>
			<td>
			<button class="btn btn-sm btn-primary" onclick="info('${x}')">
				Детально
			</button>
			</td>
			<td>
				<button class="btn btn-danger" onclick="delet('${x}')">Видалити</button>
			</td>
		</tr>`
    }
    body.innerHTML = text;
}
drawPeople()

function hideModal(){
    var moda = document.getElementById("myModal");
    moda.style.display = "none";
}

function delet(id){
    users.splice(id, 1);
    drawPeople();
}

function info(id){
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
    let info = `
    <div class="modal-content">
		  <div class="modal-header text-center">
			<h4>Повна інформація про користувача</h4>
			<span class="close" onclick="hideModal()">&times;</span>
		  </div>
		  <div class="modal-body py-3">
			<p><b>Ім'я:</b> ${users[id].name}</p>
			<p><b>Місто:</b> ${users[id].address.city}</p>
			<p><b>Email:</b> ${users[id].email}</p>
			<p><b>Телефон:</b> ${users[id].phone}</p>
			<p><b>Сайт:</b> ${users[id].website}</p>
			<p><b>Компанія:</b> ${users[id].company.name}</p>
		  </div>
		  <div class="modal-footer">
			<button class="btn btn-sm btn-secondary" onclick="hideModal()">Скасувати</button>
			<a class="btn btn-sm btn-success" href="https://www.google.com.ua/maps/@${users[id].address.geo.lat},${users[id].address.geo.lng},13.12z">Показати на карті</a>
			<a class="btn btn-sm btn-warning" href="mailto: ${users[id].email}">Написати email</a>
		  </div>
		</div>
    `
    modal.innerHTML = info;
}

