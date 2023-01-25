from turtle import Turtle
class Paddle(Turtle) :

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5.1, 1.0)
        self.penup()
        self.setposition(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_dw(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

