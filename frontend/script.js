const endpoint = "http://127.0.0.1:8080/endpoints"


function set_embed_page(url) {
	document.getElementById("docset-page").src = url;
}

function populateSearchBar(docset_json) {
	// Add to docset-table
	document.getElementById("docset-table").getElementsByTagName("tbody")[0].innerHTML += "<tr>" +
		"<td scope=\"row\">" +
		"<button id=\"docset-" + docset_json["CFBundleIdentifier"] + "-parent\" class=\"docset-parent\" onclick=\"set_embed_page('" + docset_json["docset_index"] + "')\">" +
		"<img class=\"docset-icon\" src=\"" + docset_json["icon.png"] + "\"/>" + 
		docset_json["CFBundleName"] + 
		"</button>" +
		"</td>" + 
		"</tr>";
}


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
	delete json_response
}
xhttp.send();
