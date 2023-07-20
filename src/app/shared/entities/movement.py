from math import sqrt
from src.app.shared.entities.board import Board
from src.app.shared.entities.position import Position
from src.app.shared.entities.snake import Snake


class Movement():
    snake: Snake
    board: Board

    def __init__(self, snake: Snake, board: Board):
        self.snake = snake
        self.board = board
    
    def direction(position: Position):
        if(position.x > 0):
            return {"move": "right"}
        elif(position.x < 0):
            return {"move": "left"}
        elif(position.y > 0):
            return {"move": "up"}
        elif(position.y < 0):
            return {"move": "down"}
        
    def move(self):
        moveUp = False
        moveDown = False
        moveRight = False
        moveLeft = False
        for snake in self.board.snakes:
            for body in self.bord.snake.body:
                if(self.snake.head.x - body.x >= 3 ):
                    moveRight = True
                else:
                    moveRight = False
                if(self.snake.head.x - body.x <= -3 ):
                    moveLeft = True
                else:
                    moveLeft = False
                if(self.snake.head.y - body.y >= 3 ):
                    moveUp = True
                else:
                    moveUp = False
                if(self.snake.head.y - body.y <= -3 ):
                    moveDown = True
                else:
                    moveDown = False

            if(self.snake.head.x - self.board.snake.head.x >= 3 ):
                moveRight = True
            else:
                moveRight = False
            if(self.snake.head.x - self.board.snake.head.x <= -3 ):
                moveLeft = True
            else:
                moveLeft = False
            if(self.snake.head.y - self.board.snake.head.y >= 3 ):
                moveUp = True
            else:
                moveUp = False
            if(self.snake.head.y - self.board.snake.head.y <= -3 ):
                moveDown = True
            else:
                moveDown = False
        
        

        if(moveUp):
            return {"move": "up"}
        elif(moveDown):
            return {"move": "down"}
        elif(moveRight):
            return {"move": "right"}
        elif(moveLeft):
            return {"move": "left"}
        
        self.eat()
            
    def distance(initial: Position, final: Position):
        return sqrt((final.x - initial.x)**2 + (final.y - final.x)**2)
        
    def eat(self):
        closest_food = self.board.food[0]
        for food in self.board.food:
            if(self.distance(food, self.snake.head) < self.distance(closest_food, self.snake.head)):
                closest_food = food
        for snake in self.board.snakes:
            if(self.distance(closest_food, snake.head) > self.distance(self.snake.head, closest_food)):
                self.move(Position(food.x - self.snake.head.x, food.y - self.snake.head.y))
        

