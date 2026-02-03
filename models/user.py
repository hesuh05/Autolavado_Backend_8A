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
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Relationship
from config.db import Base


class Usuario(Base):
    """
        Docstring para Usuario
    """
    __tablename__ = "tbb_usuarios"
    Id = Column(Integer,primary_key=True,index=True)
    Rol_Id = Column(Integer, ForeignKey("tbc_roles.Id"))
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(100))
    Contrasena = Column(String(40))
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column(Enum(MyEstatus))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
