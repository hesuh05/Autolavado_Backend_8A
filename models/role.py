"""
    Clase para generar el modelo para los tipos de rol
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Relationship
from config.db import Base

class Rol(Base):
    """
        Docstring para Rol
    """
    __tablename__ = "tbc_roles"
    
    Id = Column(Integer, primary_key=True)
    nombreRol = Column(String(15))
    estado = Column(Boolean)
