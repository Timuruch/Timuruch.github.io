

function show(){
    var body = document.getElementById("car")
    //тут всі товари
    let products = JSON.parse(localStorage.getItem("products"));
    //перевіряємо чи список товарів пустий
    if(products == null){
        //якщо пустий то рівний порожньому масиву
        products = []
    }
    let products_html = ``;

    products.forEach(function(product, index) {
        //тут пиши логіку - Немає в наявності і інше
        console.log(product)
        let nav = `<p class="card-text" style="color: green;">В наявності</p>`
        let but = `<a href="#" class="btn btn-primary" onclick="order(${index})">Купити</a>`
        if(products[index].count == 0){
            nav = `<p class="card-text" style="color: red;">Немає в наявності</p>`
            but = `<a href="#" class="btn btn-primary">Повідомити коли буде у наявності</a>`
        }

        products_html +=
        `
        <div class="card" style="width: 18rem;margin-top: 120px;">
            <img src="..." class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${products[index].name}</h5>
                <p class="card-text">${products[index].price}UAH</p>
                ${nav}
                ${but}
            </div>
        </div>
        `
    });

    /*
    let vas = ``;
    for(var x = 0;x < num;x++){
        var jora = JSON.parse(localStorage.getItem(`prodic${x}`));
        console.log(jora)
        let uyer = "<a href='#' class='btn btn-primary'>Купити</a>";
        let o = "<p class='card-text' style='color: green;'>В наявності</p>"; 
        if(jora[3] < 0 || jora[3] == 0){
            o = "<p class='card-text' style='color: red;'>Немає в наявності</p>";
            uyer =  "<a href='#' class='btn btn-primary'>Повідомити коли буде у наявності</a>";
        }
        vas += `
        <div class="card" id="car" style="width: 18rem; margin-top: 120px">
        <img src="${jora[1]}" class="card-img-top" alt="...">
        <div class="card-body">
        <h5 class="card-title">${jora[0]}</h5>
        <p class="card-text">${jora[2]}UAH</p>
        ${o}
        ${uyer}
        </div>
        </div>
        `
    }
    */
    body.innerHTML = products_html;
}

function up(){
    var body = document.getElementById("car")
    let num = JSON.parse(localStorage.getItem("num"));
    var jora = JSON.parse(localStorage.getItem(`prodic${num}`));
    let allka = ``;

}

function order(index){
    localStorage.setItem("temp_order", JSON.stringify(index))
    window.location = "order.html";
}

show()


function tp(){
    window.location = "./admin/index.html";
}
