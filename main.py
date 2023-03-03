from fastapi import FastAPI
from talana_kombat import TalanaKombat
from schemas import InputSchema

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
