
function buy(){
    var prod = JSON.parse(localStorage.getItem("products"));
    var ll = JSON.parse(localStorage.getItem("temp_order"));
    var coun = document.getElementById("count").value;
    var on = prod[ll].price * coun;
    console.log(on);
    const new_product ={
        name:  document.getElementById("name").value,
        cv: document.getElementById("cv").value,
        price: on,
        count: document.getElementById("count").value,
        phone: document.getElementById("phone").value,
    } 
    console.log(new_product);
    let zakaz = JSON.parse(localStorage.getItem("orders"));
    //перевіряємо чи пустий
    if(zakaz == null){
        //якщо пустий то рівний порожньому масиву
        zakaz = []
    }
    //додаємо в кінець вже існуючого списку новий товар
    zakaz.push(new_product)
    
    //зберігаємо змінений масив (з новим товаром)
    localStorage.setItem(`orders`, JSON.stringify(zakaz)); 

    //num тут буде довжина масиву (кількість товарів);

    displayMessage('message-success', 'Purshchase', 'Ok', 4000);
    setTimeout(function (){
        window.location = "succes.html";
    }, 4000);
}

function showMoney(){
    var prod = JSON.parse(localStorage.getItem("products"));
    var ll = JSON.parse(localStorage.getItem("temp_order"));
    var shower = document.getElementById("money");
    var coun = document.getElementById("count").value;
    var on = prod[ll].price * coun;
    console.log(on);
    shower.innerHTML = `Загальна сума ${on}грн`;
}
showMoney();