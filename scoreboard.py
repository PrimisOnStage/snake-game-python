from turtle import Turtle
with open("data.txt", "r") as file:
    data = file.read()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.highscore = int(data)
        self.score = 0
        self.goto(0,270)
        self.refresh()

    def score_up(self):
        self.score += 1

    def refresh(self):
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", align="center", font=("Arial", 24, "bold"))

    def reset(self):
        self.score = 0
        self.refresh()
        with open("data.txt", "w") as file:
            file.write(str(self.highscore))


#Functions not used in main
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 24, "bold"))


