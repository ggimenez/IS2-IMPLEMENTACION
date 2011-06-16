from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession
import datetime 


__all__ = [ 'ValoresGeneral' ]

class ValoresGeneral(DeclarativeBase):

    __tablename__ = 'valores_general'

    id_valor_general = Column(Integer, primary_key=True)
    atributo = Column(Unicode, nullable=True)    
    item = Column(Unicode, nullable=True)    
    
    valor = Column(Unicode, nullable=True)    
    
    
