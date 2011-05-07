from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

import datetime 

__all__ = [ 'Fase' ]

class Fase(DeclarativeBase):

	__tablename__ = 'fase'

	id_fase = Column(Integer, primary_key=True)
	cod_fase = Column(Unicode, nullable=False,unique=True)
	nombre = Column(Unicode, nullable=False)
	estado = Column(Unicode, nullable=False, default = 'CREADO')
	lineas_bases = relationship("LineaBase", backref="fase")
	items = relationship("Item", backref="fase")
