import random
from fastapi import FastAPI
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
    possible_moves = ["up", "down", "left", "right"]    
    move = random.choice(possible_moves)
    return {
        "move": move,
        "shout": "Moving up!"
    }


@app.post("/end")
def move():
    return


handler = Mangum(app, lifespan="off")
