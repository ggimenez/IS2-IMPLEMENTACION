# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
from repoze.what import predicates

from proyectosaptg.lib.base import BaseController
from proyectosaptg.model import DBSession, metadata
from proyectosaptg.controllers.error import ErrorController
from proyectosaptg import model
from proyectosaptg.controllers.secure import SecureController

from tg import tmpl_context
#from proyectosaptg.widgets.add_usuario_form import create_add_user_form



from tg import validate


from proyectosaptg.model import *

from sprox.formbase import AddRecordForm
from tw.forms import TextField,CalendarDatePicker

from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller


from tgext.crud import CrudRestController
from proyectosaptg.model import DBSession, Usuario


from tw.core import WidgetsList
from tw.forms import TableForm, TextField, CalendarDatePicker, SingleSelectField, TextArea, PasswordField
from formencode.validators import Int, NotEmpty, DateConverter, DateValidator


from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller


from proyectosaptg.controllers.controlador_usuarios import * 
from proyectosaptg.controllers.controlador_proyectos import *



#abm de forma manual
from tg import tmpl_context
from proyectosaptg.widgets.usuario_form import create_usuario_form



class UsuarioRootController(BaseController):
    
    @expose('proyectosaptg.templates.usuario_list')
    def index(self):
        return dict(usuarios=DBSession.query(Usuario),
          page='ToscaSample Usuario list')
    
    #new user manual
    @expose('proyectosaptg.templates.new_form')
    def new(self, **kw):
        """Show form to add new movie data record."""
        tmpl_context.form = create_usuario_form
        return dict(modelname='Usuario', value=kw)                              

    @expose()
    def create(self, **kw):
        """Create a movie object and save it to the database."""
        usuario = Usuario()
        usuario.nombres = kw['nombres']
        usuario.apellidos = kw['apellidos']
        usuario.username = kw['username']
        usuario.password = kw['password']
        DBSession.add(usuario)
        flash("Usuario was successfully created.")
        redirect("list")
        
    @expose("proyectosaptg.templates.usuario_list")
    def list(self):
      """List all movies in the database"""
      return dict(usuarios=DBSession.query(Usuario),
          page='ToscaSample Usuario list')    