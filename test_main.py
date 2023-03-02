from main import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    """ Test de la función de prueba"""

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


def test_read_main_game():
    """ Test de la función principal del juego"""

    response = client.post("/", json={
        "player1": {"movimientos": ["D", "DSD", "DSD", "S", "SD"], "golpes": ["K", "P", "K", "", "P"]},
        "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]}
    })
    assert response.status_code == 200
    assert response.json()[-1] == "El ganador es Arnaldor con 1 puntos de vida"


def test_read_main_game_usecase_two():
    """ Test de la función principal del juego con otro caso de uso"""

    response = client.post("/", json={
        "player1": {"movimientos": ["SDD", "DSD", "SA", "DSD"], "golpes": ["K", "P", "K", "P"]},
        "player2": {"movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"], "golpes": ["P", "K", "K", "K", "P", "k"]}
    })
    assert response.status_code == 200
    assert response.json()[-1] == "El ganador es Tonyn con 3 puntos de vida"


def test_read_main_game_usecase_three():
    """ Test de la función principal del juego con otro caso de uso"""

    response = client.post("/", json={
        "player1": {"movimientos": ["DSD", "S"], "golpes": ["P", ""]},
        "player2": {"movimientos": ["", "ASA", "DA", "AAA", "", "SA"], "golpes": ["P", "", "P", "K", "K", "K"]}
    })
    assert response.status_code == 200
    assert response.json()[-1] == "El ganador es Arnaldor con 3 puntos de vida"
