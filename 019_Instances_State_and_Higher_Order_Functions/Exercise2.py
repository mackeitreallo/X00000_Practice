from turtle import Turtle, Screen
cursor = Turtle()
screen = Screen()

cursor.shape()

def reset():
    cursor.clear()
    cursor.reset()

def btn_up():
    cursor.fd(5)

def btn_down():
    cursor.back(5)

def btn_left():
    head = cursor.heading() + 5
    cursor.setheading(head)

def btn_right():
    head = cursor.heading() - 5
    cursor.setheading(head)

screen.listen()
screen.onkey(btn_up, "w")
screen.onkey(btn_down, "s")
screen.onkey(btn_left, "a")
screen.onkey(btn_right, "d")
screen.onkey(reset, "c")
screen.exitonclick()