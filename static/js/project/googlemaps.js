function initialize() {
	var onoff = $('#on_off p').html();
	
	if (onoff == 'True')
	{
		var position_width = $('#position_width p').html();
		var width = position_width;
		var position_height = $('#position_height p').html();
		var title = $('#title p').html();
		var city = $('#city p').html();
		var street = $('#street p').html();
        var zoom = Number($('#g_zoom p').html());
		position_width = Number(position_width) + 0.0007;
		position_height = Number(position_height);
		var map_canvas = document.getElementById('map_canvas');
		var map_options = {
			center: new google.maps.LatLng(position_width, position_height),
			zoom: zoom,
			mapTypeControlOptions: {
				mapTypeIds: ['map_style', google.maps.MapTypeId.SATELLITE,]
			}

							}
		var styles = [
			{
			  featureType: "road",
			  elementType: "labels",
			  stylers: [
				{ visibility: "on" }
			  ]
			}
		];
		
		var map = new google.maps.Map(map_canvas, map_options);
		var marker = new google.maps.Marker({map: map,position: new google.maps.LatLng(width,position_height)});
		var infowindow = new google.maps.InfoWindow({content:"<b>"+title+"</b><br/>"+street+"<br/>"+city });
		var styledMap = new google.maps.StyledMapType(styles,
			{name: "Styled Map"});

		map.mapTypes.set('map_style', styledMap);
		map.setMapTypeId('map_style');

		infowindow.open(map,marker);
		google.maps.event.addListener(marker, "click", function(){infowindow.open(map,marker);});
	}
}

function loadScript() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&' +
      'callback=initialize';
  document.body.appendChild(script);
}

window.onload = loadScript;
//~ google.maps.event.addDomListener(window, 'load', initialize);
