let admin = JSON.parse( localStorage.getItem("admin"));
if(admin == false || admin == null){
    window.location = "index.html";
}

function tp(){
    window.location = "../index.html";
    localStorage.setItem("admin", false);
}


function add(){
    //створюємо новий товар як об'єкт
    const new_product ={
        name:  document.getElementById("name").value,
        image: document.getElementById("image").value,
        price: document.getElementById("price").value,
        count: document.getElementById("count").value,
    } 
    
    //дістаємо всі збережені товари як масив (може бути пустим)
    let products = JSON.parse(localStorage.getItem("products"));
    //перевіряємо чи пустий
    if(products == null){
        //якщо пустий то рівний порожньому масиву
        products = []
    }
    //додаємо в кінець вже існуючого списку новий товар
    products.push(new_product)
    
    //зберігаємо змінений масив (з новим товаром)
    localStorage.setItem(`products`, JSON.stringify(products)); 

    //num тут буде довжина масиву (кількість товарів);

    displayMessage('message-success', 'Admin', 'Ваш товар було успішно добавлено!', 4000);
    setTimeout(function (){
        location.reload();
    }, 4000);
}