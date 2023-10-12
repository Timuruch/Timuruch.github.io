let admin = JSON.parse( localStorage.getItem("admin"));
if(admin == false || admin == null){
    window.location = "index.html";
}

function deleted (index){
    let products = JSON.parse(localStorage.getItem("orders"));
    products.splice(index, 1);
    localStorage.setItem("orders", JSON.stringify(products))
    location.reload();
}


function tp(){
    window.location = "../index.html";
    localStorage.setItem("admin", false);
}

function show_people(){
    var tbody = document.getElementById("tbody");
    let orders = JSON.parse(localStorage.getItem("orders"));
    let vas = ``;
    orders.forEach(function(product, index){
        vas += `
        <tr>
        <td>${index + 1}</td>
        <td>${orders[index].name}</td>
        <td>${orders[index].street}</td>
        <td>${orders[index].price}</td>
        <td>${orders[index].count}</td>
        <td>${orders[index].phone}</td>
        <td class="text-center"><button type="button" class="btn-close" aria-label="Close" onclick="deleted(${index})"></button></td>
        </tr>
        `
    })
        
    
    tbody.innerHTML = vas;
}

show_people()