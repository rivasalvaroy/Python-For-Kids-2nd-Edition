from tkinter import *
import random
import time
import sys


class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

    def change_color(self):
        colors = ['yellow', 'red', 'blue',
                  'green', 'orange', 'black', 'purple']
        self.canvas.itemconfig(ball.id, fill=random.choice(colors))
        self.canvas.itemconfig(self.paddle.id, fill=random.choice(colors))

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.y * -1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = self.y * -1
            self.change_color()
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = self.x * -1


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def start_game(self, evt):
        self.started = True


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


tk = Tk()

tk.title("Bounce Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, 'black')
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, score, 'green')
game_over_text = canvas.create_text(
    250, 200, text='GAME OVER', state='hidden')


while True:
    if ball.hit_bottom == False:
        if paddle.started == True:
            ball.draw()
            paddle.draw()
    else:
        canvas.itemconfig(game_over_text, state='normal')
        for i in range(0, 5):
            canvas.config(background='red')
            tk.update()
            time.sleep(0.25)
            canvas.config(background='white')
            tk.update()
            time.sleep(0.25)
        sys.exit()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
