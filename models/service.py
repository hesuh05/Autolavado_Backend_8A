"""
    Clase para generar el modelo de Servicio
"""
from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base

class Servicio(Base):#pylint:disable=too-few-public-methods
    """
        Docstring
    """
    __tablename__ = "tbb_servicios"

    servicio_id = Column(Integer,primary_key=True,index=True)
    usuario_id = Column(Integer,ForeignKey("tbb_usuarios"))
    nombre = Column(String(80))
    descripcion = Column(LONGTEXT)
    precio = Column(Numeric(precision=18,scale=2))
    estatus = Column(String(45))
