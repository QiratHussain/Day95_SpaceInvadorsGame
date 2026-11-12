from turtle import Screen
from players import Player

# -------------------------- SCREEN -----------------------------
screen= Screen()
# screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.listen()

# -------------------------- PLAYERS -----------------------------
mainlead= Player()

# TODO: 3. create boundary
# TODO: 4. create enemy ships
# TODO: 5. create bombing function
# TODO: 6. remove the boundary when bomb strikes
# TODO: 7. remove the player turtle when bomb strikes
screen.exitonclick()