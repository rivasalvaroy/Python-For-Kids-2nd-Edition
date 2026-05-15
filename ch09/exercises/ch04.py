import turtle
import time

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()


t1.forward(100)
t2.right(180)
t2.forward(100)
t3.forward(100)
t4.left(180)
t4.forward(100)


def spiral(t, left):
    f = 100
    for x in range(0, 8):
        if left == True:
            t.left(90)
        else:
            t.right(90)
        t.forward(f)
        if x % 2 != 0:
            f -= 20


spiral(t1, True)
spiral(t2, False)
spiral(t3, False)
spiral(t4, True)

time.sleep(1)
