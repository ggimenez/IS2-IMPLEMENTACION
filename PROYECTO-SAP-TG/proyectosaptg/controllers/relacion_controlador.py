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


"""configuraciones del modelo Relacion"""
class RelacionRegistrationForm(AddRecordForm):
    __model__ = Relacion
    __require_fields__ = ['cod_relacion', 'descripcion']
    __omit_fields__ = ['id_relacion', 'estado']
    cod_relacion           = TextField
    descripcion            = TextArea
    
class RelacionCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ = Relacion
        __limit_fields__ = ['cod_relacion', 'descripcion','estado',]
        __url__ = '../relacion.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Relacion
        __limit_fields__ = ['id_relacion','cod_relacion', 'descripcion','estado']
        
        def __actions__(self, obj):
            """Override this function to define how action links should be displayed for the given record."""
            primary_fields = self.__provider__.get_primary_fields(self.__entity__)
            pklist = '/'.join(map(lambda x: str(getattr(obj, x)), primary_fields))

            value =  '<div><div><a class="edit_link" href="'+pklist+'/edit" style="text-decoration:none">edit</a>'\
            '</div><div>'\
            '<form method="POST" action="'+pklist+'" class="button-to">'\
            '<input type="hidden" name="_method" value="DELETE" />'\
            '<input class="delete-button" onclick="return confirm(\'Esta seguro que desea eliminar?\');" value="delete" type="submit" '\
            'style="background-color: transparent; float:left; border:0; color: #286571; display: inline; margin: 0; padding: 0;"/>'\
            '</form>'\
            '<a class="fases_link" href="../relaciones/?pid='+pklist+'">Relacion</a>'\
            '</div></div>'
            
            return value
            
            
        def _do_get_provider_count_and_objs(self, **kw):
            
            limit = kw.get('limit', None)
            offset = kw.get('offset', None)
            order_by = kw.get('order_by', None)
            desc = kw.get('desc', False)
            if len(kw) > 0:
                objs = DBSession.query(self.__entity__).filter_by(item_origen_fk=kw['iid']).all()
            else:
                objs = DBSession.query(self.__entity__).all()
                
            count = len(objs)
            self.__count__ = count
            return count, objs    
            

    class defaultCrudRestController(CrudRestController):
        @with_trailing_slash
        @expose('proyectosaptg.templates.get_all')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            return CrudRestController.get_all(self, *args, **kw)
      
    new_form_type = RelacionRegistrationForm
