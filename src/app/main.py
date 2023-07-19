from logging import handlers
from fastapi import FastAPI
from fastapi import request
from mangum import Mangum

app = FastAPI()

# TODO: Implement my logic here to handle the requests from Battlesnake


@app.get("/")
def get():
    return {
        "apiversion": "1",
        "color": "#ff3399",
        "head": "beluga",
        "tail": "curled",
    }


@app.post("/start")
def start():
    return


@app.post("/move")
def move():
    game_state = request.get_json()
    return handlers["move"](game_state)


@app.post("/end")
def move():
    return


handler = Mangum(app, lifespan="off")
