
# -*- coding: utf-8 -*-
from tgext.admin.config import AdminConfig, CrudRestControllerConfig
from formencode import Schema
from formencode.validators import FieldsMatch
from tw.forms import *
from sprox.fillerbase import TableFiller, EditFormFiller
from sprox.formbase import AddRecordForm, EditableForm
from sprox.tablebase import TableBase
from sprox.widgets import PropertyMultipleSelectField
from proyectosaptg.model import *
from tg import expose, flash, require, url, request, redirect, tmpl_context
from tg.decorators import without_trailing_slash, with_trailing_slash, paginate
from tgext.crud.decorators import registered_validate, register_validators, catch_errors
from tgext.crud.controller import CrudRestController
from repoze.what.predicates import has_permission

class MyPropertyMultipleSelectField(PropertyMultipleSelectField):
    def _my_update_params(self, d, nullable=False):
        
        print "MyPropertyMultipleSelectField,d:\n:"
        print d
        
        laFase = DBSession.query(Fase).filter_by(id_fase=d["fid"]).one()
        items_fase = laFase.items
        
        options = [(item_aux.id_item, item_aux.nombre)
                            for item_aux in items_fase]
        d['options']= options
        return d

"""configuraciones del modelo LineaBase"""
class LineaBaseRegistrationForm(AddRecordForm):
	__model__			= LineaBase
	__require_fields__		= ['cod_linea_base', 'descripcion', 'items']
	__omit_fields__		= ['id_linea_base', 'version', 'estado','peso_acumulado', 'fecha_creacion', 'id_fase_fk']
	cod_linea_base 		= TextField
	descripcion 		= TextArea
	__dropdown_field_names__ = {'items':'nombre'}
	items = MyPropertyMultipleSelectField

class LineaBaseCrudConfig(CrudRestControllerConfig):
	class table_type(TableBase):
		__entity__ 		=  LineaBase
		__limit_fields__	= ['cod_linea_base', 'descripcion', 'items']
		__url__ 		= '../linea_base.json' #this just tidies up the URL a bit

	class table_filler_type(TableFiller):
		__entity__ 		= LineaBase
		__limit_fields__ 	= ['id_linea_base','cod_linea_base','descripcion', 'items']
		
		def __actions__(self, obj):
			"""Override this function to define how action links should be displayed for the given record."""
			primary_fields 	= self.__provider__.get_primary_fields(self.__entity__)
			pklist 		= '/'.join(map(lambda x: str(getattr(obj, x)), primary_fields))

			value 		=  '<div>'
			if has_permission(''):
			<div><a class="edit_link" href="'+pklist+'/edit" style="text-decoration:none">edit</a>'\
			'</div><div>'\
			'<form method="POST" action="'+pklist+'" class="button-to">'\
			'<input type="hidden" name="_method" value="DELETE" />'\
			'<input class="delete-button" onclick="return confirm(\'Est&aacute; seguro que desea eliminar?\');" value="delete" type="submit" '\
			'style="background-color: transparent; float:left; border:0; color: #286571; display: inline; margin: 0; padding: 0;"/>'\
			'</form>'\
			'</div></div>'

			return value

		def items(self, obj, **kw):
			nombres_items = ""
			for a in obj.items:
				nombres_items = nombres_items + ", " + a.nombre
			return nombres_items[1:]

		def _do_get_provider_count_and_objs(self, **kw):

			limit 	= kw.get('limit', None)
			offset 	= kw.get('offset', None)
			order_by 	= kw.get('order_by', None)
			desc 	= kw.get('desc', False)

			if len(kw) > 0:
				objs 	= DBSession.query(self.__entity__).filter_by(id_fase_fk = kw['fid']).all()
			else:
				objs 	= DBSession.query(self.__entity__).all()

			count 	   = len(objs)
			self.__count__ = count
			return count, objs

	class defaultCrudRestController(CrudRestController):

		@with_trailing_slash
		@expose('proyectosaptg.templates.get_all_lineabase')
		@expose('json')
		@paginate('value_list', items_per_page=7)
		def get_all(self, *args, **kw):
			fid 		= kw['fid']
			retorno 		= CrudRestController.get_all(self, *args, **kw)
			retorno['fid'] 	= fid

			return retorno

		@without_trailing_slash
		@expose('proyectosaptg.templates.new_linea_base')
		def new(self, *args, **kw):
			"""Display a page to show a new record."""

			if len(args) > 0:
				kw['id_fase_fk']=  args[0] 

			tmpl_context.widget = self.new_form
			retorno 		= dict(value = kw, model = self.model.__name__)
			retorno['fid']	= args[0]

			return retorno

		@expose()
		@registered_validate(error_handler=new)
		def post(self, *args, **kw):
			fid 	= kw['id_fase_fk']
			new_item 	= self.provider.create(self.model, params=kw)
			path 	= '../?fid='+ str(fid)

			raise redirect(path)

		@expose()
		def post_delete(self, *args, **kw):
			"""This is the code that actually deletes the record"""
			#obtenemos el id de la linea base para hacer el filtrado despues de la redireccion
			lb_to_del 	= DBSession.query(LineaBase).filter_by(id_linea_base=args[0]).one()
			fid 	= lb_to_del.id_fase_fk
			pks 	= self.provider.get_primary_fields(self.model)
			d 		= {}

			for i, arg in enumerate(args):
				d[pks[i]] = arg

			self.provider.delete(self.model, d)
			path 	= './' + '../' * (len(pks) - 1) + '?fid=' + str(fid)

			redirect(path)

		@expose('tgext.crud.templates.edit')
		def edit(self, *args, **kw):
			"""Display a page to edit the record."""
			tmpl_context.widget = self.edit_form
			pks 		= self.provider.get_primary_fields(self.model)
			kw 			= {}

			for i, pk in  enumerate(pks):
				kw[pk] 		= args[i]

			value 		= self.edit_filler.get_value(kw)
			value['_method'] 	= 'PUT'

			return dict(value = value, model = self.model.__name__, pk_count = len(pks))

		@expose()
		@registered_validate(error_handler=edit)
		def put(self, *args, **kw):
			"""update"""
			pks 		= self.provider.get_primary_fields(self.model)
			for i, pk in enumerate(pks):
				if pk not in kw and i < len(args):
					kw[pk] 	= args[i]

			fid 		= kw['id_fase_fk']
			path 		= '../' * len(pks) + "?fid=" + str(fid)

			self.provider.update(self.model, params = kw)
			redirect(path)

	new_form_type 		= LineaBaseRegistrationForm

