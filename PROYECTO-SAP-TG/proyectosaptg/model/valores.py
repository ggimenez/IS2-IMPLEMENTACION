from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'Valores' ]

class Valores(DeclarativeBase):

    __tablename__ = 'valores'

    id_valor = Column(Integer, primary_key=True)
    fk_atributo = Column(Integer, ForeignKey('atributo.id_atributo'))
    fk_item = Column(Integer, ForeignKey('item.id_item'))
    
    valor = Column(Unicode, nullable=False)
    
    
