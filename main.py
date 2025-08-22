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

#make wall
wall_maker = t.Turtle()
wall_maker.hideturtle()
wall_maker.color("white")
wall_maker.penup()
wall_maker.goto(280,280)
wall_maker.setheading(180)
wall_maker.pendown()
for _ in range(4):
    wall_maker.forward(560)
    wall_maker.left(90)

#playing game
game = True
while game:
    if snake.seg_list[0].distance(f) < 15:
        print("nom, nom, nom")
        score.score_up()
        score.refresh()
        f.refresh()
        snake.extend()

    for seg in snake.seg_list[1:]:

        if snake.seg_list[0].distance(seg) < 10:
            score.reset()
            snake.reset()

    if snake.seg_list[0].xcor() >= 280 or snake.seg_list[0].ycor() >= 280 or snake.seg_list[0].xcor() <= -280 or snake.seg_list[0].ycor() <= -280:
        score.reset()
        snake.reset()


    sc.update()
    time.sleep(0.1)
    snake.move()














sc.exitonclick()