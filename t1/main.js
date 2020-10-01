function test(){
	console.log("It's started");
	alert("This is test");	
	confirm("Do you love or like JS");
	console.log("It's end.Sorry:(");
}
function stress_test(){
	var x=prompt("Pelase enter the number!!!");
	if (x == 10){
		alert("Wow you do this");
	} else {
		alert("Sorry.You don't win:(");
	}
}
stress_test()
var sec=confirm("Do you want to play a bit more?")
if (sec == true){
	stress_test()
}
var sec=confirm("Do you want to play a bit more?")
if (sec == true){
	stress_test()
}
var sec=confirm("Do you want to play a bit more?")
if (sec == true){
	stress_test()
}