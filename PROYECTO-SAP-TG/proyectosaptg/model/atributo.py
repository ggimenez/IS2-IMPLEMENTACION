from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'Atributo' ]

class Atributo(DeclarativeBase):

    __tablename__ = 'atributo'

    id_atributo = Column(Integer, primary_key=True)
    cod_atributo = Column(Unicode, nullable=False,unique=True)
    nombre = Column(Unicode, nullable=False)
    descripcion = Column(Unicode, nullable=True)
    tipo_dato = Column(Unicode, nullable=True)	
    #id_tipo_item_fk = Column(Integer, ForeignKey('tipo_item.id_tipo_item'))
