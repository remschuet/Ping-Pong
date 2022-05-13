from tkinter import *
from ball import Ball
from player import Player

root = Tk()
root.resizable(False, False)

WIDTH = 600
HEIGHT = 300

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()


ball = Ball("ball", canvas, WIDTH, HEIGHT, 10, 10, 50, 50, root)
player_left = Player(canvas, "player_left", 10, 10, 20, 60, ball)
#player_right = Player(canvas, "player_right", 580, 180, 590, 230, ball)


root.bind("<Up>", player_left.move_top)
root.bind("<Down>", player_left.move_down)

#root.bind("<w>", player_right.move_top)
#root.bind("s", player_right.move_down)


root.mainloop()
