
function test(){
	Dajax.process();
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
	$(".nav-page-element").click(change_page);

	var defaultBounds = new google.maps.LatLngBounds(
	  new google.maps.LatLng(-33.8902, 151.1759),
	  new google.maps.LatLng(-33.8474, 151.2631));

	var input = document.getElementById('id_location');
	var options = {
	  bounds: defaultBounds,
	  types: ['geocode']
	};

	autocomplete = new google.maps.places.Autocomplete(input, options);
});
