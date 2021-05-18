
function refresh(){
    displayMessage('message-warning', 'Admin', 'Сторінка перезапустится через 4 секунди', 4000);
    setTimeout(function (){
        location.reload();
    }, 4000);
    
}

function del(){
    var chtuka = document.getElementById("boom")
    chtuka.style.display = "none";
    localStorage.clear();
    localStorage.setItem("admin", JSON.stringify(true))
    localStorage.setItem("num", JSON.stringify(0));
}

function hide(){
    var chtuka = document.getElementById("boom")
    chtuka.style.display = "none";
}

function alert(){
    var chtuka = document.getElementById("boom")
    chtuka.style.display = "flex";
}


function vulyh(num){
    let nim = JSON.parse(localStorage.getItem("num"));
    for(var x = 0;x < nim;x++){
        if(x == num){
            localStorage.removeItem(`prodic${x}`)
        }else{
            var jora = JSON.parse(localStorage.getItem(`prodic${x}`));
            localStorage.removeItem(`prodic${x}`)
            var y = x + 1;
            localStorage.setItem(`prodic${y}`, jora)

        }
    }
    location.reload();

}

function edit(pa){
    var name = document.getElementById("name").value;
    var price = document.getElementById("price").value;
    var photo = document.getElementById("photo").value;
    var count = document.getElementById("count").value;
    const lol = [name, photo, price, count];
    console.group(lol);
    localStorage.setItem(`prodic${pa}`, JSON.stringify(lol))
    location.reload();
}

function sho(pa){
    var jora = JSON.parse(localStorage.getItem(`prodic${pa}`));
    var cho = document.getElementById("cho");
    cho.innerHTML = `
    <div class="conta" style="border: 1px solid black;width: 200px">
    <p>Назва</p>
    <input type="text" id="name">
    <p>Ціна</p>
    <input type="number" id="price">
    <p>Фото</p>
    <input type="text" id="photo">
    <p>Кількість</p>
    <input type="number" id="count">
    <button type="button" class="btn btn-success" onclick="edit('${pa}')">Змінити</button>
    </div>
    `
    var name = document.getElementById("name").value = jora[0];
    var price = document.getElementById("price").value = jora[2];
    var photo = document.getElementById("photo").value = jora[1];
    var count = document.getElementById("count").value = jora[3];

}


function up(){
    var body = document.getElementById("pok")
    let num = JSON.parse(localStorage.getItem("num"));
    let vas = ``;
    for(var x = 0;x < num;x++){
        var jora = JSON.parse(localStorage.getItem(`prodic${x}`));
        console.log(jora)
        vas += `
        <tr>
        <td>${x + 1}</td>
        <td>${jora[0]}</td>
        <td>${jora[2]}</td>
        <td>${jora[1]}</td>
        <td>${jora[3]}</td>
        <td class="text-center"><button type="button" class="btn-close" aria-label="Close" onclick="vulyh(${x})"></button></td>
        <td class="text-center"><button type="button" class="btn btn-warning" onclick="sho('${x}')">Edt</button></td>
        </tr>
        `
    }
    
    body.innerHTML = vas;
}

up()