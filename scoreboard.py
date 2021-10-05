from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.score_counting()

    def score_counting(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.net_line()

    def net_line(self):
        self.setheading(90)
        self.color("white")
        self.hideturtle()
        for line in range(0, 6):
            self.pensize(width=5)
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()
        self.setheading(270)
        self.color("white")
        self.penup()
        self.forward(270)
        for line in range(0, 6):
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()
