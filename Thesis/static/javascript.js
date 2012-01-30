function initialize(id) {
        var mapOptions = {
		  center: new google.maps.LatLng(-33.8688, 151.2195),
		  zoom: 13,
		  mapTypeId: google.maps.MapTypeId.ROADMAP
		};
	var map = new google.maps.Map(document.getElementById('map_canvas'),
	  mapOptions);

	var defaultBounds = new google.maps.LatLngBounds(
	  new google.maps.LatLng(-33.8902, 151.1759),
	  new google.maps.LatLng(-33.8474, 151.2631));

	var input = document.getElementById(id);
	var options = {
	  bounds: defaultBounds,
	  types: ['geocode']
	};
	var autocomplete = new google.maps.places.Autocomplete(input, options);
	
	autocomplete.bindTo('bounds', map);

	var infowindow = new google.maps.InfoWindow();
	var marker = new google.maps.Marker({
	  map: map
	});
	
	google.maps.event.addListener(autocomplete, 'place_changed', function() {
	  infowindow.close();
	  var place = autocomplete.getPlace();
	  if (place.geometry.viewport) {
	    map.fitBounds(place.geometry.viewport);
	  } else {
	    map.setCenter(place.geometry.location);
	    map.setZoom(17);  // Why 17? Because it looks good.
	  }

	  var image = new google.maps.MarkerImage(
	      place.icon,
	      new google.maps.Size(71, 71),
	      new google.maps.Point(0, 0),
	      new google.maps.Point(17, 34),
	      new google.maps.Size(35, 35));
	  marker.setIcon(image);
	  marker.setPosition(place.geometry.location);
	  
	  var address = '';
	  if (place.address_components) {
	    address = [(place.address_components[0] &&
	                place.address_components[0].short_name || ''),
	               (place.address_components[2] &&
	                place.address_components[2].short_name || '')
	              ].join(' ');
	  }

	  infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
	  infowindow.open(map, marker);
	
	});
}

$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

function send_form(){
	data = $('#my_form').serializeObject();
	Dajaxice.Thesis.main.send_form(test,{'form':data});
}

var initiate_play_search = function(){
	var defaultBounds = new google.maps.LatLngBounds(
	  new google.maps.LatLng(-33.8902, 151.1759),
	  new google.maps.LatLng(-33.8474, 151.2631));

	var input = document.getElementById('search-input');
	var options = {
	  bounds: defaultBounds,
	  types: ['geocode']
	};

	autocomplete = new google.maps.places.Autocomplete(input, options);
	
	
	var new_location_set = function() {
	  /*infowindow.close();
	  var place = autocomplete.getPlace();
	  if (place.geometry.viewport) {
	    map.fitBounds(place.geometry.viewport);
	  } else {
	    map.setCenter(place.geometry.location);
	    map.setZoom(17);  // Why 17? Because it looks good.
	  }

	  var image = new google.maps.MarkerImage(
	      place.icon,
	      new google.maps.Size(71, 71),
	      new google.maps.Point(0, 0),
	      new google.maps.Point(17, 34),
	      new google.maps.Size(35, 35));
	  marker.setIcon(image);
	  marker.setPosition(place.geometry.location);
	*/
	var place = autocomplete.getPlace();
	  var address = '';
	  if (place.address_components) {
	    address = [(place.address_components[0] &&
	                place.address_components[0].long_name || ''),
	               (place.address_components[2] &&
	                place.address_components[2].long_name || '')
	              ].join(' ');
	  }

	 /* infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
	  infowindow.open(map, marker);*/
	
	  var populate_map = function(locations) {
		alert(locations);
	    var infowindow = new google.maps.InfoWindow();

	    var marker, i;

	    for (i = 0; i < locations.length; i++) {  
	      marker = new google.maps.Marker({
	        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
	        map: map
	      });

	      google.maps.event.addListener(marker, 'click', (function(marker, i) {
	        return function() {
	          infowindow.setContent(locations[i][0]);
	          infowindow.open(map, marker);
	        }
	      })(marker, i));
	    }
	};
	
	Dajaxice.Thesis.main.find_locations(populate_map,{'location':$("#search-input").val()});
};
	google.maps.event.addListener(autocomplete, 'place_changed', new_location_set);
	$("#search-button").click(new_location_set);
}

function change_page(event){
	var pageClickedTarget = $(event.target);
	var pageClicked = pageClickedTarget.html();
	var currentPage = $('.selected').html();
	if (currentPage != pageClicked) {
		$('.selected').removeClass('selected');
		pageClickedTarget.addClass('selected');
		Dajaxice.Thesis.main.changePage(function(data){
			Dajax.process(data);
			if (pageClicked == "Play"){
				initiate_play_search();
			}
		},{'newPage':pageClicked});
	}
}

$(document).ready(function() {
	if($(".nav-page-element")){
		$(".nav-page-element").click(change_page);
	}
	
	if ($(".registrationForm #my_form")) {
		var inputs = $(".form > * > input");
		var labels = $(".form > * > label");
		for (i=0; i< inputs.length; i++){
			if (labels[i]){
				$(inputs[i]).attr("placeholder",$(labels[i]).html().replace(":", "..."));
				$(labels[i]).remove();
			}
		}
		$(labels[inputs.length]).remove();
	}
	
	
	if (document.getElementById('id_location')){
		 initialize('id_location');
	}
});
