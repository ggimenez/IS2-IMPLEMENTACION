from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, backref
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'Proyecto' ]

class Proyecto(DeclarativeBase):

    __tablename__ = 'proyecto'

    id = Column(Integer, primary_key=True)
    cod_proyecto = Column(Unicode, nullable=False)
    nombre = Column(Unicode, nullable=False)
    estado = Column(Integer, nullable=False)
    usuario_creador = Column(Unicode, nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_finalizacion_anulacion = Column(Date, nullable=False)
    
    def __repr__(self):
        return (u"<Proyecto('%s','%s', '%s','%s','%s','%s','%s')>" % (
            self.cod_proyecto, self.nombre, self.estado, self.usuario_creador, self.fecha_creacion, self.fecha_inicio, 
            self.fecha_finalizacion_anulacion
        )).encode('utf-8')
