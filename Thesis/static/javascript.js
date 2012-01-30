
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
			Dajax.process(data);
		},{'newPage':pageClicked});
	}
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

$(document).ready(function() {
  $(".nav-page-element").click(change_page);
});
