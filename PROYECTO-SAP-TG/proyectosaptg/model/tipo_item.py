from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

import datetime 

__all__ = [ 'TipoItem' ]

class TipoItem(DeclarativeBase):

	__tablename__ = 'tipo_item'

	id_tipo_item = Column(Integer, primary_key=True)
	cod_tipo_item = Column(Unicode, nullable=False,unique=True)
	descripcion = Column(Unicode, nullable=True)
	atributoss = relationship("Atributo", backref="tipo_item")
