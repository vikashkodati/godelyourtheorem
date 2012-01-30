function test(){
	Dajax.process();
}

function send_form(){
	data = $('#my_form').serialize(true);
	alert(data);
	Dajaxice.Thesis.main.send_form(test,{'form':data});
}