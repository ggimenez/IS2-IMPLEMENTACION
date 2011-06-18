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





"""configuraciones del modelo TipoItem"""
"""tipo_item_form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))"""


"""from sprox.widgets import PropertyMultipleSelectField
class MyPropertyMultipleSelectField(PropertyMultipleSelectField):
    def _my_update_params(self, d, nullable=False):
        
        print "MyPropertyMultipleSelectField,d:\n:"
        print d
        
        atributos = DBSession.query(Atributo).filter_by(id_atributo=d["filtrar_id"]).all()
        options = [(atributo.id_atributo, atributo.nombre)
                            for atributo in atributos]
        d['options']= options
        return d"""
    



class TipoItemRegistrationForm(AddRecordForm):
    __model__ = TipoItem
    __require_fields__ = ['nombre' ,'descripcion']
    __omit_fields__ = ['id_tipo_item','cod_tipo_item','acumulador']
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    nombre           = TextField
    cod_tipo_item           = TextField
    #descripcion                 = TextArea
    __dropdown_field_names__ = {'atributos':'nombre'}
    
   

class TipoItemCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  TipoItem
        __limit_fields__ = ['cod_tipo_item', 'nombre','descripcion','atributos']
        
        
        __url__ = '../tipoitem.json' #this just tidies up the URL a bit
       


    class table_filler_type(TableFiller):
        __entity__ = TipoItem
        __limit_fields__ = ['id_tipo_item','cod_tipo_item', 'nombre','descripcion','atributos']
        
        def atributos(self, obj, **kw):
            nombres_atributos = ""
            
            for a in obj.atributos:
                        nombres_atributos = nombres_atributos + ", " + a.nombre
            
            return nombres_atributos[1:]
    
    new_form_type = TipoItemRegistrationForm
        

    class defaultCrudRestController(CrudRestController):
        
        
            
        @without_trailing_slash
        @expose('proyectosaptg.templates.new')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            
            tmpl_context.widget = self.new_form
            
            retorno = dict(value=kw, model=self.model.__name__)
            
            return retorno    


        @expose()
        @registered_validate(error_handler=new)
        def post(self, *args, **kw):
            
            nombre_tipo_item = kw["nombre"].split(" ")
            
            cod = ""
            for palabra in nombre_tipo_item:
                cod = cod + palabra[0].upper()
            
            kw['cod_tipo_item'] = cod
            
            self.provider.create(self.model, params=kw)
            
            raise redirect("./")        
