# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect




from tg.decorators import with_trailing_slash
from tg import config as tg_config




from pylons.i18n import ugettext as _, lazy_ugettext as l_
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
from repoze.what import predicates
from repoze.what.predicates import not_anonymous

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
#from proyectosaptg.model import DBSession, Usuario


from tw.core import WidgetsList
from tw.forms import TableForm, TextField, CalendarDatePicker, SingleSelectField, TextArea, PasswordField
from formencode.validators import Int, NotEmpty, DateConverter, DateValidator


from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller


#from proyectosaptg.controllers.controlador_usuarios import * 
#from proyectosaptg.controllers.controlador_proyectos import *
from proyectosaptg.controllers.admin import *
from proyectosaptg.controllers.admin2 import *



import inspect
from sqlalchemy.orm import class_mapper

from proyectosaptg import model
from proyectosaptg.model import DBSession


class MyAdminSysController(AdminController):
    menu = {}
    def __init__(self, models, session, config_type=None, translations=None, menu=None):
        super(AdminController, self).__init__()
        if translations is None:
            translations = {}
        if config_type is None:
            config = AdminConfig(models, translations)
        else:
            config = config_type(models, translations)

        if config.allow_only:
            self.allow_only = config.allow_only

        self.config = config
        self.session = session

        self.menu = menu


        self.default_index_template = ':'.join((tg_config.default_renderer, self.index.decoration.engines.get('text/html')[1]))
        if self.config.default_index_template:
            self.default_index_template = self.config.default_index_template

    @with_trailing_slash
    @expose('tgext.admin.templates.index')
    def index(self):
        #overrides the template for this method
        original_index_template = self.index.decoration.engines['text/html']
        new_engine = self.default_index_template.split(':')
        new_engine.extend(original_index_template[2:])
        self.index.decoration.engines['text/html'] = new_engine
        return dict(models=self.menu)

    def _make_controller(self, config, session):
        m = config.model
        Controller = config.defaultCrudRestController
        class ModelController(Controller):
            model        = m
            table        = config.table_type(session)
            table_filler = config.table_filler_type(session)
            new_form     = config.new_form_type(session)
            new_filler   = config.new_filler_type(session)
            edit_form    = config.edit_form_type(session)
            edit_filler  = config.edit_filler_type(session)
            allow_only   = config.allow_only
        menu_items = None
        if self.config.include_left_menu:
            menu_items = self.menu
        return ModelController(session, menu_items)



class RootController(BaseController):
    """
    The root controller for the PROYECTO-SAP-TG application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

    panel = ControlPanelController()
    another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    #prueba con crudcontroller	
    #usuarios = UsuarioRootController(DBSession)
    #proyectos = ProyectoController(DBSession)
    

    secc = SecureController()    

    #admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    
    

    menu_adm_sys = {}
    menu_adm_sys[User.__name__.lower()] = User
    menu_adm_sys[Permission.__name__.lower()] = Permission
    menu_adm_sys[Group.__name__.lower()] = Group
    menu_adm_sys[Proyecto.__name__.lower()] = Proyecto
    menu_adm_sys[TipoItem.__name__.lower()] = TipoItem
    menu_adm_sys[Atributo.__name__.lower()] = Atributo
    #admin = AdminController(model, DBSession, config_type=MyAdminConfig, xfavor=models)
    menu_gconfig = {}
    
    menu_gconfig[Relacion.__name__.lower()] = Relacion
    menu_gconfig[LineaBase.__name__.lower()] = LineaBase
    
    admin= MyAdminSysController(model, DBSession, config_type=MyAdminConfig, menu=menu_adm_sys)
    
    gconfig= MyAdminSysController(model, DBSession, config_type=MyAdmin2Config, menu=menu_gconfig)
    
    #admin = AdminController([Proyecto, User], DBSession, config_type=MyAdminConfig)
    error = ErrorController()

    
    @expose('proyectosaptg.templates.index')
    #@require(not_anonymous(msg='Por favor inicia sesion para continuar.'))
    def index(self):
        return dict(page='index')	


    @expose('proyectosaptg.templates.about')
    @require(not_anonymous(msg='Por favor inicia sesion para continuar.'))
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('proyectosaptg.templates.environ')
    @require(not_anonymous(msg='Por favor inicia sesion para continuar.'))
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(environment=request.environ)

    @expose('proyectosaptg.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params=kw)

    @expose('proyectosaptg.templates.authentication')
    @require(not_anonymous(msg='Por favor inicia sesion para continuar.'))
    def auth(self):
        """Display some information about auth* on this application."""
        return dict(page='auth')

    @expose('proyectosaptg.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('proyectosaptg.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('proyectosaptg.templates.login')
    def login(self, came_from=url('/')):
        """Start the user login."""
        login_counter = request.environ['repoze.who.logins']
        if login_counter > 0:
                        flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
            came_from=came_from)

    @expose()
    def post_login(self, came_from='/'):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
                        login_counter = request.environ['repoze.who.logins'] + 1
                        redirect('/login', came_from=came_from, __logins=login_counter)
        userid = request.identity['repoze.who.userid']
        #print "esto es userid:\n"
        #print userid
        #id_el = request.identity['repoze.who.user_id']
        #print id_el
        
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from=url('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)
