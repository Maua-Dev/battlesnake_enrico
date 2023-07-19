from src.app.shared.domain.entities.position import Position
from src.app.shared.domain.entities.snake import Snake


def Board():
    height: int
    width: int
    food: list[Position]
    snakes: list[Snake]

    def __init__(self, heigth: int, width: int, food: list[Position], snakes: list[Snake]):
        self.height = heigth
        self.width = width
        self.food = food
        self.snakes = snakes