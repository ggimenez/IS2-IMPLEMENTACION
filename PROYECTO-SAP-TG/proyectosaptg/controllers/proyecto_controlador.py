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



from repoze.what import predicates
from repoze.what.predicates import not_anonymous

"""configuraciones del modelo Proyecto"""
"""proyecto_form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))"""
class ProyectoRegistrationForm(AddRecordForm):
    __model__ = Proyecto
    __require_fields__ = ['cod_proyecto', 'nombre']
    __omit_fields__ = ['id_proyecto', 'estado','fecha_creacion' ,'fecha_inicio', 
                      'fecha_finalizacion_anulacion', 'fases','user']
    cod_proyecto           = TextField
    nombre                 = TextField
    usuario_creador = HiddenField
    __dropdown_field_names__ = {'tipo_items':'nombre'}
     

class ProyectoCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ = Proyecto
        __limit_fields__ = ['cod_proyecto', 'nombre','estado', 'fecha_creacion','fecha_inicio', 
                            'fecha_finalizacion_anulacion','usuario_creador']
        #__omit_fields__ = ['__actions__'] 
          
        
        
        __url__ = '../proyecto.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Proyecto
        __limit_fields__ = ['id_proyecto','cod_proyecto', 'nombre','estado', 'fecha_creacion', 
                            'fecha_inicio', 'fecha_finalizacion_anulacion','usuario_creador']
                            
        """def user_id(self, obj, **kw):
            user = DBSession.query(User).filter_by(user_id=obj.user_id).one()
            return user.user_name"""
        
        
        def __actions__(self, obj):
            """Override this function to define how action links should be displayed for the given record."""
            primary_fields = self.__provider__.get_primary_fields(self.__entity__)
            pklist = '/'.join(map(lambda x: str(getattr(obj, x)), primary_fields))
            
                       
            value =  '<div><div><a class="edit_link" href="'+pklist+'/edit" style="text-decoration:none">edit</a>'\
            '</div><div>'\
            '<form method="POST" action="'+pklist+'" class="button-to">'\
            '<input type="hidden" name="_method" value="DELETE" />'\
            '<input class="delete-button" onclick="return confirm(\'Are you sure?\');" value="delete" type="submit" '\
            'style="background-color: transparent; float:left; border:0; color: #286571; display: inline; margin: 0; padding: 0;"/>'\
            '</form>'\
            '<a class="fases_link" href="../fases/?pid='+pklist+'">Fases</a>'\
            '</div></div>'
            
            return value
        
        
    
    class defaultCrudRestController(CrudRestController):
        @with_trailing_slash
        @expose('proyectosaptg.templates.get_all')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            return CrudRestController.get_all(self, *args, **kw)
      
    
        @without_trailing_slash
        @expose('proyectosaptg.templates.new')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            
            #obtenemos el nombre del usuario creador del proyecto
            user = request.identity['repoze.who.userid'] 
           
            print "new de proyecto, esto es user:\n"
            print user
            
            kw["usuario_creador"]= user
            
            tmpl_context.widget = self.new_form
            
            retorno = dict(value=kw, model=self.model.__name__)
            
            return retorno
    
    #proyecto_table_filler = CamposTableFiller(DBSession)                        
    new_form_type = ProyectoRegistrationForm
