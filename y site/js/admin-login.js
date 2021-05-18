let admin = JSON.parse( localStorage.getItem("admin"));
if(admin == true){
    window.location = "admin-edit.html";
}

function sumbit(){
    const password = document.getElementById("adminPassword").value
    if(password == "12345678"){
        displayMessage('message-success', 'Admin', 'Успішний вхід', 2000);
        setTimeout(function (){
            localStorage.setItem("admin", JSON.stringify(true))
            window.location = "admin-edit.html"; 
        }, 2000)
    } else {
        displayMessage('message-error', 'Admin', 'Пароль введено неправильно!', 4000);
        document.getElementById("adminPassword").value = "";
    }
}