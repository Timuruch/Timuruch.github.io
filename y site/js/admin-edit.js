let admin = JSON.parse( localStorage.getItem("admin"));
if(admin == false || admin == null){
    window.location = "index.html";
}

function tp(){
    window.location = "../index.html";
    localStorage.setItem("admin", false);
}


function add(){
    var name = document.getElementById("name").value;
    var image = document.getElementById("image").value;
    var price = document.getElementById("price").value;
    var count = document.getElementById("count").value;
    var a = [name, image, price, count];
    
    let num = JSON.parse(localStorage.getItem("num"));
    localStorage.setItem(`prodic${num}`, JSON.stringify(a)); 
    num = num + 1;
    localStorage.setItem("num", JSON.stringify(num));
    displayMessage('message-success', 'Admin', 'Ваш товар було успішно добавлено!', 4000);
    setTimeout(function (){
        location.reload();
    }, 4000);
}