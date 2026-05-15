import turtle
import time

t = turtle.Turtle()


def draw_star(size, points):
    angle = 360/points
    for x in range(0, points):
        t.forward(size)
        t.left(180-angle)
        t.forward(size)
        t.right(180 - (angle*2))


draw_star(80, 70)

time.sleep(1)
