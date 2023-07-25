from shared.entities.position import Position
from shared.entities.snake import Snake


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

    @staticmethod
    def fromJson(self, json: dict):
        snakes_list = []
        for snake in json["board"]["snakes"]:
            position_list = []
            for body_position in snake["body"]:
                position_list.append(Position(body_position["x"], body_position["y"]))
            snakes_list.append(Snake(Position(snake["head"]["x"], snake["head"]["y"]), position_list))

        food_list = []
        for food in json["board"]["food"]:
            food_list.append(Position(food["x"], food["y"]))

        return Board(
            json["board"]["height"],
            json["board"]["width"],
            food_list,
            snakes_list,
        )