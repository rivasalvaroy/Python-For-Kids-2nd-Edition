import turtle
import time

t = turtle.Turtle()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

time.sleep(1)

t.reset()
for x in range(1, 5):
    t.forward(50)
    t.left(90)

time.sleep(1)
