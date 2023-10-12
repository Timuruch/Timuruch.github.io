
function refresh(){
    displayMessage('message-warning', 'Admin', 'Сторінка перезапустится через 2 секунди', 2000);
    setTimeout(function (){
        location.reload();
    }, 2000);
    
}

function delete_all(){
    localStorage.removeItem("products");
    location.reload()
}

function deleted(index){
    let products = JSON.parse(localStorage.getItem("products"));
    products.splice(index, 1);
    localStorage.setItem("products", JSON.stringify(products))
    location.reload();
}

function closeEdit(){
    var cho = document.getElementById("hello")
    cho.innerHTML = "";
}

function saveEdit(index){
    let products = JSON.parse(localStorage.getItem("products"));
    const new_product ={
        name:  document.getElementById("name").value,
        image: document.getElementById("image").value,
        price: document.getElementById("price").value,
        count: document.getElementById("count").value,
    } 
    products[index] = new_product;
    localStorage.setItem("products", JSON.stringify(products))
    location.reload()
}

function showEdit(index){
    var cho = document.getElementById("hello")
    let products = JSON.parse(localStorage.getItem("products"));
    console.log(index)
    let tol = `
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Edit product</h5>
                <button type="button" class="btn-close" aria-label="Close" onclick="closeEdit()"></button>
            </div>
            <div class="modal-body">
            <label for="exampleInputEmail1" class="form-label">Name</label>
            <input type="text" id="name" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            
            <label for="exampleInputEmail1" class="form-label">Image</label>
            <input type="text" id="image" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">

            <label for="exampleInputEmail1" class="form-label">Price</label>
            <input type="number" id="price" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">

            <label for="exampleInputEmail1" class="form-label">Count</label>
            <input type="number" id="count" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">

            </div>
        
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary"onclick="closeEdit()" >Close</button>
                <button type="button" class="btn btn-primary" onclick="saveEdit(${index})">Save changes</button>
            </div>
            </div>
        </div>
    `
    cho.innerHTML = tol;
    document.getElementById("name").value = products[index].name;
    document.getElementById("image").value = products[index].image;
    document.getElementById("price").value = products[index].price;
    document.getElementById("count").value = products[index].count;

}


function up(){
    var body = document.getElementById("pok")
    let products = JSON.parse(localStorage.getItem("products"));
    let vas = ``;
    products.forEach(function(product, index){
        vas += `
        <tr>
        <td>${index + 1}</td>
        <td>${products[index].name}</td>
        <td>${products[index].price}</td>
        <td>${products[index].image}</td>
        <td>${products[index].count}</td>
        <td class="text-center"><button type="button" class="btn-close" aria-label="Close" onclick="deleted(${index})"></button></td>
        <td class="text-center"><button type="button" class="btn btn-warning" onclick="showEdit('${index}')">Edit</button></td>
        </tr>
        `
    })
        
    
    body.innerHTML = vas;
}

up()