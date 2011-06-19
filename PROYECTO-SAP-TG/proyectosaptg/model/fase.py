from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

from proyectosaptg.model.auth import fase_group_table
import datetime 

__all__ = [ 'Fase' ]


#tabla intermedia entre fases y tipos de items
fase_tipo_item_table = Table('fase_tipo_item', metadata,
    Column('fase_id', Integer, ForeignKey('fase.id_fase',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('tipo_item_id', Integer, ForeignKey('tipo_item.id_tipo_item',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)



class Fase(DeclarativeBase):

    __tablename__ = 'fase'

    id_fase = Column(Integer, primary_key=True)
    cod_fase = Column(Unicode, nullable=False,unique=True)
    nombre = Column(Unicode, nullable=False)
    descripcion = Column(Unicode, nullable=True)                
    estado = Column(Unicode, nullable=False, default = 'CREADO')
    
    
    lineas_bases = relationship("LineaBase")
   
    items = relationship("Item")
    
    proyecto_id = Column(Integer, ForeignKey('proyecto.id_proyecto'), nullable=False)
    
    
    orden = Column(Integer, nullable=False)
    bool_primero = Column(Integer, nullable=False)
    bool_ultimo = Column(Integer, nullable=False)
    
    roles = relation('Group', secondary=fase_group_table)
    tipo_items = relationship('TipoItem', secondary=fase_tipo_item_table)    
    
    
