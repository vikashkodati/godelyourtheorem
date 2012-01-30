function send_form(){
	data = $('my_form').serialize(true);
	Dajaxice.main.send_form(Dajax.process,{'form':data});
}