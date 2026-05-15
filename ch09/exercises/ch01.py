import turtle
import time

t = turtle.Turtle()


def octagon(size):
    for x in range(1, 9):
        t.forward(size)
        t.right(45)


octagon(100)

time.sleep(1)
