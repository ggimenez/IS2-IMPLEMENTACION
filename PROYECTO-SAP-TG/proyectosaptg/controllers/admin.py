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

"""configuraciones del modelo User"""
user_form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))
class UserRegistrationForm(AddRecordForm):
    __model__ = User
    __require_fields__     = ['password', 'user_name', 'email_address']
    __omit_fields__        = ['_password', 'created', 'user_id', 'town_id','proyectos','display_name']
    __field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    __base_validator__     = user_form_validator
    email_address          = TextField
    nombres_apellidos      = TextField
    verify_password        = PasswordField('verify_password')

  


class UserCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ = User
        __limit_fields__ = ['user_name','nombres_apellidos', 'email_address','created','groups']
        __url__ = '../user.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = User
        __limit_fields__ = ['user_id', 'user_name','nombres_apellidos', 'email_address','created','groups']
   
    new_form_type = UserRegistrationForm






"""configuraciones del modelo Proyecto"""
"""proyecto_form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))"""
class ProyectoRegistrationForm(AddRecordForm):
    __model__ = Proyecto
    __require_fields__ = ['cod_proyecto', 'nombre']
    __omit_fields__ = ['id_proyecto', 'estado','fecha_creacion' ,'fecha_inicio', 
                      'fecha_finalizacion_anulacion', 'fases']
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    cod_proyecto           = TextField
    nombre                 = TextField
    
    

class ProyectoCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ = Proyecto
        __limit_fields__ = ['cod_proyecto', 'nombre','estado', 'fecha_creacion','fecha_inicio', 
                            'fecha_finalizacion_anulacion', 'user_id']
        #__omit_fields__ = ['__actions__'] 
          
        
        
        __url__ = '../proyecto.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Proyecto
        __limit_fields__ = ['id_proyecto','cod_proyecto', 'nombre','estado', 'fecha_creacion', 
                            'fecha_inicio', 'fecha_finalizacion_anulacion', 'user_id']
                            
        def user_id(self, obj, **kw):
            user = DBSession.query(User).filter_by(user_id=obj.user_id).one()
            return user.user_name
        
        
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
      
    
        
    
    #proyecto_table_filler = CamposTableFiller(DBSession)                        
    new_form_type = ProyectoRegistrationForm

      
    


"""configuraciones del modelo TipoItem"""
"""tipo_item_form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))"""
class TipoItemRegistrationForm(AddRecordForm):
    __model__ = TipoItem
    __require_fields__ = ['cod_tipo_item','nombre' ,'descripcion']
    __omit_fields__ = ['id_tipo_item']
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



"""configuraciones del modelo Atributo"""
"""atributo_form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))"""
class AtributoRegistrationForm(AddRecordForm):
    __model__ = Atributo
    __require_fields__ = ['cod_atributo', 'nombre','tipo_dato']
    __omit_fields__ = ['id_atributo',]
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    cod_atributo           = TextField
    nombre = TextField
    tipo_dato = TextField
    #descripcion                 = TextArea
    
    


class AtributoCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  Atributo
        __limit_fields__ = ['cod_atributo', 'nombre','descripcion', 'tipo_dato']
        __url__ = '../atributo.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Atributo
        __limit_fields__ = ['id_atributo','cod_atributo', 'nombre','descripcion', 'tipo_dato']
    new_form_type = AtributoRegistrationForm



"""configuraciones del modelo Fase"""
class FaseRegistrationForm(AddRecordForm):
  
    __model__ = Fase
    __require_fields__ = ['cod_fase', 'nombre']
    __omit_fields__ = ['id_fase','estado','lineas_bases']
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    #__hidden_fields__      = ['proyecto_id']
    cod_fase           = TextField
    nombre = TextField
    #descripcion                 = TextArea
    proyecto_id = HiddenField
    


class FaseCrudConfig(CrudRestControllerConfig):
  
    
    class table_type(TableBase):
        __entity__ =  Fase
        __limit_fields__ = ['cod_fase', 'nombre','estado', 'proyecto_id']
        __url__ = '../fases.json' #this just tidies up the URL a bit"""

    class table_filler_type(TableFiller):
        __entity__ = Fase
        __limit_fields__ = ['cod_fase', 'nombre','estado', 'proyecto_id']
        
        
        
        def proyecto_id(self, obj,**kw):
            #print obj.proyecto_id
            proyecto = DBSession.query(Proyecto).filter_by(id_proyecto=obj.proyecto_id).one()
            return proyecto.nombre
        
        def _do_get_provider_count_and_objs(self, **kw):
            
            limit = kw.get('limit', None)
            offset = kw.get('offset', None)
            order_by = kw.get('order_by', None)
            desc = kw.get('desc', False)
            if len(kw) > 0:
                objs = DBSession.query(self.__entity__).filter_by(proyecto_id=kw['pid']).all()
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
            
            
      
        @without_trailing_slash
        @expose('tgext.crud.templates.new')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            
          
            print kw
            
            kw['proyecto_id'] = 2
            print kw
            tmpl_context.widget = self.new_form
            return dict(value=kw, model=self.model.__name__)
        
        
        
    new_form_type = FaseRegistrationForm



"""configuraciones del modelo Item"""
class ItemRegistrationForm(AddRecordForm):
    __model__ = Item
    __require_fields__ = ['cod_item', 'nombre']
    __omit_fields__ = ['id_item','version','total_peso', 'estado', 'relaciones','id_fase_fk','id_linea_base_fk', 'relacion',
                        'fase','linea_base']
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    cod_item           = TextField
    nombre = TextField
    __dropdown_field_names__ = {'tipo_item':'nombre'}
    
    
    
class ItemCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  Item
        #__limit_fields__ = ['cod_fase', 'nombre','estado', 'items','lineas_bases']
        __url__ = '../item.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Item
        #__limit_fields__ = ['id_fase','cod_fase', 'nombre','estado', 'items','lineas_bases']
    new_form_type = ItemRegistrationForm






    
    

#instancimos todas nuestras configuraciones
class MyAdminConfig(AdminConfig):
      
    #DefaultControllerConfig    = MyCrudRestControllerConfig  
    
    
    user = UserCrudConfig
    proyecto = ProyectoCrudConfig
    tipoitem = TipoItemCrudConfig
    atributo = AtributoCrudConfig
    fase = FaseCrudConfig
    item = ItemCrudConfig
   
    
   
    
   