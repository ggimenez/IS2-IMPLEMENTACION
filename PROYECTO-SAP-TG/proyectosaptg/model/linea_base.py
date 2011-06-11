from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

import datetime 

__all__ = [ 'LineaBase' ]

class LineaBase(DeclarativeBase):

    __tablename__ = 'linea_base'

    id_linea_base = Column(Integer, primary_key=True)
    cod_linea_base = Column(Unicode, nullable=False,unique=True)
    version = Column(Integer, nullable=False, default = 0)
    descripcion = Column(Unicode, nullable=True)
    estado = Column(Unicode, nullable=False, default = 'CERRADO')
    peso_acumulado = Column(Integer, nullable=True, default = 0)
    fecha_creacion = Column(Date, nullable=False, default=datetime.datetime.now())

    id_fase_fk = Column(Integer, ForeignKey('fase.id_fase'))
    
    items = relationship("Item")
