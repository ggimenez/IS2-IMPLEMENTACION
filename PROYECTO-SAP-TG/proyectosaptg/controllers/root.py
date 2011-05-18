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
#from proyectosaptg.controllers.controlador_proyectos import *



#abm de forma manual
from tg import tmpl_context
#from proyectosaptg.widgets.usuario_form import create_usuario_form
#from proyectosaptg.controllers.user_controller import *


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

    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    
    @expose('proyectosaptg.templates.index')
    def index(self):
        return dict(page='index')	


    @expose('proyectosaptg.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('proyectosaptg.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(environment=request.environ)

    @expose('proyectosaptg.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params=kw)

    @expose('proyectosaptg.templates.authentication')
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
