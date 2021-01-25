from turtle import Turtle
step_kun = Turtle()
import random

colour = ["red", "blue", "green", "yellow", "black"]
angle = [0, 90, 180, 270]

#Forward
def forward():
    step_kun.pensize(5)
    step_kun.speed(10)
    step_kun.color(random.choice(colour))
    step_kun.forward(10)

stop = False
while stop != True:
    step_kun.left(random.choice(angle))
    forward()