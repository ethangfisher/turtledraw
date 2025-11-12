import turtle
import math

file = open("line-data.txt", "r")

window = turtle.Screen()
window.setup(width=450, height=450)
window.title("Turtle Draw")
window.bgcolor("white")

turtleDraw = turtle.Turtle()
turtleDraw.hideturtle()                    # hide while moving/drawing for neatness
turtleDraw.speed(0)                        # maximum speed
turtleDraw.penup()                         # start with pen up (so origin->first point not drawn)
turtleDraw.showturtle()

fname = input("Enter input filename: ").strip()
try:
    infile = open(fname, "r")
except Exception as e:
    print(f"Error opening file '{fname}': {e}")
    'return'

total_distance = 0.0
prev_point = None   # holds (x, y) of previous connected point when pen is down
pen_down = False

    # Read file line by line (for loop), strip whitespace, split into pieces
for line in file:
    raw = line.strip()
    if raw == "":
        continue
    parts = raw.split()

        # detect 'stop' lines (line that contains just the word stop)
    if parts[0].lower() == "stop":
        # lift pen, mark disconnected (prev_point reset)
        turtleDraw.penup()
        pen_down = False
        prev_point = None
        continue

        # non-stop: expected format: color x y
    if len(parts) < 3:
        # malformed line - skip (or could warn)
        print(f"Skipping malformed line: {raw}")
        continue

    color = parts[0]
    try:
        x = float(parts[1])
        y = float(parts[2])
    except ValueError:
        print(f"Skipping line with non-numeric coords: {raw}")
        continue

        # Change color before moving/drawing
    try:
        turtleDraw.pencolor(color)
    except Exception:
            # if color invalid, fall back to black but keep going
        turtleDraw.pencolor("black")
    if prev_point is None:
        turtleDraw.penup()
        turtleDraw.goto(x, y)
            # prepare to draw the next connection from this point
        turtleDraw.pendown()
        pen_down = True
        prev_point = (x, y)
    else:
            # We have a previous point in the same connected run: draw from prev_point to (x,y)
        if not pen_down:
            turtleDraw.pendown()
            pen_down = True
            # compute distance from prev_point to current
        dx = x - prev_point[0]
        dy = y - prev_point[1]
        dist = math.hypot(dx, dy)
        total_distance += dist
            # move (drawing a line)
        turtleDraw.goto(x, y)
        prev_point = (x, y)
