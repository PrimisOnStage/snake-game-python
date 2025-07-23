import turtle as t
import time
from food import Food
from scoreboard import ScoreBoard


#setting up snake
import snake as s
snake = s.Snake()


#Screen Setup
sc = t.Screen()
sc.setup(600,600)
sc.bgcolor("black")
sc.tracer(0)

#food
f = Food()
score = ScoreBoard()


#setup screen listening
sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")


#playing game
game = True
while game:
    if snake.seg_list[0].distance(f) < 15:
        print("nom, nom, nom")
        score.score_up()
        score.refresh()
        f.refresh()

    sc.update()
    time.sleep(0.1)
    snake.move()














sc.exitonclick()