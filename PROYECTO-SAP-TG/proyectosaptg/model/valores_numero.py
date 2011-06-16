from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession
import datetime 


__all__ = [ 'ValoresNumero' ]

class ValoresNumero(DeclarativeBase):

    __tablename__ = 'valores_numero'

    id_valor = Column(Integer, primary_key=True)
    fk_atributo = Column(Integer, ForeignKey('atributo.id_atributo'))
    fk_item = Column(Integer, ForeignKey('item.id_item'))
    
    valor = Column(Integer, nullable=False,default= 0)
    
    descripcion = Column(Unicode, nullable=False)    
