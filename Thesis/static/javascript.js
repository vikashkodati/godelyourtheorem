
function test(){
	Dajax.process();
}

function change_page(event){
	var pageClickedTarget = $(event.target);
	var pageClicked = pageClickedTarget.html();
	var currentPage = $('.selected').html();
	if (currentPage != pageClicked) {
		$('.selected').removeClass('selected');
		pageClickedTarget.addClass('selected');
		Dajaxice.Thesis.main.changePage(function(data){
			alert(data.message);
		},{'newPage':pageClicked});
	}
}

function send_form(){
	data = $('#my_form').serialize(true);
	Dajaxice.Thesis.main.send_form(test,{'form':data});
}

$(document).ready(function() {
  $(".nav-page-element").click(change_page);
});
