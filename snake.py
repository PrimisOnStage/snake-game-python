import turtle as t
STARTING_POSITIONS = [0, -20, -40]

class Snake:

    def __init__(self):
        self.seg_list = []
        self.create_snake()

    def create_snake(self):
        for i in range(len(STARTING_POSITIONS)):
            new_seg = t.Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            self.seg_list.append(new_seg)
            new_seg.goto(STARTING_POSITIONS[i], 0)

    def move(self):
        for i in range(len(self.seg_list) - 1, 0, -1):
            self.seg_list[i].goto(self.seg_list[i - 1].xcor(), self.seg_list[i - 1].ycor())

        self.seg_list[0].forward(20)

    def up(self):
        if self.seg_list[0].heading() != 270:
            self.seg_list[0].setheading(90)

    def down(self):
        if self.seg_list[0].heading() != 90:
            self.seg_list[0].setheading(270)

    def right(self):
        if self.seg_list[0].heading() != 180:
            self.seg_list[0].setheading(0)

    def left(self):
        if self.seg_list[0].heading() != 0:
            self.seg_list[0].setheading(180)