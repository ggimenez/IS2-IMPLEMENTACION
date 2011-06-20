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
from repoze.what.predicates import has_permission
from sprox.widgets import PropertySingleSelectField


class AtributoRegistrationForm(AddRecordForm):
    __model__ = Atributo
    __require_fields__ = ['cod_atributo', 'nombre','tipo_dato']
    __omit_fields__ = ['id_atributo']
    cod_atributo           = TextField
    nombre = TextField
    tipodatochoices = (("Cadena"),("Numerico"))
    tipo_dato = SingleSelectField

class AtributoCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  Atributo
        __limit_fields__ = ['cod_atributo', 'nombre','descripcion', 'tipo_dato']
        __url__ = '../atributo.json' #this just tidies up the URL a bit

    class table_filler_type(TableFiller):
        __entity__ = Atributo
        __limit_fields__ = ['id_atributo','cod_atributo', 'nombre','descripcion', 'tipo_dato']

        def __actions__(self, obj):
            """Override this function to define how action links should be displayed for the given record."""
            primary_fields = self.__provider__.get_primary_fields(self.__entity__)
            pklist = '/'.join(map(lambda x: str(getattr(obj, x)), primary_fields))

            value =  '<div>'
            if has_permission('editar_atributo'):
                value = value + '<div><a class="edit_link" href="'+pklist+'/edit" style="text-decoration:none">edit</a></div>'
            if has_permission('eliminar_atributo'):
                value = value + '<div><form method="POST" action="'+pklist+'" class="button-to"><input type="hidden" name="_method" value="DELETE" /><input class="delete-button" onclick="return confirm(\'Est&aacute; seguro que desea eliminar?\');" value="delete" type="submit" style="background-color: transparent; float:left; border:0; color: #286571; display: inline; margin: 0; padding: 0;"/></form></div>'
            value = value + '</div>'
            
            return value
    
    class defaultCrudRestController(CrudRestController):
        @with_trailing_slash
        @expose('proyectosaptg.templates.get_all_atributo')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            return CrudRestController.get_all(self, *args, **kw)

        @without_trailing_slash
        @expose('proyectosaptg.templates.new_atributo')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            tipos = ["Cadena","Numerico","Fecha"]
            tmpl_context.widget = self.new_form
            retorno = dict(value=kw, model=self.model.__name__, tipo_dato_options = tipos)

            return retorno

    new_form_type = AtributoRegistrationForm
