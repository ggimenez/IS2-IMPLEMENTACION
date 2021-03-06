import re
import pylons
from pylons.i18n import ugettext as _
from formencode import Invalid
from formencode.schema import SimpleFormValidator
from tw.forms.validators import Email
 
from proyectosaptg.model import DBSession, Usuario
from proyectosaptg import model
 
__all__ = ['UniqueUserName']
 
 
 
def validate_unique_user_name(value_dict, state, validator):    
    user_prueba = DBSession.query(Usuario).filter_by(username=value_dict['username'])
    #if user_prueba is not None:
    return {'user_name':'The user name already exists.'}
           
UniqueUserName = SimpleFormValidator(validate_unique_user_name)
