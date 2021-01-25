import turtle as t
round_kun = t.Turtle()
import random
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pick = (r, g, b)
    return pick

def draw(offset):
    for n in range(int(360/offset)):
        round_kun.speed("fastest")
        round_kun.color(random_colour())
        round_kun.circle(100)
        round_kun.setheading(round_kun.heading() + offset)

draw(2)

