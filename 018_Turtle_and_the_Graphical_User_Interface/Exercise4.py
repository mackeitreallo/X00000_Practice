import turtle as t
line_kun = t.Turtle()

angle = float(360)
#triangle
def shape(angle, sides):
    n = angle / sides
    degree = 360
    for draw in range(sides):
        line_kun.fd(100)
        line_kun.right(n)

for sides in range(3,10):
    shape(angle, sides)
    sides += 1
