import turtle as t
import time
from food import Food


#setting up snake
import snake as s
snake = s.Snake()

#food
f = Food()

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
score = 0
while game:
    if snake.seg_list[0].distance(f) < 15:
        print("nom, nom, nom")

        score+=1
        f.refresh()

    sc.update()
    time.sleep(0.1)
    snake.move()














sc.exitonclick()