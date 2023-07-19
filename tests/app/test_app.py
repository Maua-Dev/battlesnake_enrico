from src.app.main import get, move


class Test_App:
    def test_get(self):
        resp = get()

        assert resp == {
            "apiversion": "1",
            "color": "#ff3399",
            "head": "beluga",
            "tail": "curled",
        }

    def move(self):
        resp = move()

        assert resp == {
            "move": "up",
            "shout": "Moving up!"
        }
