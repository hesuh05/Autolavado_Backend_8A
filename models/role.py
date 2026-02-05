"""
    Clase para generar el modelo para los tipos de rol
"""

from sqlalchemy import Column, Integer, String, Boolean
from config.db import Base

class Role(Base):#pylint:disable=too-few-public-methods
    """
        Docstring para Rol
    """
    __tablename__ = "tbc_roles"

    Id = Column(Integer, primary_key=True)
    Nombre_Rol = Column(String(15))
    Estado = Column(Boolean)
