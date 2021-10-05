from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle()
        self.goto(position)

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

#
# class SecondPaddle(Paddle):
#     def __init__(self):
#         super().__init__()
#
#     def create_paddle(self):
#         super().create_paddle()
#         self.goto(-350, 0)
