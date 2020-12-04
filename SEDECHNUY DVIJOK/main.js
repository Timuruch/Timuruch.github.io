

var go = document.getElementById("life4")
go.style.display= "none"

var goh = document.getElementById("life")
var alik = 0;

function pru(){
	if(alik == 0){
		document.getElementById("life").innerHTML="Dead"
		goh.style.backgroundColor = "red"
	}
	setTimeout(function(){
		document.getElementById("life").innerHTML="D/C"
		goh.style.backgroundColor = "gray"
		alik++
	}, 2000)
}

var gosha = document.getElementById("life1")
var ali= 0;

function pru1(){
	if(ali == 0){
		gosha.style.backgroundColor = "red"
		document.getElementById("life1").innerHTML="Dead"
	}
	setTimeout(function(){
		document.getElementById("life1").innerHTML="D/C"
		gosha.style.backgroundColor = "gray"
		ali++
	}, 2000)
	
}

var gosh = document.getElementById("life2")
var ai = 0;

function pru2(){
	if(ai == 0){
		gosh.style.backgroundColor = "red"
		document.getElementById("life2").innerHTML="Dead"
	}
	setTimeout(function(){
		document.getElementById("life2").innerHTML="D/C"
		gosh.style.backgroundColor = "gray"
		ai++
	}, 2000)
}

var goha = document.getElementById("life3")
var al = 0;

function pru3(){
	if(al== 0){
		goha.style.backgroundColor = "red"
		document.getElementById("life3").innerHTML="Dead"
	}
	setTimeout(function(){
		document.getElementById("life3").innerHTML="D/C"
		goha.style.backgroundColor = "gray"
		al++
	}, 2000)
}

var gol = document.getElementById("life4")
var ad = 0;

function pru4(){
	if(ad== 0){
		gol.style.backgroundColor = "red"
		document.getElementById("life4").innerHTML="Dead"
	}
	setTimeout(function(){
		document.getElementById("life4").innerHTML="D/C"
		gol.style.backgroundColor = "gray"
		ad++
	}, 2000)
}
function test(){
	var hog = document.getElementById("name").value
	var hof = document.getElementById("gofo")
	hof.innerHTML=hog;
	go.style.display= "block"
}
