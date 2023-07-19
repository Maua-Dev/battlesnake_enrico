from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# TODO: Implement my logic here to handle the requests from Battlesnake


@app.get("/")
def customization():
    return {
        "apiversion": "1",
        "color": "#ff3399",
        "head": "beluga",
        "tail": "curled",
    }


@app.post("/start")
def start():
    return {

    }


@app.post("/move")
def move():
    return {
        "move": "up",
        "shout": "Moving up!"
    }


@app.post("/end")
def move():
    return {
    }


handler = Mangum(app, lifespan="off")
