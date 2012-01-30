function test(){
	alert('fff');
	Dajax.process();
	alert('asf');
}

function send_form(){
	data = $('my_form').serialize(true);
	Dajaxice.Thesis.main.send_form(test,{'form':data});
}