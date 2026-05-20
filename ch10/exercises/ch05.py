from tkinter import *
import time
import random

tk = Tk()

canvas = Canvas(tk, width=800, height=800)
canvas.pack()

myimage = PhotoImage(file='./images/python.gif')

for x in range(0, 100):
    p1 = random.randrange(800)
    p2 = random.randrange(800)
    canvas.create_image(p1, p2, anchor=NW, image=myimage)
    tk.update()
    time.sleep(0.2)

canvas.mainloop()
