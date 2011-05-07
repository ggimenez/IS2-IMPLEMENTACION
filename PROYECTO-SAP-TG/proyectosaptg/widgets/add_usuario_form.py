
from tw.api import WidgetsList
from tw.forms import (TableForm, CalendarDatePicker, Label,
    SingleSelectField, Spacer, TextField, PasswordField,TextArea)


class AddUsuarioForm(TableForm):

    fields = [
        TextField('nombres', label_text='Nombres'),
        TextField('apellidos', label_text='Apellidos'),
	TextField('username', label_text='Username'),
	PasswordField('password', label_text='Contrasenha')]
	    
    submit_text = 'Guardar Usuario'	       

create_add_user_form = AddUsuarioForm("create_add_user_form")


