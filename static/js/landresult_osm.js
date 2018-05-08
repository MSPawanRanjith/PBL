window.onload=function(){
    //alert("hey js is working");
    var x=13.08387245;
    var y=77.5743201838385;
    var mymap = L.map('mapid').setView([x,y], 14);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);
	L.marker([x,y]).addTo(mymap);

	console.log("test : "+htmlLand);
	var land_details = htmlLand;
    console.log(land_details);

	if(land_details!=""){
	    L.polygon(land_details.coordinates,{color:'blue'}).addTo(mymap);
    }
	else{
	    console.log("Its NULL");
    }
}