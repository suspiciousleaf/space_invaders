from turtle import Turtle, register_shape

MOVE_DISTANCE = 7

controller = "icons\\controller.gif"

register_shape(controller)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
        self.right_move = False
        self.left_move = False

    def create_player(self):
        self.penup()
        self.speed("fastest")
        self.setpos(0, -250)
        self.shape(controller)

    def left(self):
        if self.xcor() > -350:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def right(self):
        if self.xcor() < 350:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def right_on(self):
        self.right_move = True

    def right_off(self):
        self.right_move = False

    def left_on(self):
        self.left_move = True

    def left_off(self):
        self.left_move = False

    def get_x_coordinate(self):
        return self.xcor()
