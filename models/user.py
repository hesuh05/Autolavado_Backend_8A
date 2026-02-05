"""
    Este archivo define la clase de
        - us_id pk
        - us_nombre vc60
        - us_apellidoPaterno vc60
        - us_apellidoMaterno vc60
        - us_usuario vc60
        - us_password vc256
        - ro_id int
"""
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from config.db import Base

class MyEstatus(PyEnum):#pylint:disable=too-few-public-methods
    """
        Docstring para MyEstatus
    """
    ONE=""
    TWO=""
    THREE=""

class Usuario(Base):#pylint:disable=too-few-public-methods
    """
        Docstring para Usuario
    """
    __tablename__ = "tbb_usuarios"

    usuario_id = Column(Integer,primary_key=True,index=True)
    rol_id = Column(Integer, ForeignKey("tbc_roles.Id"))
    nombre_usuario = Column(String(60))
    correo_electronico = Column(String(100))
    contrasena = Column(String(40))
    numero_telefonico_Movil = Column(String(20))
    estatus = Column(Enum(MyEstatus))
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
