import turtle as t
import time

#Screen Setup
sc = t.Screen()
sc.setup(600,600)
sc.bgcolor("black")


#turtle setup
head = t.Turtle("square")
head.color("white")
head.penup()
seg_list = [head]
seg_loc = [-20, -40]

for i in range(2):
    new_seg = t.Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    seg_list.append(new_seg)
    new_seg.goto(seg_loc[i],0)

def add_seg():
    new_seg = t.Turtle("square")
    new_seg.color("white")
    seg_list.insert(0,new_seg)

sc.tracer(0)
game = True
while game:

    for i in range(1, len(seg_list)):
        seg_list[i].goto(seg_list[i-1].xcor(), seg_list[i-1].ycor())
        seg_list[0].forward(10)

    time.sleep(0.1)
    sc.update()
















sc.exitonclick()