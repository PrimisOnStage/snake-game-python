from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.score = 0
        self.goto(0,270)
        self.refresh()

    def score_up(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score} ", False, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 24, "bold"))


