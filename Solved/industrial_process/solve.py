#!/usr/bin/env python3
from tkinter import *

# Prepare canvas to draw coordinate points
root = Tk()
root.title("INSHACK 2019")
cw = 1000  # canvas width
ch = 400  # canvas height
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.grid(row=0, column=1)

# Draw coordinates
with open("registers.txt", "r") as f:
    register_list = f.readlines()

# Parameters
offset = 10
scale = 0.03

# Draw canvas
prevX = -1
prevY = -1
prevPiece = -1
for each in register_list:
    # extract register
    reg = each.split(',')
    x_axis = int(reg[0])
    y_axis = int(reg[1])
    piece = int(reg[2])

    # scale the axis
    drawX = (x_axis + piece * 1100) * scale
    drawY = (y_axis) * scale

    # invert y-axis
    drawY = (1000*scale) - drawY

    # padding
    drawX += offset
    drawY += offset

    # if first line, make it a point
    if prevPiece != piece:
        prevX = drawX
        prevY = drawY

    # draw lines
    canvas_1.create_line(prevX, prevY, drawX, drawY, smooth="true")
    prevX = drawX
    prevY = drawY
    prevPiece = piece

# Show frame
root.mainloop()
