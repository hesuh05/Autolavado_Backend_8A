"""
    Este archivo define la clase de
        - au_id pk
        - au_modelo vc45
        - au_matricula vc45
        - au_color vc60
        - us_usuario int
        - au_Tipo varchar(45)
"""

from pydantic import BaseModel

class Auto(BaseModel):
    """
        Docstring para Auto
    """
    id: int
    modelo: str
    matricula: str
    color: str
    usuario: int
    tipo: str
