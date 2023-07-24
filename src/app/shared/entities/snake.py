from app.shared.entities.position import Position


class Snake:
    head: Position
    body: list[Position]
    health: int

    def __init__(self, head: Position, body: list[Position], health: int):
        self.head = head
        self.body = body
        self.health = health
    
    @staticmethod
    def fromJson(self, json: dict):
        position_list = []
        for body_position in json["you"]["body"]:
            position_list.append(Position(body_position["x"], body_position["y"]))
        return Snake(Position(json["you"]["head"]["x"], json["you"]["head"]["y"]), position_list, json["you"]["health"])
    