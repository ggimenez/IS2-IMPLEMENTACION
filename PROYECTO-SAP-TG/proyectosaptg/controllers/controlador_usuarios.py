# -*- coding: utf-8 -*-
"""Main Controller"""

from sprox.formbase import AddRecordForm
from tw.forms import TextField,CalendarDatePicker

from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller


from tgext.crud import CrudRestController
from proyectosaptg.model import DBSession, Usuario


from tw.core import WidgetsList
from tw.forms import TableForm, TextField, CalendarDatePicker, SingleSelectField, TextArea, PasswordField
from formencode.validators import Int, NotEmpty, DateConverter, DateValidator
from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller

from tw.forms.validators import Schema, Int, NotEmpty, UnicodeString, \
                                FieldsMatch, Email, URL      
from formencode.schema import SimpleFormValidator


#prueba con crudrestcontroller
from tw.api import CSSLink
from tw.forms.validators import Schema, Int, NotEmpty, UnicodeString, \
                                FieldsMatch, Email, URL
from tg import config, url                                


from proyectosaptg.widgets.validators import  UniqueUserName

class UsuarioForm(TableForm):
    #css = [CSSLink(link=url('/theme/%s/_css/user.css' % config['theme']))]
    """validator = Schema(
        chained_validators=[
            UniqueUserName(),
            ]
        )"""
  
    # This WidgetsList is just a container
    class fields(WidgetsList):
        nombres = TextField(validator=NotEmpty)
	apellidos = TextField(validator=NotEmpty)
	username = TextField(validator=NotEmpty)
	password = PasswordField(validator=NotEmpty)
        #fecha_creacion = CalendarDatePicker(validator=DateConverter())
        submit_tex = "Crear Usuario"
#then, we create an instance of this form
usuario_add_form = UsuarioForm("create_usuario_form")


class UsuarioEditForm(EditableForm):
    __model__ = Usuario
    __omit_fields__ = ['id_usuario', 'username','fecha_creacion']
usuario_edit_form = UsuarioEditForm(DBSession)

class UsuarioEditFiller(EditFormFiller):
    __model__ = Usuario
usuario_edit_filler = UsuarioEditFiller(DBSession)

class UsuarioTable(TableBase):
    __model__ = Usuario
    __omit_fields__ = ['id_usuario']
usuario_table = UsuarioTable(DBSession)


class UsuarioTableFiller(TableFiller):
    __model__ = Usuario
usuario_table_filler = UsuarioTableFiller(DBSession)


from datetime import datetime
from tg.controllers import RestController, redirect
from tg.decorators import expose, validate
from proyectosaptg.model import DBSession, Usuario
from formencode.validators import DateConverter, Int, NotEmpty

from formencode.schema import SimpleFormValidator


class UsuarioRootController(CrudRestController):
   
    model = Usuario
    table = usuario_table
    table_filler = usuario_table_filler
    new_form = usuario_add_form	
    edit_filler = usuario_edit_filler		
    edit_form = usuario_edit_form

    
     
    
 
  
    
