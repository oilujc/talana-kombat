from typing import Dict
from player import Player, Arnaldor, Tonyn

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


