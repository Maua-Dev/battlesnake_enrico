from src.app.shared.entities.position import Position
from src.app.shared.entities.snake import Snake


class Board:
    height: int
    width: int
    food: list[Position]
    snakes: list[Snake]

    def __init__(self, heigth: int, width: int, food: list[Position], snakes: list[Snake]):
        self.height = heigth
        self.width = width
        self.food = food
        self.snakes = snakes