"""
    Clase para generar el modelo de Cliente
"""
from sqlalchemy import Column, Integer, String
from config.db import Base

class Cliente(Base):#pylint:disable=too-few-public-methods
    """
        Docstring
    """
    __tablename__ = "tbb_clientes"

    cliente_id = Column(Integer,primary_key=True,index=True)
    nombre = Column(String(60))
    apellido_materno = Column(String(60))
    apellido_paterno = Column(String(60))
    direccion = Column(String(255))
    correo_electronico = Column(String(55))
    telefono = Column(String(15))
    contrasena = Column(String(40))
