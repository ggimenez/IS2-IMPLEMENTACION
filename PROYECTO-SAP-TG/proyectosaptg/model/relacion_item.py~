"""
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from sqlalchemy.ext.declarative import declarative_base
from proyectosaptg.model.item import *

Base = declarative_base()

association_table = Table('relacion_item', Base.metadata,
    Column('id_item', Integer, ForeignKey('item.id_item')),
    Column('id_relacion', Integer, ForeignKey('relacion.id_relacion'))
)
"""
