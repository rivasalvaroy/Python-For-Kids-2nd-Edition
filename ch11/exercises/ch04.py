from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        random_x = random.randrange(0, 485)
        random_y = random.randrange(0, 200)
        self.canvas.move(self.id, random_x, random_y)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def change_color(self):
        self.canvas.itemconfig(ball.id, fill=random.choice(
            ['yellow', 'red', 'blue', 'green', 'orange', 'black', 'white', 'purple']))

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

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 'purple')

while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
