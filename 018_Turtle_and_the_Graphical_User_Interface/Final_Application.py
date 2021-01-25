import turtle as t
from turtle import Screen
dot_kun = t.Turtle()
import random
import colorgram
t.colormode(255)

colour = colorgram.extract('image.jpg', 25)
dot_kun.speed("fastest")
colours = [(229, 228, 229), (225, 223, 225), (199, 175, 199), (124, 36, 124), (210, 221, 210), (168, 106, 168), (222, 224, 222), (186, 158, 186), (6, 57, 6), (109, 67, 109), (113, 161, 113), (22, 122, 22), (64, 153, 64), (39, 36, 39), (76, 40, 76), (9, 67, 9), (90, 141, 90), (181, 96, 181), (132, 40, 132), (210, 200, 210), (141, 171, 141), (179, 201, 179), (172, 153, 172), (212, 183, 212), (176, 198, 176)]

#Starting Place
x = -500
y = -350
dot_kun.penup()
dot_kun.setx(x)
dot_kun.sety(y)

def movex():
    for n in range(0, 10):
        dot_kun.dot(20, random.choice(colours))
        dot_kun.forward(100)

for n in range(0, 10):
    movex()
    y += 100
    dot_kun.setx(x)
    dot_kun.sety(y)


screen = Screen()
screen.exitonclick()