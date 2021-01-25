import turtle as t
line_kun = t.Turtle()

def dashed():
    line_kun.fd(5)
    line_kun.pu()
    line_kun.fd(5)
    line_kun.pd()

for step in range(50):
    dashed()