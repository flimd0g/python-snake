from turtle import Turtle
score = 0
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
        self.increase_score()

    def increase_score(self):
        global score
        self.write(f"Score: {score}", False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        global score
        self.clear()
        score += 1
        self.increase_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)