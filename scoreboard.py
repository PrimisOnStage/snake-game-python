from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.highscore = 0
        self.score = 0
        self.goto(0,270)
        self.refresh()

    def score_up(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score} ", False, align="center")

    def reset(self):
        if self.score > self.highscore:
            self.score = self.score
        self.score = 0
        self.refresh()


#Functions not used in main
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 24, "bold"))


