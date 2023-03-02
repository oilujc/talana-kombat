import random

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List, Tuple, Set


class Player():
    """ Clase base para los jugadores """

    __GENERAL_MOVES: Set[str] = {'A', 'S', 'D', 'W'}
    __ATTACK_WORDS: List[str] = ['conecta un',
                                 'ataca con un', 'lanza un', 'usa un']

    __MOVE_WORDS: Dict[str, str] = {
        'W': 'salta',
        'S': 'se agacha'
    }

    def __init__(self, moves: List[str], hits: List[str]):
        self.energy: int = 6
        self.player_direction: str = None
        self.combinations: Dict[str, Tuple[int, str]] = {}
        self.move_words: Dict[str, str] = {}

        self.moves = self.validate_moves(moves)
        self.hits = self.validate_hits(hits)
        self.data = self.get_combination(moves, hits)

    def set_move_words(self) -> Dict[str, str]:
        """ Retorna un diccionario con las palabras de los movimientos"""
        return {
            **self.__MOVE_WORDS,
            'A': 'avanza' if self.player_direction == 'right' else 'retrocede',
            'D': 'retrocede' if self.player_direction == 'right' else 'avanza'
        }

    def get_combination(self, moves: List[str], hits: List[str]) -> List[Tuple[str, str]]:
        """ Retorna una lista de tuplas con las combinaciones de movimientos y golpes"""
        return list(zip(moves, hits))

    def validate_moves(self, moves: List[str]) -> List[str]:
        """ Valida que los movimientos no sean mayores a 5 caracteres"""
        for move in moves:
            if len(move) > 5:
                raise ValueError(
                    'El movimiento no puede ser mayor a 5 caracteres')
        return moves

    def validate_hits(self, hits: List[str]) -> List[str]:
        """ Valida que los golpes no sean mayores a 1 caracter"""
        for hit in hits:
            if len(hit) > 1:
                raise ValueError('El golpe no puede ser mayor a 1 caracter')
        return hits

    def handle_atack(self, move, atack_name) -> str:
        """ Retorna el mensaje de ataque"""

        atack_word = random.choice(self.__ATTACK_WORDS)

        if move in self.__GENERAL_MOVES:
            move_word = self.move_words[move]

            return f'{self.__class__.__name__} {move_word} y {atack_word} {atack_name}'

        if move in self.combinations:
            return f'{self.__class__.__name__} {atack_word} {atack_name}'

        words = [self.move_words[word] for word in move]

        return f'{self.__class__.__name__} {" y ".join(words)} y {atack_word} {atack_name}'

    def handle_atack_move(self, move: str) -> str:
        """ Retorna el mensaje de ataque con movimiento"""

        if move == '':
            return f'{self.__class__.__name__} se ha quedado sin movimientos'

        words = [self.move_words[word] for word in move]

        return f'{self.__class__.__name__} {" y ".join(words)}'

    def atack(self, current_move: int, target: 'Player') -> str:
        """ Realiza el ataque"""

        if current_move >= len(self.data):
            return self.handle_atack_move('')

        move, hit = self.data[current_move]

        if hit == '':
            return self.handle_atack_move(move)

        if move in self.__GENERAL_MOVES:
            energy, atack_name = self.combinations[hit]

        if f'{move}+{hit}' in self.combinations:
            move = f'{move}+{hit}'
            energy, atack_name = self.combinations[move]

        else:
            energy, atack_name = self.combinations[hit]

        target.energy -= energy
        return self.handle_atack(move, atack_name)


class Tonyn(Player):
    """ Clase para el jugador Tonyn"""

    def __init__(self, moves: List[str], hits: List[str]):
        super().__init__(moves, hits)
        self.player_direction = 'left'
        self.combinations: Dict[str, Tuple[int, str]] = {
            "DSD+P": (3, 'Taladoken'),
            "SD+K": (2, 'Remuyuken'),
            "P": (1, 'Puño'),
            "K": (1, 'Patada')
        }
        self.move_words = self.set_move_words()


class Arnaldor(Player):
    """ Clase para el jugador Arnaldor"""

    def __init__(self, moves: List[str], hits: List[str]):
        super().__init__(moves, hits)
        self.player_direction = 'right'
        self.combinations: Dict[str, Tuple[int, str]] = {
            "SA+K": (3, 'Remuyuken'),
            "ASA+P": (2, 'Taladoken'),
            "P": (1, 'Puño'),
            "K": (1, 'Patada')
        }
        self.move_words = self.set_move_words()


class TalanaKombat:
    """ Clase principal"""

    @classmethod
    def is_player_one_turn(cls, player1: Player, player2: Player) -> bool:
        """ verifica que el jugador 1 ataque primero"""

        if len(player1.data) > len(player2.data):
            return False

        if len(player1.moves) > len(player2.moves):
            return False

        if len(player1.hits) > len(player2.hits):
            return False

        return True

    @classmethod
    def run(cls, players_data: Dict[str, str]) -> None:
        """ Función principal"""

        player1 = Tonyn(players_data['player1']['movimientos'],
                        players_data['player1']['golpes'])
        player2 = Arnaldor(
            players_data['player2']['movimientos'], players_data['player2']['golpes'])

        atacking_player = cls.is_player_one_turn(player1, player2)
        turn, moves = 0, 0
        result = []

        # main loop
        while (turn < len(player1.data) or turn < len(player2.data)):

            if atacking_player == 1:
                result.append(player1.atack(turn, player2))

            else:
                result.append(player2.atack(turn, player1))

            moves = moves + 1

            if moves == 2:
                moves = 0

            atacking_player = not atacking_player

            if moves == 0:
                turn += 1

            if player1.energy <= 0 or player2.energy <= 0:
                break

        winner = player1 if player1.energy > player2.energy else player2
        result.append(
            f'El ganador es {winner.__class__.__name__} con {winner.energy} puntos de vida')

        return result


class PlayerSchema(BaseModel):
    """ Esquema de entrada para el jugador"""

    movimientos: List[str]
    golpes: List[str]


class InputSchema(BaseModel):
    """ Esquema de entrada"""

    player1: PlayerSchema
    player2: PlayerSchema


app = FastAPI()


@app.get("/")
def read_root():
    """ Función de prueba"""

    return {"Hello": "World"}

@app.post("/")
def main_game(body: InputSchema):
    """ Función principal"""

    players_data = body.dict()

    return TalanaKombat.run(players_data)
