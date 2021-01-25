import turtle as t
step_kun = t.Turtle()
import random
t.colormode(255)

angle = [0, 90, 180, 270]

def shade():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pick = (r, g, b)
    return pick

#Forward
def forward():
    step_kun.pensize(5)
    step_kun.speed(10)
    step_kun.color(shade())
    step_kun.forward(10)

stop = False
while stop != True:
    step_kun.left(random.choice(angle))
    forward()