import random
from fastapi import FastAPI
from mangum import Mangum
from src.app.shared.entities.board import Board
from src.app.shared.entities.movement import Movement
from src.app.shared.entities.position import Position
from src.app.shared.entities.snake import Snake



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
