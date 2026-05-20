from tkinter import Canvas, Tk
from random import randrange

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()


def random_rectangle(width, height):
    x1 = randrange(width)
    y1 = randrange(height)
    x2 = x1 + randrange(width)
    y2 = y1 + randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)


random_rectangle(400, 400)

canvas.mainloop()
