const endpoint = "http://127.0.0.1:8080/endpoints"

console.log("hello");

function set_embed_page(url) {
	document.getElementById("docset-page").src = url;
}

function populateSearchBar(docset_json) {
	console.log(docset_json);

	// Add to search bar
	document.getElementById("searchbar").getElementsByTagName("tbody")[0].innerHTML += "<tr>" +
		"<td scope=\"row\">" +
		"<button id=\"docset-\"" + docset_json["CFBundleIdentifier"] + "-parent\" class=\"docset-parent\">" +
		docset_json["CFBundleName"] + 
		"</button>" +
		"</td>" + 
		"</tr>";

	// Add onclick event
	/*
	document.getElementById("docset-" + docset_json["CFBundleIdentifier"] + "-parent").addEventListener("click", function(){ 
		set_embed_page(docset_json["docset_root"]);
	});
	*/
}

document.getElementById("docset-example-parent").addEventListener("click", function() {
	set_embed_page("https://example.com");
});


let xhttp = new XMLHttpRequest();
xhttp.open("GET", endpoint + "/get_plist.py");
xhttp.onload = function(){
	const json_response = JSON.parse(this.response);
	console.log(json_response);

	if(!json_response["success"]) {
		console.warn("Invalid json_response");
		return 1;
	}

	//populateSearchBar(json_response["docsets"][0]);
	json_response["docsets"].forEach(populateSearchBar);
}
xhttp.send();
