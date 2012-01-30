function test(){
	Dajax.process();
}

function send_form(){
	data = $('#my_form').serialize(true);
	Dajaxice.Thesis.main.send_form(test,{'form':data});
}