from tkinter import *
from ball import Ball
from player import Player
from points import Point


root = Tk()
root.resizable(False, False)

WIDTH = 600
HEIGHT = 300

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

points_left = Point(canvas, "points_left", 200, 20, 0)
points_right = Point(canvas, "points_right", 400, 20, 0)
ball = Ball("ball", canvas, WIDTH, HEIGHT, 30, 30, 70, 70, root, points_left, points_right)

player_left = Player(canvas, "player_left", 10, 10, 20, 60, ball)
player_right = Player(canvas, "player_right", 580, 180, 590, 230, ball)


root.bind("<Up>", player_right.move_top)
root.bind("<Down>", player_right.move_down)

root.bind("<w>", player_left.move_top)
root.bind("s", player_left.move_down)

root.mainloop()
