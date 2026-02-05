"""
    Clase para generar el modelo de Servicio de Auto
"""
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Time, Numeric
from sqlalchemy.dialects.mysql import BIT
from config.db import Base

class ServicioAuto(Base):#pylint:disable=too-few-public-methods
    """
        Docstring
    """
    __tablename__ = "tbd_autos_servicios"

    servicio_auto_id = Column(Integer,primary_key=True,index=True)
    auto_id = Column(Integer,ForeignKey("tbb_autos"))
    servicio_id = Column(Integer,ForeignKey("tbb_servicios"))
    usuario_id = Column(Integer,ForeignKey("tbb_usuarios"))
    fecha = Column(DateTime)
    pagado = Column(BIT)
    monto = Column(Numeric(precision=10,scale=2))
    aprobado = Column(BIT)
    hora = Column(Time)
