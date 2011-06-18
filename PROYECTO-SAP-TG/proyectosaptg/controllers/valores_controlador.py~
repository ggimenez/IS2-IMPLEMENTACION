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



"""configuraciones del modelo ValoresCadena"""
class ValoresCadenaRegistrationForm(AddRecordForm):
    __model__ = ValoresCadena
    __require_fields__ = ['fk_atributo', 'fk_item','valor']
    __omit_fields__ = ['id_valor']
  
class ValoresCadenaCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  ValoresCadena
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
        __url__ = '../valorescadenas.json' #this just tidies up the URL a bit
       
    class table_filler_type(TableFiller):
        __entity__ = ValoresCadena
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
            
        def fk_atributo(self, obj, **kw):
            atributo = DBSession.query(Atributo).filter_by(id_atributo=obj.fk_atributo).one()
            return atributo.nombre

        def fk_item(self, obj, **kw):
            item = DBSession.query(Item).filter_by(id_item=obj.fk_item).one()
            return item.nombre
    
        def _do_get_provider_count_and_objs(self, **kw):
            
            limit = kw.get('limit', None)
            offset = kw.get('offset', None)
            order_by = kw.get('order_by', None)
            desc = kw.get('desc', False)
            if len(kw) > 0:
                objs = DBSession.query(self.__entity__).filter_by(fk_item=kw['iid']).all()
            else:
                objs = DBSession.query(self.__entity__).all()
                
            count = len(objs)
            self.__count__ = count
            return count, objs
       
    #vistas para edit...
    class edit_form_type(EditableForm):
        __entity__ = ValoresCadena
       
        __omit_fields__        = ['id_valor',"fk_atributo"]       
        
        fk_item = HiddenField
        
        descripcion = TextArea    
        __field_order__ = ['descripcion','valor']
        __disable_fields__ = ['descripcion']    
        
    class edit_filler_type(EditFormFiller):
        __entity__ = ValoresCadena
     
    class defaultCrudRestController(CrudRestController):
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
            
            
            print "put de valores cadenas.."
            print kw
            
            iid = kw['fk_item']
            path = '../' * len(pks) + "?iid=" + str(iid)
            
            self.provider.update(self.model, params=kw)
            redirect(path)
    
    
    new_form_type = ValoresCadenaRegistrationForm


"""configuraciones del modelo ValoresNumero"""
class ValoresNumeroRegistrationForm(AddRecordForm):
    __model__ = ValoresNumero
    __require_fields__ = ['fk_atributo', 'fk_item','valor']
    __omit_fields__ = ['id_valor']
  
class ValoresNumeroCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  ValoresNumero
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
        __url__ = '../valoresnumeros.json' #this just tidies up the URL a bit
       
    class table_filler_type(TableFiller):
        __entity__ = ValoresNumero
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
            
        def fk_atributo(self, obj, **kw):
            atributo = DBSession.query(Atributo).filter_by(id_atributo=obj.fk_atributo).one()
            return atributo.nombre

        def fk_item(self, obj, **kw):
            item = DBSession.query(Item).filter_by(id_item=obj.fk_item).one()
            return item.nombre
    
        def _do_get_provider_count_and_objs(self, **kw):
            
            limit = kw.get('limit', None)
            offset = kw.get('offset', None)
            order_by = kw.get('order_by', None)
            desc = kw.get('desc', False)
            if len(kw) > 0:
                objs = DBSession.query(self.__entity__).filter_by(fk_item=kw['iid']).all()
            else:
                objs = DBSession.query(self.__entity__).all()
                
            count = len(objs)
            self.__count__ = count
            return count, objs
       
    #vistas para edit...
    class edit_form_type(EditableForm):
        __entity__ = ValoresNumero
       
        __omit_fields__        = ['id_valor',"fk_atributo"]       
        
        fk_item = HiddenField
        
        descripcion = TextArea    
        __field_order__ = ['descripcion','valor']
        __disable_fields__ = ['descripcion']    
        
    class edit_filler_type(EditFormFiller):
        __entity__ = ValoresNumero
     
    class defaultCrudRestController(CrudRestController):
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
            
            
            iid = kw['fk_item']
            path = '../' * len(pks) + "?iid=" + str(iid)
            
            self.provider.update(self.model, params=kw)
            redirect(path)
    
    
    new_form_type = ValoresNumeroRegistrationForm


"""configuraciones del modelo ValoresFecha"""
class ValoresFechaRegistrationForm(AddRecordForm):
    __model__ = ValoresFecha
    __require_fields__ = ['fk_atributo', 'fk_item','valor']
    __omit_fields__ = ['id_valor']
  
class ValoresFechaCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  ValoresFecha
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
        __url__ = '../valoresnumeros.json' #this just tidies up the URL a bit
       
    class table_filler_type(TableFiller):
        __entity__ = ValoresFecha
        __limit_fields__ = ['fk_atributo', 'fk_item','valor']
            
        def fk_atributo(self, obj, **kw):
            atributo = DBSession.query(Atributo).filter_by(id_atributo=obj.fk_atributo).one()
            return atributo.nombre

        def fk_item(self, obj, **kw):
            item = DBSession.query(Item).filter_by(id_item=obj.fk_item).one()
            return item.nombre
    
        def _do_get_provider_count_and_objs(self, **kw):
            
            limit = kw.get('limit', None)
            offset = kw.get('offset', None)
            order_by = kw.get('order_by', None)
            desc = kw.get('desc', False)
            if len(kw) > 0:
                objs = DBSession.query(self.__entity__).filter_by(fk_item=kw['iid']).all()
            else:
                objs = DBSession.query(self.__entity__).all()
                
            count = len(objs)
            self.__count__ = count
            return count, objs
       
    #vistas para edit...
    class edit_form_type(EditableForm):
        __entity__ = ValoresFecha
       
        __omit_fields__        = ['id_valor',"fk_atributo"]       
        
        fk_item = HiddenField
        
        descripcion = TextArea    
        __field_order__ = ['descripcion','valor']
        __disable_fields__ = ['descripcion']    
        
    class edit_filler_type(EditFormFiller):
        __entity__ = ValoresFecha
     
    class defaultCrudRestController(CrudRestController):
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
            
            
            iid = kw['fk_item']
            path = '../' * len(pks) + "?iid=" + str(iid)
            
            self.provider.update(self.model, params=kw)
            redirect(path)
    
    
    new_form_type = ValoresFechaRegistrationForm