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
