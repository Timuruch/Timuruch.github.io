

function show(){
    var body = document.getElementById("car")
    let num = JSON.parse(localStorage.getItem("num"));
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
    
    body.innerHTML = vas;
}

function up(){
    var body = document.getElementById("car")
    let num = JSON.parse(localStorage.getItem("num"));
    var jora = JSON.parse(localStorage.getItem(`prodic${num}`));
    let allka = ``;

}

show()


function tp(){
    window.location = "./admin/index.html";
}
