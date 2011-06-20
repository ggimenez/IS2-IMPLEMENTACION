from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *
from proyectosaptg.model import DeclarativeBase, metadata, DBSession
import datetime 

__all__ = [ 'ValoresFecha' ]

class ValoresFecha(DeclarativeBase):
    __tablename__ = 'valores_fecha'

    id_valor = Column(Integer, primary_key=True)
    fk_atributo = Column(Integer, ForeignKey('atributo.id_atributo'))
    fk_item = Column(Integer, ForeignKey('item.id_item'))
    valor = Column(Date, nullable=False, default=datetime.datetime.now())
    descripcion = Column(Unicode, nullable=False)    
    bool_ultimo = Column(Integer, default=1)
    version = Column(Integer, nullable=False, default = 0)
