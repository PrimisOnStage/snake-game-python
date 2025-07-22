import turtle as t

class Snake:

    def __init__(self):
        head = t.Turtle("square")
        head.color("white")
        head.penup()
        self.seg_list = [head]
        self.seg_loc = [-20, -40]

        for i in range(2):
            new_seg = t.Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            self.seg_list.append(new_seg)
            new_seg.goto(self.seg_loc[i], 0)

    def move(self):
        for i in range(len(self.seg_list) - 1, 0, -1):
            self.seg_list[i].goto(self.seg_list[i - 1].xcor(), self.seg_list[i - 1].ycor())

        self.seg_list[0].forward(20)