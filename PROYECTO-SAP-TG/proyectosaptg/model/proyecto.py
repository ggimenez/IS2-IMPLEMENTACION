from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import *

from proyectosaptg.model import DeclarativeBase, metadata, DBSession

import datetime 

__all__ = [ 'Proyecto' ]

class Proyecto(DeclarativeBase):

	__tablename__ = 'proyecto'

	id_proyecto = Column(Integer, primary_key=True)
	cod_proyecto = Column(Unicode, nullable=False)
	nombre = Column(Unicode, nullable=False)
	estado = Column(Unicode, nullable=True, default = 'CREADO')
	cant_fases = Column(Integer, nullable=True)
	fecha_creacion = Column(Date, nullable=True, default=datetime.datetime.now())
	fecha_inicio = Column(Date, nullable=True)
	fecha_finalizacion_anulacion = Column(Date, nullable=True)
	user_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    
	"""
	def __repr__(self):
		return (u"<Proyecto('%s','%s', '%s','%s','%s','%s')>" % (
			self.cod_proyecto, self.nombre, self.estado, self.fecha_creacion, self.fecha_inicio, 
			self.fecha_finalizacion_anulacion
		)).encode('utf-8')"""
