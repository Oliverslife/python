from turtle import Turtle

FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 260)
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
