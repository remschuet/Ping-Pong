from tkinter import *
from ball import Ball
from player import Player

root = Tk()
root.resizable(False, False)

WIDTH = 600
HEIGHT = 300

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()


ball = Ball("ball", canvas, WIDTH, HEIGHT, 100, 100, root)
player_left = Player(canvas, "player_left", WIDTH, HEIGHT, 30, 150, ball)


root.bind("<Up>", player_left.move_top)
root.bind("<Down>", player_left.move_down)


root.mainloop()
