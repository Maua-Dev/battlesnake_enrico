from src.app.shared.domain.entities.position import Position


def Snake():
    head: Position
    body: list[Position]

    def __init__(self, head: Position, body: list[Position]):
        self.head = head
        self.body = body
        