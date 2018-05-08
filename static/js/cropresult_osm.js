window.onload=function(){
    alert("hey js is working");
    var x=13.08387245;
    var y=77.5743201838385;
    var mymap = L.map('mapid').setView([x,y], 14);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 20,
		id: 'mapbox.streets'
	}).addTo(mymap);
	L.marker([x,y]).addTo(mymap);

	console.log("test : "+htmlCropLand);
	var crop_land_details = htmlCropLand;
    console.log("Land details : "+crop_land_details.coordinates[0]);
    var len=crop_land_details.coordinates.length;
    console.log("Land details length : "+len);
    if(crop_land_details!=""){
        for(var i=0;i<len;i++)
        {
            L.polygon(crop_land_details.coordinates[i], {color: 'green'}).addTo(mymap);
        }
    }
    else{
	    console.log("Its NULL");
    }
}