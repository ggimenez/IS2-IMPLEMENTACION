# -*- coding: utf-8 -*-

"""
from tg import validate


from proyectosaptg.model import *

from sprox.formbase import AddRecordForm
from tw.forms import TextField,CalendarDatePicker

from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller


from tgext.crud import CrudRestController
from proyectosaptg.model import DBSession, Proyecto


from tw.core import WidgetsList
from tw.forms import TableForm, TextField, CalendarDatePicker, SingleSelectField, TextArea, PasswordField
from formencode.validators import Int, NotEmpty, DateConverter, DateValidator, Identity


from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller



#prueba con crudcontroller

class ProyectoForm(TableForm):
    # This WidgetsList is just a container
    class fields(WidgetsList):
		cod_proyecto = TextField(validator=NotEmpty)
		nombre = TextField(validator=NotEmpty)
		#estado = TextField(validator=NotEmpty)
		#user_id =TextField(validator=NotEmpty) 
		#fecha_creacion = CalendarDatePicker(validator=DateConverter())
        
#then, we create an instance of this form
proyecto_add_form = ProyectoForm("create_proyecto_form")


class ProyectoEditForm(EditableForm):
    __model__ = Proyecto
    __omit_fields__ = ['id_proyecto', 'fecha_creacion','fecha_inicio', 'fecha_finalizacion_anulacion', 'cant_fases','estado']
proyecto_edit_form = ProyectoEditForm(DBSession)

class ProyectoEditFiller(EditFormFiller):
    __model__ = proyecto
proyecto_edit_filler = ProyectoEditFiller(DBSession)

class ProyectoTable(TableBase):
    __model__ = proyecto
    __omit_fields__ = ['id_proyecto']
proyecto_table = ProyectoTable(DBSession)


class ProyectoTableFiller(TableFiller):
    __model__ = Proyecto
proyecto_table_filler = ProyectoTableFiller(DBSession)


class ProyectoController(CrudRestController):
   
    model = Proyecto
    table = proyecto_table
    table_filler = proyecto_table_filler
    new_form = proyecto_add_form	
    edit_filler = proyecto_edit_filler		
    edit_form = proyecto_edit_form"""


from tgext.crud import CrudRestController
from proyectosaptg.model import DBSession, Proyecto
from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller

from sprox.formbase import AddRecordForm
from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller


from tg import expose, flash, require, url, request, redirect
from tg.decorators import without_trailing_slash, with_trailing_slash
from tg.decorators import paginate



class ProyectoTable(TableBase):
    __model__ = Proyecto
proyecto_table = ProyectoTable(DBSession)


class ProyectoTableFiller(TableFiller):
    __model__ = Proyecto
proyecto_table_filler = ProyectoTableFiller(DBSession)

class ProyectoAddForm(AddRecordForm):
    __model__ = Proyecto
    __omit_fields__ = ['id_proyecto', 'fecha_inicio','fecha_creacion','fecha_finalizacion_anulacion','estado']
proyecto_add_form = ProyectoAddForm(DBSession)

class ProyectoEditForm(EditableForm):
    __model__ = Proyecto
    __omit_fields__ = ['id_proyecto', 'fecha_inicio','fecha_creacion','fecha_finalizacion_anulacion','estado','cod_proyecto', 'usuario']
proyecto_edit_form = ProyectoEditForm(DBSession)

class ProyectoEditFiller(EditFormFiller):
    __model__ = Proyecto
proyecto_edit_filler = ProyectoEditFiller(DBSession)



class ProyectoController(CrudRestController):
    model = Proyecto
    table = proyecto_table
    table_filler = proyecto_table_filler
    new_form = proyecto_add_form
    edit_form = proyecto_edit_form
    edit_filler = proyecto_edit_filler
    
  
    #@expose('proyectosaptg.templates.get_all')
    @with_trailing_slash
    @expose('proyectosaptg.templates.get_all')
    @expose('json')
    @paginate('value_list', items_per_page=7)
    def get_all(self, *args, **kw):
        print "get all redefinido..:me llamaron..\n"
        return super(ProyectoController, self).get_all(*args,**kw)
        
