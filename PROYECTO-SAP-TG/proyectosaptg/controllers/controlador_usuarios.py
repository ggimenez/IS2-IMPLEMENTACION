# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
from repoze.what import predicates

from proyectosaptg.lib.base import BaseController
from proyectosaptg.model import DBSession, metadata
from proyectosaptg.controllers.error import ErrorController
from proyectosaptg import model
from proyectosaptg.controllers.secure import SecureController

from tg import tmpl_context
from proyectosaptg.widgets.add_usuario_form import create_add_user_form



from tg import validate


from proyectosaptg.model import *

from sprox.formbase import AddRecordForm
from tw.forms import TextField,CalendarDatePicker

from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller


from tgext.crud import CrudRestController
from proyectosaptg.model import DBSession, Usuario


from tw.core import WidgetsList
from tw.forms import TableForm, TextField, CalendarDatePicker, SingleSelectField, TextArea, PasswordField
from formencode.validators import Int, NotEmpty, DateConverter, DateValidator, Identity


from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller



#prueba con crudcontroller

class UsuarioForm(TableForm):
    # This WidgetsList is just a container
    class fields(WidgetsList):
        nombres = TextField(validator=NotEmpty)
	apellidos = TextField(validator=NotEmpty)
	username = TextField(validator=NotEmpty)
	password = PasswordField(validator=NotEmpty)
        #fecha_creacion = CalendarDatePicker(validator=DateConverter())
        
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

class UsuarioController(CrudRestController):
   
    model = Usuario
    table = usuario_table
    table_filler = usuario_table_filler
    new_form = usuario_add_form	
    edit_filler = usuario_edit_filler		
    edit_form = usuario_edit_form	



