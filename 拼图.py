import turtle
from PIL import Image
import random

images = []

img = Image.open("picture.gif")

width, height = img.size

w, h = width / 4, height / 4

for i in range(4):
	for j in range(4):
		images.append(img.crop((j*w, i*h, (j+1)*w, (i+1)*h)))


numbers = list(range(16))
random.shuffle(numbers)

tiles = { }

board = [["#" for _ in range(4)] for _ in range(4)]

def initialize():
    r, c = 0, 0
    for i in range(16):
        tiles[(r, c)] = numbers[i]
        c += 1
        if c >= 4:
            r, c = r+1, 0

def is_adjacent(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2) == 1

def draw():
	all_turtles = screen.turtles()
	for t in all_turtles:
		if t.isvisible():
			t.hideturtle()
	screen.tracer(False)
	for r in range(4):
		for c in range(4):
			tile = turtle.Turtle(images[tiles[(r, c)]])
			tile.penup()
			board[r][c] = tile
	for r in range(4):
		for c in range(4):
			tile = board[r][c]
			tile.showturtle()
			tile.goto(-300 + c * 200, 300 - r * 200)
	screen.tracer(True)

def click(x, y):
	r, c = (400 - y) // 200, (x + 400) // 200
	for i in range(4):
		for j in range(4):
			if tiles[(i,j)] == 15:
				if is_adjacent(i, j, r, c):
					tiles[(i, j)] = tiles[(r, c)]
					tiles[(r, c)] = 15
				draw()
				return

screen = turtle.Screen()
screen.setup(800, 800, 0, 0)
screen.tracer(False)
for i in range(16):
	screen.addshape(images[i])
initialize()
screen.onscreenclick(click)
draw()
turtle.done()
