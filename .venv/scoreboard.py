from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        global score
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.high_score = 0
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        # self.goto(0, 0)
        # self.write("GAME OVER", align=ALIGNMENT, font=FONT)