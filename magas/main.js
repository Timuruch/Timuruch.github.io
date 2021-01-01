const money_first = 1399;
var sale_first = 1;
const name_first = "Клавіатура дротова Logitech G209 Prodigy USB";
const vid_first = 209;
const photo_first = "logitech.jpg";
var bals = 0;

const money_second = 1286;
var sale_second = 0;
const name_second = "Клавіатура Cougar Vantar";
const vid_second = 6;
const photo_sec = "voutar.jpg";
var balssec = 0;

if(money_first > money_second){
	balssec = money_first - money_second;
}else if(money_first < money_second){
	bals = money_second - money_first;
}

var po = vid_first / 0.5;
bals = bals + po;

var po2 = vid_second / 0.5;
balssec = balssec + po2;

if(sale_first == 1){
	bals + 100;
}else if(sale_second == 1){
	balssec + 100;
}

var tovarc = document.getElementById("tovar");
tovar.innerHTML = `
<p id="action">Акція</p>
<img id="image" src=${photo_first}>
<p id="na">${name_first}</p>
<a id="vidhuk" href="">${vid_first} відгуків</a>
<p id="cianspec">${money_first}₴</p>
<p>${bals} балів</p>
`;


var tova = document.getElementById("tova");
tova.innerHTML = `
<img id="image" src=${photo_sec}>
<p id="na">${name_second}</p>
<a id="vidhuk" href="">${vid_second} відгуків</a>
<p id="cian">${money_second}₴</p>
<p>${balssec} балів</p>
`;

  