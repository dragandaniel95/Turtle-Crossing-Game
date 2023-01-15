from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)
        self.goto(-150, 0)
        self.write("☠️Game Over! ☠️", align="left", font=FONT)
