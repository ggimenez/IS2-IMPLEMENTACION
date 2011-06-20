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
from sprox.widgets import PropertySingleSelectField
from repoze.what.predicates import has_permission

class MyPropertySingleSelectField(PropertySingleSelectField):
    def _my_update_params(self, d, nullable=False):
        lista_ids = d['options']
        items = []
        for iid in lista_ids:
            items.append(DBSession.query(Item).filter_by(id_item = iid).one())    

        options = [(item.id_item, item.nombre) for item in items]
        d['options']= options

        return d

"""configuraciones del modelo Relacion"""
class RelacionRegistrationForm(AddRecordForm):
    __model__ = Relacion
    __require_fields__ = ['cod_relacion', 'descripcion']
    __omit_fields__ = ['id_relacion', 'estado']
    cod_relacion           = TextField
    descripcion            = TextArea
    item_origen_fk         = HiddenField
    item_destino_fk =  MyPropertySingleSelectField
    __dropdown_field_names__ = {'item_destino_fk':'nombre'}
    
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

            value = '<div>'
            if has_permission('editar_relacion'):
                value = value + '<div><a class="edit_link" href="'+pklist+'/edit" style="text-decoration:none">edit</a></div>'
            if has_permission('eliminar_relacion'):
                value = value + '<div><form method="POST" action="'+pklist+'" class="button-to"><input type="hidden" name="_method" value="DELETE" /><input class="delete-button" onclick="return confirm(\'Esta seguro que desea eliminar?\');" value="delete" type="submit" style="background-color: transparent; float:left; border:0; color: #286571; display: inline; margin: 0; padding: 0;"/></form></div>'
            value = value + '<div><a class="fases_link" href="../relaciones/?pid='+pklist+'">Relacion</a></div></div>'
            
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

    new_form_type = RelacionRegistrationForm

    class defaultCrudRestController(CrudRestController):
        @with_trailing_slash
        @expose('proyectosaptg.templates.get_all_relacion')
        @expose('json')
        @paginate('value_list', items_per_page=7)
        def get_all(self, *args, **kw):
            retorno = CrudRestController.get_all(self, *args, **kw)
            if kw.has_key("iid"):
                retorno["iido"] = kw["iid"]

            return retorno
            
        @without_trailing_slash
        @expose('proyectosaptg.templates.new_relacion')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            tmpl_context.widget = self.new_form
            #setemos el id origen de la relacion..
            kw["item_origen_fk"] = args[0]    
            #traemos todos los posibles Items destino de la relacion
            #1-->traemos todos los items de la fase del Item origen..
            fase_item_origen_fk = DBSession.query(Item).filter_by(id_item = kw["item_origen_fk"]).one().id_fase_fk
            items_fase_origen_list = DBSession.query(Item.id_item).filter(Item.id_fase_fk
                                   == fase_item_origen_fk).filter(Item.id_item != kw["item_origen_fk"]).all()
            items_fase_origen = []
            for elemento in items_fase_origen_list:
                items_fase_origen.append(elemento[0])

            fase_item_origen = DBSession.query(Fase).filter_by(id_fase = fase_item_origen_fk).one()

            proyecto_id = fase_item_origen.proyecto_id
            orden_item_origen = fase_item_origen.orden

            #2-->traemos todos los items de la fase siguiente, si la fase del item origen no es la ultima
            items_fase_siguiente = []
            if fase_item_origen.bool_ultimo == 0:
                fase_siguiente = DBSession.query(Fase).filter_by(proyecto_id = proyecto_id,
                                orden = (orden_item_origen + 1)).all()
                print "la fase sgte"
                print fase_siguiente
                if len(fase_siguiente) > 0:
                    items_fase_siguiente_list = DBSession.query(Item.id_item).filter_by(id_fase_fk = fase_siguiente[0].id_fase).all()
                    items_fase_siguiente = []
                    for elemento in items_fase_siguiente_list:
                        items_fase_siguiente.append(elemento[0])

            items_a_mostrar = items_fase_origen + items_fase_siguiente

            return dict(value=kw, model=self.model.__name__,item_destino_fk_options = items_a_mostrar)        
