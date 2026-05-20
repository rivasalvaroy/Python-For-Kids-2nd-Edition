from tkinter import *


def movetriangle(event):
    canvas.move(1, 5, 0)


tk = Tk()

canvas = Canvas(tk)
canvas.pack()

canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.bind_all('<KeyPress-Return>', movetriangle)

canvas.mainloop()
