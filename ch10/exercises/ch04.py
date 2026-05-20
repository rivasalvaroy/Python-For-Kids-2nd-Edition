import time
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=660, height=630)
canvas.pack()

myimage = PhotoImage(file='./images/python.gif')
canvas.create_image(0, 0, anchor=NW, image=myimage)

for x in range(0, 35):
    canvas.move(1, 10, 10)
    tk.update()
    time.sleep(0.05)

canvas.mainloop()
