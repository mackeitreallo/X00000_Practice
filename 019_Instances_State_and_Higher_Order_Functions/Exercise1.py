from turtle import Turtle, Screen
grr = Turtle()
screen = Screen()

def trigger():
    grr.fd(100)

screen.listen()
screen.onkey(key="a", fun=trigger)
screen.exitonclick()