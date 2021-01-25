from turtle import Turtle, Screen

square_kun = Turtle()

def walk_forward():
    square_kun.fd(100)
    square_kun.left(90)

walk_forward()
walk_forward()
walk_forward()
walk_forward()

screen = Screen()
screen.exitonclick()