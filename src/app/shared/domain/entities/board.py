from src.app.shared.domain.entities.position import Position
from src.app.shared.domain.entities.snake import Snake


def Board():
    height: int
    width: int
    food: list[Position]
    snakes: list[Snake]