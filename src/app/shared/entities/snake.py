from src.app.shared.entities.position import Position


class Snake:
    head: Position
    body: list[Position]

    def __init__(self, head: Position, body: list[Position]):
        self.head = head
        self.body = body
        