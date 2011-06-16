# -*- coding: utf-8 -*-

from tgext.admin.config import AdminConfig, CrudRestControllerConfig
from sprox.formbase import AddRecordForm, EditableForm
from formencode import Schema
from formencode.validators import FieldsMatch
from tw.forms import *


from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller
from sprox.fillerbase import EditFormFiller



from proyectosaptg.model import *

from tg import expose, flash, require, url, request, redirect
from tg.decorators import without_trailing_slash, with_trailing_slash
from tg.decorators import paginate
from tgext.crud.decorators import registered_validate, register_validators, catch_errors



from tg import tmpl_context

from tgext.crud.controller import CrudRestController


from sprox.widgets import PropertyMultipleSelectField



"""configuraciones del modelo Atributo"""
"""atributo_form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))"""


from sprox.widgets import PropertySingleSelectField
class AtributoRegistrationForm(AddRecordForm):
    __model__ = Atributo
    __require_fields__ = ['cod_atributo', 'nombre','tipo_dato']
    __omit_fields__ = ['id_atributo']
    cod_atributo           = TextField
    nombre = TextField
    tipodatochoices = (("Cadena"),("Numerico"))
    
    
    tipo_dato = SingleSelectField
    #descripcion                 = TextArea
    
    


class AtributoCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  Atributo
        __limit_fields__ = ['cod_atributo', 'nombre','descripcion', 'tipo_dato']
        __url__ = '../atributo.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Atributo
        __limit_fields__ = ['id_atributo','cod_atributo', 'nombre','descripcion', 'tipo_dato']
        
    
    
    class defaultCrudRestController(CrudRestController):
        
        
            
        @without_trailing_slash
        @expose('proyectosaptg.templates.new_atributo')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            
            
            tipos = ["Cadena","Numerico","Fecha"]
            
            tmpl_context.widget = self.new_form
            
            retorno = dict(value=kw, model=self.model.__name__, tipo_dato_options = tipos)
            
            return retorno
    
            
    new_form_type = AtributoRegistrationForm
