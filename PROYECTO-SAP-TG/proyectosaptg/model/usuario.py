from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, backref
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

import datetime 

__all__ = [ 'Usuario' ]

class Usuario(DeclarativeBase):

    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)
    nombres = Column(Unicode, nullable=False)
    apellidos = Column(Unicode, nullable=False)	
    username = Column(Unicode, nullable=False, unique=True)
    password = Column(Unicode, nullable=False)
    fecha_creacion = Column(Date, nullable=False, default=datetime.datetime.now()  )
	

    def __repr__(self):
        return (u"<Usuario('%s','%s', '%s', '%s', '%s', '%s')>" % (
            self.id_usuario, self.nombres, self.apellidos, self.username, self.password, self.fecha_creacion
        )).encode('utf-8')

