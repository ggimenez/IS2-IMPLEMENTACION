from sqlalchemy import *
from sqlalchemy.orm import *
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
    #proyectos = relationship("Proyecto", backref="usuario")
	  
    """def __init__(self,nombres, apellidos,username, password):
        self.nombres = nombres
        self.apellidos = apellidos
        self.username = username
        self.password = password"""
	