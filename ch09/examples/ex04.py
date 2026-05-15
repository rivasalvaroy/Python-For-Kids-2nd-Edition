import turtle
import time

t = turtle.Turtle()


def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


# green
mycircle(0, 1, 0)
# darker green
mycircle(0, 0.5, 0)

mycircle(1, 0, 0)

mycircle(0.5, 0, 0)

mycircle(0, 0, 1)

mycircle(0, 0, 0.5)
# gold
mycircle(0.9, 0.75, 0)
# light pink
mycircle(1, 0.7, 0.75)
# two different shades of orange
mycircle(1, 0.5, 0)
mycircle(0.9, 0.5, 0.15)
# black
mycircle(0, 0, 0)
# white
mycircle(1, 1, 1)

time.sleep(1)
