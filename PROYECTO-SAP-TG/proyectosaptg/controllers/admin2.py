from tgext.admin.config import AdminConfig, CrudRestControllerConfig
from sprox.formbase import AddRecordForm
from formencode import Schema
from formencode.validators import FieldsMatch
from tw.forms import *
from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller
from proyectosaptg.model import *
from tg import expose, flash, require, url, request, redirect
from tg.decorators import without_trailing_slash, with_trailing_slash
from tg.decorators import paginate
from tg import tmpl_context
from tgext.crud.controller import CrudRestController

"""configuraciones del modelo Relacion"""
class RelacionRegistrationForm(AddRecordForm):
    __model__ = Relacion
    __require_fields__ = ['cod_relacion', 'descripcion']
    __omit_fields__ = ['id_relacion', 'estado','items']
    cod_relacion           = TextField
    descripcion            = TextArea
    
class RelacionCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ = Relacion
        __limit_fields__ = ['cod_relacion', 'descripcion','estado', 'items']
        __url__ = '../relacion.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Relacion
        __limit_fields__ = ['id_relacion','cod_relacion', 'descripcion','estado', 'items']
        
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

    class defaultCrudRestController(CrudRestController):
        @with_trailing_slash
        @expose('proyectosaptg.templates.get_all')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            return CrudRestController.get_all(self, *args, **kw)
      
    new_form_type = RelacionRegistrationForm

      
    
"""configuraciones del modelo LineaBase"""
class LineaBaseRegistrationForm(AddRecordForm):
    __model__ = LineaBase
    __require_fields__ = ['cod_linea_base', 'descripcion', 'items']
    __omit_fields__ = ['id_linea_base', 'version', 'estado','peso_acumulado', 'fecha_creacion', 'id_fase_fk']
    cod_linea_base           = TextField
    descripcion              = TextArea

class LineaBaseCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  LineaBase
        __limit_fields__ = ['cod_linea_base', 'descripcion', 'items']
        __url__ = '../linea_base.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = LineaBase
        __limit_fields__ = ['id_linea_base','cod_linea_base','descripcion', 'items']
    
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
            '<a class="fases_link" href="../linea_base/?pid='+pklist+'">Linea Base</a>'\
            '</div></div>'
            
            return value

    class defaultCrudRestController(CrudRestController):
        @with_trailing_slash
        @expose('proyectosaptg.templates.get_all')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            return CrudRestController.get_all(self, *args, **kw)

    new_form_type = LineaBaseRegistrationForm

#instancimos todas nuestras configuraciones
class MyAdmin2Config(AdminConfig):
    relacion = RelacionCrudConfig
    lineabase = LineaBaseCrudConfig
