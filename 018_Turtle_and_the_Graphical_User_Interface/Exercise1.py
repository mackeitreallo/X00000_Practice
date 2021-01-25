from turtle import Turtle, Screen

testing_turtle = Turtle()
testing_turtle.shape("turtle")
testing_turtle.color("blue")
testing_turtle.fd(200)


#Should always be at the end for the screen not to close
screen = Screen()
screen.exitonclick()