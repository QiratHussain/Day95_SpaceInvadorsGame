from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape('square')
        self.shapesize(2, 1)
        self.setheading(90)
        self.goto((0, -260))