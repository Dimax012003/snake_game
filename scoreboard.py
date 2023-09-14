from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", mode="r") as file:
            str1=str(file.read())
            self.highscore=int(str1)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score} High Score:{self.highscore}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def setscore(self):
        self.score=self.score+1
    def gettext(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.gettext()