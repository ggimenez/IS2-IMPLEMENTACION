from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation, synonym

from proyectosaptg.model import DeclarativeBase, metadata, DBSession



relacion_item_table = Table('relacion_item_table', metadata,
    Column('id_item', Integer, ForeignKey('item.id_item',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('id_relacion', Integer, ForeignKey('relacion.id_relacion',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)
