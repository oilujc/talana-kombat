from typing import List
from pydantic import BaseModel, validator

class PlayerSchema(BaseModel):
    """ Esquema de entrada para el jugador"""

    movimientos: List[str]
    golpes: List[str]

    @validator('movimientos')
    def validate_moves(cls, v):
        """ Valida que los movimientos no sean mayores a 5 caracteres"""
        for move in v:
            if len(move) > 5:
                raise ValueError(
                    f'El movimiento no puede ser mayor a 5 caracteres {move}')
            
        return v

    @validator('golpes')
    def validate_hits(cls, v):
        """ Valida que los golpes no sean mayores a 1 caracter"""
        for hit in v:
            if len(hit) > 1:
                raise ValueError(f'El golpe no puede ser mayor a 1 caracter {hit}')
        return v


class InputSchema(BaseModel):
    """ Esquema de entrada"""

    player1: PlayerSchema
    player2: PlayerSchema