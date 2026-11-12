from turtle import Screen
from players import Player, Brick

BRICKS_POSITIONS= [(275, 0),(250,0), (225,0),(200,0),(175,0), (150,0),(125,0),(100,0),(75,0),(50,0),(25,0),(0,0),
(-275, 0),(-250,0), (-225,0),(-200,0),(-175,0), (-150,0),(-125,0),(-100,0),(-75,0),(-50,0),(-25,0)]

# -------------------------- SCREEN -----------------------------
screen= Screen()
# screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.listen()

# -------------------------- PLAYERS -----------------------------
mainlead= Player()
for positions in BRICKS_POSITIONS:
    Brick(position= positions)

# TODO: 3. create boundary
# TODO: 4. create enemy ships
# TODO: 5. create bombing function
# TODO: 6. remove the boundary when bomb strikes
# TODO: 7. remove the player turtle when bomb strikes

screen.exitonclick()