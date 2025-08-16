from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.read_score()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)
        self.show_score()
        self.hideturtle()




    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            self.write_score()

        self.score = 0

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score {self.high_score}", align="center", font=("Arial",24,"normal"))


    def increase_score(self):
        self.score  = self.score +1

    def read_score(self):
        with open("data.txt") as file:
            content = file.read()
            if content is None:
                self.high_score = 0
            self.high_score = content
            self.high_score = int(self.high_score)

    def write_score(self):
        with open("data.txt", mode="w") as file:
            score = self.high_score
            file.write(str(score))
