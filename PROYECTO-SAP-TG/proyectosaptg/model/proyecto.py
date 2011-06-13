from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

from proyectosaptg.model.auth import proyecto_group_table

import datetime 

#tabla intermedia entre proyectos y tipos de items
proyecto_tipo_item_table = Table('proyecto_tipo_item', metadata,
    Column('proyecto_id', Integer, ForeignKey('proyecto.id_proyecto',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('tipo_item_id', Integer, ForeignKey('tipo_item.id_tipo_item',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)



__all__ = [ 'Proyecto' ]

class Proyecto(DeclarativeBase):

    __tablename__ = 'proyecto'

    id_proyecto = Column(Integer, primary_key=True)
    cod_proyecto = Column(Unicode, nullable=False,unique=True)
    nombre = Column(Unicode, nullable=False)
    estado = Column(Unicode, nullable=False, default = 'CREADO')
    cant_fases = Column(Integer, nullable=True)
    fecha_creacion = Column(Date, nullable=True, default=datetime.datetime.now())
    fecha_inicio = Column(Date, nullable=True)
    fecha_finalizacion_anulacion = Column(Date, nullable=True)
    
    usuario_creador = Column(Unicode, nullable=False)
   
	
    
    fases = relationship("Fase")
    
    
    tipo_items = relationship('TipoItem', secondary=proyecto_tipo_item_table)

