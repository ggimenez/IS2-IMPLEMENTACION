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
from tgext.crud.decorators import registered_validate, register_validators, catch_errors



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
                      'fecha_finalizacion_anulacion', 'fases','user']
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    cod_proyecto           = TextField
    nombre                 = TextField
    
    

class ProyectoCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ = Proyecto
        __limit_fields__ = ['cod_proyecto', 'nombre','estado', 'fecha_creacion','fecha_inicio', 
                            'fecha_finalizacion_anulacion']
        #__omit_fields__ = ['__actions__'] 
          
        
        
        __url__ = '../proyecto.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Proyecto
        __limit_fields__ = ['id_proyecto','cod_proyecto', 'nombre','estado', 'fecha_creacion', 
                            'fecha_inicio', 'fecha_finalizacion_anulacion']
                            
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
    #proyecto_id = HiddenField
    


class FaseCrudConfig(CrudRestControllerConfig):
  
    
    class table_type(TableBase):
        __entity__ =  Fase
        __limit_fields__ = ['cod_fase', 'nombre','estado', 'proyecto_id']
        __url__ = '../fases.json' #this just tidies up the URL a bit"""

    class table_filler_type(TableFiller):
        __entity__ = Fase
        __limit_fields__ = ['cod_fase', 'nombre','estado', 'proyecto_id']
        
        
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
            '<a class="itmes_link" href="../items/?fid='+pklist+'">Items</a>'\
            '</div></div>'
            
            return value
        
        
        
        
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
        @expose('proyectosaptg.templates.get_all_fase')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            
            #print "fase get_all"
            
            val = kw["pid"]
            
            #print kw
            #print args
            
            retorno =  CrudRestController.get_all(self, *args, **kw)
           
            retorno["pid"] = val 
            
            #print retorno
            
            return retorno
            
      
        @without_trailing_slash
        @expose('proyectosaptg.templates.new_fase')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            
          
            """print "new de fase:"
            print kw
            print args"""
            
            if len(args) > 0:
                #print "entre en el if\n"
                kw['proyecto_id'] = args[0]
                #print kw
                #print args
    
                
            
            tmpl_context.widget = self.new_form
            
            retorno = dict(value=kw, model=self.model.__name__)
            #print retorno
            return retorno
            
        
        
        @expose()
        @registered_validate(error_handler=new)
        def post(self, *args, **kw):
            
            """print "post:\n"
            print kw
            print args"""
            
            pid = kw["proyecto_id"]
            #print kw["proyecto_id"]
            
            self.provider.create(self.model, params=kw)
            
            path = '../?pid='+ str(pid)
            
            #print path
            
            raise redirect(path)
        
        @expose()
        def post_delete(self, *args, **kw):
            """This is the code that actually deletes the record"""
            
            
            fase_to_del = DBSession.query(Fase).filter_by(id_fase=args[0]).one()
            pid = fase_to_del.proyecto_id
            
            #print "fase a borrar:pid\n"
            #print fase_to_del.proyecto_id
            
            pks = self.provider.get_primary_fields(self.model)
            d = {}
            for i, arg in enumerate(args):
                d[pks[i]] = arg
            self.provider.delete(self.model, d)
            
            #print "post_delete:\n"
            
            #print kw
            #print args
            
            
            path = './' + '../' * (len(pks) - 1) + '?pid=' + str(pid)
            #print './' + '../' * (len(pks) - 1) + '?pid=' + str(pid)
            
            #redirect('./' + '../' * (len(pks) - 1))
            redirect(path)
        
        @expose('proyectosaptg.templates.get_delete_fase')
        def get_delete(self, *args, **kw):
            """This is the code that creates a confirm_delete page"""    
            return dict(args=args)    
        
        @expose('tgext.crud.templates.edit')
        def edit(self, *args, **kw):
            """Display a page to edit the record."""
            tmpl_context.widget = self.edit_form
            pks = self.provider.get_primary_fields(self.model)
            kw = {}
            for i, pk in  enumerate(pks):
                kw[pk] = args[i]
            value = self.edit_filler.get_value(kw)
            value['_method'] = 'PUT'
            
            return dict(value=value, model=self.model.__name__, pk_count=len(pks))
        
        
        @expose()
        @registered_validate(error_handler=edit)
        def put(self, *args, **kw):
            """update"""
            pks = self.provider.get_primary_fields(self.model)
            for i, pk in enumerate(pks):
                if pk not in kw and i < len(args):
                    kw[pk] = args[i]
            #print "update:\n"
            #print kw
            #print args
            
            pid = kw['proyecto_id']
            
            path = '../' * len(pks) + "?pid=" + str(pid)
            
            self.provider.update(self.model, params=kw)
            #redirect('../' * len(pks))
            redirect(path)    
        
    new_form_type = FaseRegistrationForm



"""configuraciones del modelo Item"""
class ItemRegistrationForm(AddRecordForm):
    __model__ = Item
    __require_fields__ = ['cod_item', 'nombre','id_fase_fk']
    __omit_fields__ = ['id_item','version','total_peso', 'estado', 'relaciones','id_linea_base_fk', 
                    'relacion','linea_base']
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    cod_item           = TextField
    nombre = TextField
    __dropdown_field_names__ = {'tipo_item':'nombre'}
    
    
    
class ItemCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  Item
        __limit_fields__ = ['cod_item', 'nombre','estado', 'version','peso','id_tipo_item_fk','id_linea_base_fk','relaciones']
        __url__ = '../item.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Item
        __limit_fields__ = ['cod_item', 'nombre','estado', 'version','peso','id_tipo_item_fk','id_linea_base_fk','relaciones']
    
     
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
            '<a class="valores_link" href="../valoress/?iid='+pklist+'">Atributos</a>'\
            '</div></div>'
            
            return value
    
        def _do_get_provider_count_and_objs(self, **kw):
            
            limit = kw.get('limit', None)
            offset = kw.get('offset', None)
            order_by = kw.get('order_by', None)
            desc = kw.get('desc', False)
            if len(kw) > 0:
                objs = DBSession.query(self.__entity__).filter_by(id_fase_fk=kw['fid']).all()
            else:
                objs = DBSession.query(self.__entity__).all()
                
            count = len(objs)
            self.__count__ = count
            return count, objs
        
    new_form_type = ItemRegistrationForm
    
    
    class defaultCrudRestController(CrudRestController):
        
        
        @with_trailing_slash
        @expose('proyectosaptg.templates.get_all_item')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            
            #print "fase get_all"
            
            val = kw["fid"]
            
            #print kw
            #print args
            
            retorno =  CrudRestController.get_all(self, *args, **kw)
           
            retorno["fid"] = val 
            
            #print retorno
            
            return retorno
            
        @without_trailing_slash
        @expose('proyectosaptg.templates.new_fase')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            print "new itme\n"
            
            
            if len(args) > 0:
                print "entre en el if\n"
                kw['id_fase_fk'] = args[0]
                print kw
                print args
    
                
            
            tmpl_context.widget = self.new_form
            
            retorno = dict(value=kw, model=self.model.__name__)
            
            return retorno
            
        
        
        @expose()
        @registered_validate(error_handler=new)
        def post(self, *args, **kw):
            
            print "post item:"
            print kw
            print args
            
            
            fid = kw["id_fase_fk"]
            #print kw["proyecto_id"]
            
            
            #kw['tipo_item']
            
            new_item = self.provider.create(self.model, params=kw)
            
            #generamos los campos para los valores de los atributos...
            atributos_new_item = new_item.tipo_item.atributos
            fk_item = new_item.id_item 
            for atributo in atributos_new_item:
                fk_atributo = atributo.id_atributo
                el_valor = {}
                el_valor['fk_atributo'] = fk_atributo
                el_valor['fk_item'] = fk_item
                el_valor['valor'] = "vacio"
                
                print el_valor
                self.provider.create(Valores, params=el_valor)
             
            path = '../?fid='+ str(fid)
            
            print path
            
            raise redirect(path)


        @expose()
        def post_delete(self, *args, **kw):
            """This is the code that actually deletes the record"""
            
            #obtenemos el id de la fase para hacer el filtrado despues de la redireccion
            item_to_del = DBSession.query(Item).filter_by(id_item=args[0]).one()
            fid = item_to_del.id_fase_fk
            
            
            pks = self.provider.get_primary_fields(self.model)
            d = {}
            for i, arg in enumerate(args):
                d[pks[i]] = arg
            self.provider.delete(self.model, d)
            
            path = './' + '../' * (len(pks) - 1) + '?fid=' + str(fid)
            
            redirect(path)

        @expose('tgext.crud.templates.edit')
        def edit(self, *args, **kw):
            """Display a page to edit the record."""
            tmpl_context.widget = self.edit_form
            pks = self.provider.get_primary_fields(self.model)
            kw = {}
            for i, pk in  enumerate(pks):
                kw[pk] = args[i]
            value = self.edit_filler.get_value(kw)
            value['_method'] = 'PUT'
            
            return dict(value=value, model=self.model.__name__, pk_count=len(pks))
        
        
        @expose()
        @registered_validate(error_handler=edit)
        def put(self, *args, **kw):
            """update"""
            pks = self.provider.get_primary_fields(self.model)
            for i, pk in enumerate(pks):
                if pk not in kw and i < len(args):
                    kw[pk] = args[i]
            
            
            fid = kw['id_fase_fk']
            path = '../' * len(pks) + "?fid=" + str(fid)
            
            self.provider.update(self.model, params=kw)
            redirect(path)
    
    
        
        


    




"""configuraciones del modelo Valores"""
class ValoresRegistrationForm(AddRecordForm):
    __model__ = Valores
    __require_fields__ = ['fk_atributo', 'fk_item','valor']
    __omit_fields__ = ['id_valor']
   
    #__field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    #__base_validator__     = user_form_validator
    #cod_item           = TextField
    #nombre = TextField
    #__dropdown_field_names__ = {'tipo_item':'nombre'}


class ValoresCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  Valores
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
        __url__ = '../valores.json' #this just tidies up the URL a bit
       


    class table_filler_type(TableFiller):
        __entity__ = Valores
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
            
        def fk_atributo(self, obj, **kw):
            atributo = DBSession.query(Atributo).filter_by(id_atributo=obj.fk_atributo).one()
            return atributo.nombre

        def fk_item(self, obj, **kw):
            item = DBSession.query(Item).filter_by(id_item=obj.fk_item).one()
            return item.nombre
       
    new_form_type = ValoresRegistrationForm





    
    

#instancimos todas nuestras configuraciones
class MyAdminConfig(AdminConfig):
      
    #DefaultControllerConfig    = MyCrudRestControllerConfig  
    
    user = UserCrudConfig
    proyecto = ProyectoCrudConfig
    tipoitem = TipoItemCrudConfig
    atributo = AtributoCrudConfig
    fase = FaseCrudConfig
    item = ItemCrudConfig
    valores = ValoresCrudConfig
   
    
   
    
   