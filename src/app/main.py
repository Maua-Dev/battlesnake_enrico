import random
from fastapi import FastAPI
from mangum import Mangum
from shared.entities.board import Board
from shared.entities.movement import Movement
from shared.entities.position import Position
from shared.entities.snake import Snake



app = FastAPI()

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
def move(request: dict):
    board = Board.fromJson(request)
    my_snake = Snake.fromJson(request)
    movimentation = Movement(my_snake, board)

    return movimentation.eat()


@app.post("/end")
def move():
    return


handler = Mangum(app, lifespan="off")
