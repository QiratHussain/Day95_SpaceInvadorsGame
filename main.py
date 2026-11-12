from turtle import Screen
from players import Player, Brick, Enemy
import time
import random

BRICKS_POSITIONS= [(275, 0),(250,0), (225,0),(200,0),(175,0), (150,0),(125,0),(100,0),(75,0),(50,0),(25,0),(0,0),
(-275, 0),(-250,0), (-225,0),(-200,0),(-175,0), (-150,0),(-125,0),(-100,0),(-75,0),(-50,0),(-25,0)]
ENEMY_POSITIONS= [(+50,+260),(0,+260),(-50,+260)]
GAME_ON= True
# -------------------------- SCREEN -----------------------------
screen= Screen()
# screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.listen()

# -------------------------- PLAYERS -----------------------------
mainlead= Player()
enemies= []

bricks = [Brick(position=p) for p in BRICKS_POSITIONS]  
bombs = []

for positions in ENEMY_POSITIONS:
    enemy= Enemy(position= positions)
    enemies.append(enemy)

# -------------------------- MOVEMENTS -----------------------------
screen.onkey(mainlead.move_left,'f')
screen.onkey(mainlead.move_right,'j')

step = 10
while GAME_ON:
    screen.update()
    time.sleep(0.1)
    # check the whole group first
    if any(e.xcor() + step > 200 or e.xcor() + step < -200 for e in enemies):
        step *= -1
    for e in enemies:
        e.move(step)

    if len(bombs) < 5 and random.random() < 0.1:
        bombs.append(random.choice(enemies).bomb())

    for bomb in bombs[:]:               # iterate over a copy, since we remove inside the loop
        bomb.move()
        destroyed = False

        # TODO 6: bomb destroys a brick
        for brick in bricks[:]:
            if bomb.distance(brick) < 25:
                brick.hideturtle()
                bricks.remove(brick)
                destroyed = True
                break

        # TODO 7: bomb hits the player
        if not destroyed and bomb.distance(mainlead) < 25:
            mainlead.hideturtle()
            GAME_ON = False
            destroyed = True

        # bomb left the screen
        if bomb.ycor() < -290:
            destroyed = True

        if destroyed:
            bomb.hideturtle()
            bombs.remove(bomb)



screen.exitonclick()