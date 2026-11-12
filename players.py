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

    def move_left(self):
        self.goto((self.xcor()-10, self.ycor()))

    def move_right(self):
        self.goto((self.xcor()+10, self.ycor()))

class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("green")
        self.penup()
        self.shape('square')
        self.shapesize(2, 1)
        self.goto(position)

class Enemy(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("red")
        self.penup()
        self.setheading(90)
        self.shape('square')
        self.shapesize(2, 1)
        self.goto(position)