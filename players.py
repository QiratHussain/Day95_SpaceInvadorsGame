from turtle import Turtle
STEP= 10
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
        
    def move(self, step):
        self.goto(self.xcor() + step, self.ycor())
    
    def bomb(self):
        """Create a bomb just below this enemy and return it."""
        return Bomb((self.xcor(), self.ycor() - 25))

class Bomb(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.shapesize(0.6, 0.6)
        self.penup()
        self.setheading(270)    
        self.goto(position)

    def move(self):
        self.forward(15)
