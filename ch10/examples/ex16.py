from tkinter import colorchooser, Canvas, Tk
from random import randrange

c = colorchooser.askcolor()

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()


def random_rectangle(width, height, fill_color):
    x1 = randrange(width)
    y1 = randrange(height)
    x2 = x1 + randrange(width)
    y2 = y1 + randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)


random_rectangle(400, 400, c[1])

canvas.mainloop()
