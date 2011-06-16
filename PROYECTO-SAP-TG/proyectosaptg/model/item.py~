from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession
from proyectosaptg.model.relacion_item import *
from sqlalchemy.ext.declarative import declarative_base

from relacion import * 

from proyectosaptg.model.relacion_item_table  import *

__all__ = [ 'Item' ]

Base = declarative_base()





class Item(DeclarativeBase):

    __tablename__ = 'item'

    id_item = Column(Integer, primary_key=True)
    cod_item = Column(Unicode, nullable=False)
    nombre = Column(Unicode, nullable=False)
    estado = Column(Unicode, nullable=False, default = 'REVISION')
    version = Column(Integer, nullable=False, default = 0)
    peso = Column(Integer, nullable=False)
    total_peso = Column(Integer, nullable=True)
    descripcion = Column(Unicode, nullable=True)	
    
    id_tipo_item_fk = Column(Integer, ForeignKey('tipo_item.id_tipo_item'))
    tipo_item = relationship("TipoItem", uselist=False)

    id_linea_base_fk = Column(Integer, ForeignKey('linea_base.id_linea_base'))

    id_fase_fk = Column(Integer, ForeignKey('fase.id_fase'),nullable=False)

    relaciones = relation('Relacion', secondary=relacion_item_table)