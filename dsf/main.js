var gizmo45 = {name: "Oleg", age: 24}
var orizel4ik = {name: "Vasul", age: 11}
function test(){
	var login = document.getElementById('log').value
	var password = document.getElementById('pas').value
	if (login == "gizmo45" && password == 12345){
		console.log(gizmo45)
		document.getElementById("names").innerHTML = "Name:oleg Age:24"
	}else if (login == "orizel4ik", password == 12345){
		console.log(orizel4ik)
		document.getElementById("names").innerHTML = "Name:Vasul Age:11"
	}else{
		console.log("no way")
	}
}