from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def change_color(self):
        colors = random.sample(
            ['yellow', 'red', 'blue', 'green', 'orange', 'black', 'white', 'purple'], 2)
        self.canvas.itemconfig(ball.id, fill=colors[0])
        self.canvas.config(background=colors[1])

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
            self.change_color()
        if pos[3] >= self.canvas_height:
            self.y = -3
            self.change_color()
        if pos[0] <= 0:
            self.x = 3
            self.change_color()
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.change_color()


tk = Tk()

tk.title("Bounce Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0,
                highlightthickness=0, background='orange')
canvas.pack()
tk.update()

ball = Ball(canvas, 'purple')

while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
