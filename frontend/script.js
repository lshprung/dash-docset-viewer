const endpoint = "http://127.0.0.1:8080/endpoints"

console.log("hello");

document.getElementById("docset-example-parent").onclick = function(){
	document.getElementById("docset-page").src = "https://example.com";
}

let xhttp = new XMLHttpRequest();
xhttp.open("GET", endpoint + "/get_plist.py");
xhttp.onload = function(){
	console.log(this.response);
}
xhttp.send();
