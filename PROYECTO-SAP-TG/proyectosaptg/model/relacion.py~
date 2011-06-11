from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

from proyectosaptg.model.relacion_item_table  import *

import datetime 

__all__ = [ 'Relacion' ]

class Relacion(DeclarativeBase):

    __tablename__ = 'relacion'

    id_relacion = Column(Integer, primary_key=True)
    cod_relacion = Column(Unicode, nullable=False,unique=True)
    estado = Column(Unicode, nullable=False, default = 'CERRADO')
    descripcion = Column(Unicode, nullable=True)

    #items = relation('Item', secondary=relacion_item_table, backref='relacion')

    item_origen_fk = Column(Integer, ForeignKey('item.id_item'))
    item_destino_fk = Column(Integer, ForeignKey('item.id_item'))