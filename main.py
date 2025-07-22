import turtle as t
import time

#setting up snake
import snake as s
snake = s.Snake()


#Screen Setup
sc = t.Screen()
sc.setup(600,600)
sc.bgcolor("black")
sc.tracer(0)

#setup screen listening
sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")



#playing game
game = True
while game:
    sc.update()
    time.sleep(0.1)
    snake.move()














sc.exitonclick()