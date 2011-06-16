from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'ValoresCadena' ]

class ValoresCadena(DeclarativeBase):

    __tablename__ = 'valores_cadena'

    id_valor = Column(Integer, primary_key=True)
    fk_atributo = Column(Integer, ForeignKey('atributo.id_atributo'))
    fk_item = Column(Integer, ForeignKey('item.id_item'))
    
    valor = Column(Unicode, nullable=False, default= 'sin valor')
    
    descripcion = Column(Unicode, nullable=False)    
