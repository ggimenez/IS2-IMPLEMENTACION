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



"""configuraciones del modelo Item"""
class ItemRegistrationForm(AddRecordForm):
    __model__ = Item
    __require_fields__ = ['nombre','id_fase_fk']
    __omit_fields__ = ['id_item','cod_item','version','total_peso', 'estado', 'relaciones','id_linea_base_fk', 
                    'relacion','linea_base']
    
    cod_item           = TextField
    nombre = TextField
    __dropdown_field_names__ = {'tipo_item':'nombre'}
    
    tipo_item = SingleSelectField
    
    
    
class ItemCrudConfig(CrudRestControllerConfig):
    class table_type(TableBase):
        __entity__ =  Item
        __limit_fields__ = ['cod_item', 'nombre','estado', 'version','peso','id_tipo_item_fk','id_linea_base_fk','relaciones']
        __url__ = '/item.json' #this just tidies up the URL a bit
        __xml_fields__ = ['Atributos']
        __headers__ = {'id_tipo_item_fk':'Atributos'}


    class table_filler_type(TableFiller):
        __entity__ = Item
        __limit_fields__ = ['cod_item', 'nombre','estado', 'version','peso','id_tipo_item_fk','id_linea_base_fk','relaciones']

               
        
        def id_tipo_item_fk(self, obj):
            
            tipo_item = DBSession.query(TipoItem).filter_by(id_tipo_item=obj.id_tipo_item_fk).one()
            atributos = tipo_item.atributos
             
            
            id_item = obj.id_item
            
            
            retorno = ''
            for a in atributos:
                nombre_atributo = a.nombre
                
                if a.tipo_dato == "Cadena":
                    controlador = "valorescadenas"
                elif a.tipo_dato == "Fecha":
                    controlador = "valoresfechas"
                elif a.tipo_dato == "Numerico":
                    controlador = "valoresnumeros"
                
                retorno = retorno + ('<a href="../'+controlador+'/?iid='+str(id_item)+'">'+nombre_atributo+'</a>') + ','
           
            print retorno
            
            return retorno.join(('<div>', '</div>'))


     
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
            '<a class="relacion_link" href="../relacions/?iid='+pklist+'">Relaciones</a>'\
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
            
            
            val = kw["fid"]
                        
            retorno =  CrudRestController.get_all(self, *args, **kw)
           
            retorno["fid"] = val 
            
            return retorno
            
        @without_trailing_slash
        @expose('proyectosaptg.templates.new_item')
        def new(self, *args, **kw):
            """Display a page to show a new record."""
            print "new itme\n"
            
            """filtramos solo los Tipos de Items asociados al Proyecto"""
            id_fase = args[0]
            #traemos la fase de la BD
            fase = DBSession.query(Fase).filter_by(id_fase = id_fase).one()
            #obtenemos el id del Proyecto, traemos el Proyecto y sus Tipos de Items
            id_proyecto = fase.proyecto_id
            proyecto = DBSession.query(Proyecto).filter_by(id_proyecto = id_proyecto).one()
            tipo_items = proyecto.tipo_items
            #obtenemos lo id y los nombres de los tipos de items del Proyecto para enviarlos como las opciones 
            #disponibles
            id_tipo_items = []
            for tipo_item in tipo_items:
                id_tipo_items.append((tipo_item.id_tipo_item,tipo_item.nombre))
                
            print id_tipo_items    
            
            
            
            
            if len(args) > 0:
                print "entre en el if\n"
                kw['id_fase_fk'] = args[0]
                print kw
                print args
    
                
            
            tmpl_context.widget = self.new_form
            
            retorno = dict(value=kw, model=self.model.__name__)
            
            retorno["id_tipo_items"] = id_tipo_items
            
            return retorno
            
        
        
        @expose()
        @registered_validate(error_handler=new)
        def post(self, *args, **kw):
            
            print "post item..:"
            print kw
            
            
            fid = kw["id_fase_fk"]
            
            tipo_item = DBSession.query(TipoItem).filter_by(id_tipo_item=kw['tipo_item']).one()
            
            print tipo_item
            
            new_acumulador = tipo_item.acumulador + 1
            
            kw['cod_item'] = tipo_item.cod_tipo_item + "-" + str(new_acumulador)
            
            new_item = self.provider.create(self.model, params=kw)
            
            #generamos los campos para los valores de los atributos...
            atributos_new_item = new_item.tipo_item.atributos
            fk_item = new_item.id_item 
            for atributo in atributos_new_item:
                
                tipo_dato_atr = atributo.tipo_dato
                
                
                fk_atributo = atributo.id_atributo
                el_valor = {}
                el_valor['fk_atributo'] = fk_atributo
                el_valor['fk_item'] = fk_item
                #el_valor['valor'] = "vacio"
                el_valor['descripcion'] = "Item:" + kw['nombre'] + "\nAtributo:" + atributo.nombre + "\nTipo:" + atributo.tipo_dato
                
                if tipo_dato_atr == "Cadena":
                    self.provider.create(ValoresCadena, params=el_valor)
                elif tipo_dato_atr == "Fecha":
                    self.provider.create(ValoresFecha, params=el_valor)
                elif tipo_dato_atr == "Numerico":
                    self.provider.create(ValoresNumero, params=el_valor)
                
                
            tipo_item.acumulador = new_acumulador
            DBSession.flush()
            #DBSession.commit()
             
            path = '../?fid='+ str(fid)
            
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
