from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

from proyectosaptg.model.atributo import *

import datetime 

__all__ = [ 'TipoItem' ]


"""relacion muchos a muchos entre TipoItem y Atributos"""
tipo_item_atributo_table = Table('tipo_item_atributo', metadata,
                            Column('tipo_item_id', Integer, ForeignKey('tipo_item.id_tipo_item'), primary_key = True),
                            Column('atributo_id', Integer, ForeignKey('atributo.id_atributo'), primary_key = True))


class TipoItem(DeclarativeBase):

    __tablename__ = 'tipo_item'

    id_tipo_item = Column(Integer, primary_key=True)
    nombre = Column(Unicode, nullable=False)
    cod_tipo_item = Column(Unicode, nullable=False,unique=True)
    descripcion = Column(Unicode, nullable=True)
    #atributos = relationship("Atributo", backref="tipo_item")
    atributos = relationship(Atributo, secondary=tipo_item_atributo_table)