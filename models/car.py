"""
    Clase para generar el modelo de Auto
    Este archivo define la clase de
        - au_id pk
        - au_modelo vc45
        - au_matricula vc45
        - au_color vc60
        - us_usuario int
        - au_Tipo varchar(45)
"""

from sqlalchemy import Column, Integer, String, ForeignKey

from config.db import Base


class Auto(Base):#pylint:disable=too-few-public-methods
    """
        Docstring para Auto
    """
    __tablename__ = "tbb_autos"

    auto_id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String(45))
    matricula = Column(String(15))
    color = Column(String(45))
    cliente_id = Column(Integer,ForeignKey("tbb_clientes"))
    tipo = Column(String(45))
