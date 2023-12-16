from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(-300, 250)
        self.speed("fastest")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score:2}", align="center", font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align="center", font=("courier", 36, "bold"))
