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


from tg import validate
from tg import tmpl_context

from proyectosaptg.model import *

from sprox.formbase import AddRecordForm
from tw.forms import TextField,CalendarDatePicker
class AddUsuario(AddRecordForm):
    __model__ = Usuario
    __omit_fields__ = [
        'id_usuario', 
    ]
    nombres = TextField
    apellidos = TextField	
    username = TextField
add_usuario_form = AddUsuario(DBSession)

__all__ = ['RootController']


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
    secc = SecureController()

    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    @expose('proyectosaptg.templates.index')
    def index(self, **named):
        """Handle the front-page."""
        usuarios = DBSession.query( Usuario ).order_by( Usuario.username )
        tmpl_context.add_usuario_form = add_usuario_form
        from webhelpers import paginate
        count = usuarios.count()
        page =int( named.get( 'page', '1' ))
        currentPage = paginate.Page(
            usuarios, page, item_count=count,
            items_per_page=5,
        )
        usuarios = currentPage.items
        return dict(
            page='index',
            usuarios = usuarios,
            currentPage = currentPage,
        )

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

    @expose( )
    @validate(
        form=add_usuario_form,
        error_handler=index,
    )
    def add_usuario( self, nombres, apellidos, username, password ,fecha_creacion, **named ):
        """Create a new Usuario record"""
        new = Usuario(
	    nombres = nombres,
	    apellidos = apellidos,		
            username = username,
            password = password,
            fecha_creacion = fecha_creacion,
        )
        DBSession.add( new )
        flash( '''Added usuario: %s'''%( username, ))
        redirect( './index' )

	   	
