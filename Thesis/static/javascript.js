function send_form(){
	alert('all good');
	data = $('my_form').serialize(true);
	alert('all good');
	Dajaxice.main.send_form(Dajax.process,{'form':data});
}