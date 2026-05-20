from tkinter import *
import time


def hello():
    print('hello there')


tk = Tk()

btn = Button(tk, text="click me", command=hello)
btn.pack()
btn.mainloop()

time.sleep(1)
