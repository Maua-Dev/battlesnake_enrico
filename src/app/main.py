import random
from fastapi import FastAPI
from mangum import Mangum
from src.app.shared.entities.board import Board
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
    snakes_list = []
    for snake in request["board"]["snakes"]:
        position_list = []
        for body_position in snake["body"]:
            position_list.append(Position(body_position["x"], body_position["y"]))
    snakes_list.append(Snake(Position(snake["head"]["x"], snake["head"]["y"]), position_list))

    food_list = []
    for food in request["board"]["food"]:
        food_list.append(Position(food["x"], food["y"]))

    my_position_list = []
    for my_body_position in snake["you"]["body"]:
        my_position_list.append(Position(my_body_position["x"], my_body_position["y"]))

    board = Board(
        request["board"]["height"],
        request["board"]["width"],
        food_list,
        snakes_list,
    )

    my_snake = Snake(
        Position(request["you"]["head"]["x"], request["you"]["head"]["y"]),
        my_position_list,
    )




    return {"move": 'up'}


@app.post("/end")
def move():
    return


handler = Mangum(app, lifespan="off")
