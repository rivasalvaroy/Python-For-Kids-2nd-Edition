import turtle
import time

t = turtle.Turtle()

# An equilateral triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
time.sleep(1)
t.reset()

# An isosceles triangle
t.forward(50)
t.left(104.47751218592992)
t.forward(100)
t.left(151.04497562814015)
t.forward(100)
t.left(104.47751218592992)
time.sleep(1)
t.reset()

# Right scalene triangle
t.forward(100)
t.left(149)
t.forward(117)
t.left(119)
t.forward(60)
time.sleep(1)
t.reset()

# Obtuse scalene triangle
t.forward(100)
t.left(153.9)
t.forward(131)
t.left(133.1)
t.forward(60)
time.sleep(1)
t.reset()

# Acute scalene triangle
t.forward(100)
t.left(144)
t.forward(93)
t.left(101.2)
t.forward(60)

time.sleep(1)
