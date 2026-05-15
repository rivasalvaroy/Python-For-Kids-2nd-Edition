import turtle
import time

t = turtle.Turtle()


def mysquare(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)


mysquare(50)

t.reset()
mysquare(25)
mysquare(50)
mysquare(75)
mysquare(100)
mysquare(125)

t.reset()
t.begin_fill()
mysquare(50)
t.end_fill()

time.sleep(1)
