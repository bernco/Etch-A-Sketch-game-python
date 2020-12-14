from turtle import Turtle, Screen

tom = Turtle()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def move_left():
    tom.left(10)


def move_right():
    tom.right(10)


def clear_drawing():
    tom.clear()
    tom.pu()
    tom.home()
    tom.pd()


my_screen = Screen()
my_screen.listen()
my_screen.onkeypress(key='w', fun=move_forward)
my_screen.onkeypress(key='s', fun=move_backward)
my_screen.onkeypress(key='a', fun=move_left)
my_screen.onkeypress(key='d', fun=move_right)
my_screen.onkeypress(key='c', fun=clear_drawing)
my_screen.exitonclick()
