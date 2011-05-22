  from tgext.admin.config import AdminConfig, CrudRestControllerConfig
from sprox.formbase import AddRecordForm
from formencode import Schema
from formencode.validators import FieldsMatch
from tw.forms import *
from proyectosaptg.model.auth import *
from proyectosaptg.model.proyecto import * 
from proyectosaptg.model.tipo_item import * 

from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller
from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller
from proyectosaptg.model import DBSession




class UserCrudConfig(CrudRestControllerConfig):
    """configuraciones del Modelo Usuario"""    
    class UserRegistrationForm(AddRecordForm):
        form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))
      
        __model__ = User
        __require_fields__     = ['password', 'user_name', 'email_address']
        __omit_fields__        = ['_password', 'groups', 'created', 'user_id', 'town_id']
        __field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
        __base_validator__     = form_validator
        email_address          = TextField
        display_name           = TextField
        verify_password        = PasswordField('verify_password')
    
  
    class UserTableFormType(TableBase):
        __model__= User

    class UserTableFillerType(TableFiller):
        __model__ = User
  
    table_type = UserTableFormType
    table_filler_type = UserTableFillerType
    new_form_type = UserRegistrationForm








class PermissionCrudConfig(CrudRestControllerConfig):
    """configuraciones del Modelo Permission"""
    class PermissionTableFormType(TableBase):
        __model__= Permission

    class PermissionTableFillerType(TableFiller):
        __model__ = Permission
  
    table_type = PermissionTableFormType
    table_filler_type = PermissionTableFillerType



class GroupsCrudConfig(CrudRestControllerConfig):
    """configuraciones del Mdelo Groups"""
    class GroupsTableFormType(TableBase):
        __model__= Group

    class GroupsTableFillerType(TableFiller):
        __model__ = Group

    
    table_type = GroupsTableFormType
    table_filler_type = GroupsTableFillerType



class TipoItemCrudConfig(CrudRestControllerConfig):
    """configuraciones del Mdelo Groups"""
    class TipoItemTableFormType(TableBase):
        __model__= TipoItem

    class TipoItemTableFillerType(TableFiller):
        __model__ = TipoItem

    table_type = TipoItemTableFormType
    table_filler_type = TipoItemTableFillerType




class ProyectoCrudConfig(CrudRestControllerConfig):
    """configuraciones del Mdelo Proyecto"""
    
    class ProyectoRegistrationForm(AddRecordForm):
        form_validator =  Schema(chained_validators=(FieldsMatch('cod_proyecto',
                                                          'verify_password',
                                                          messages={'invalidNoMatch':
                                                          'cod_proyecto do not match'}),))
        __model__ = Proyecto
        __require_fields__     = ['cod_proyecto', 'nombre', 'cant_fases','user_id']
        __omit_fields__        = ['id_proyecto', 'estado', 'fecha_creacion', 'fecha_inicio', 'fecha_finalizacion_anulacion']
        __field_order__        = ['cod_proyecto', 'nombre', 'cant_fases','user_id']
        __base_validator__     = form_validator
        cod_proyecto           = TextField
        nombre                 = TextField
        cant_fases             = TextField

    
    class ProyectoTableFormType(TableBase):
        __model__= Proyecto

    class ProyectoTableFillerType(TableFiller):
        __model__ = Proyecto
  
    table_type = ProyectoTableFormType
    table_filler_type = ProyectoTableFillerType
    new_form_type = ProyectoRegistrationForm
    
    """class ProyectoTable(TableBase):
      __model__ = Proyecto
      

    class ProyectoTableFiller(TableFiller):
        __model__ = Proyecto
       
    class ProyectoAddForm(AddRecordForm):
        __model__ = Proyecto
        __omit_fields__ = ['id_proyecto', 'fecha_inicio','fecha_creacion','fecha_finalizacion_anulacion','estado']
        

    class ProyectoEditForm(EditableForm):
        __model__ = Proyecto
        __omit_fields__ = ['id_proyecto', 'fecha_inicio','fecha_creacion','fecha_finalizacion_anulacion','estado','cod_proyecto', 'usuario']
        

    class ProyectoEditFiller(EditFormFiller):
        __model__ = Proyecto
       
    
    proyecto_table = ProyectoTable(DBSession)
    proyecto_table_filler = ProyectoTableFiller(DBSession)
    proyecto_add_form = ProyectoAddForm(DBSession)
    proyecto_edit_form = ProyectoEditForm(DBSession)
    proyecto_edit_filler = ProyectoEditFiller(DBSession)"""

class MyAdminConfig(AdminConfig):
    """instanciamos todas nuestras configuraciones"""
    user = UserCrudConfig
    permission = PermissionCrudConfig
    group = GroupsCrudConfig
    proyectos = ProyectoCrudConfig
    tipoItem = TipoItemCrudConfig
