import turtle
import math

file = open("line-data.txt", "r")

window = turtle.Screen()
window.setup(width=450, height=450)
window.title("Turtle Draw")
window.bgcolor("white")

turtleDraw = turtle.Turtle()
turtleDraw.hideturtle()                   
turtleDraw.speed(10)                        
turtleDraw.penup()                        
turtleDraw.showturtle()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed(10)

fname = input("Enter input filename: ").strip()
try:
    infile = open(fname, "r")
except Exception as e:
    print(f"Error opening file '{fname}': {e}")
    'return'

total_distance = 0.0
prev_point = None   
pen_down = False

    
for line in file:
    raw = line.strip()
    if raw == "":
        continue
    parts = raw.split()

        
    if parts[0].lower() == "stop":
        
        turtleDraw.penup()
        pen_down = False
        prev_point = None
        continue

    if len(parts) < 3:

        print(f"Skipping malformed line: {raw}")
        continue

    color = parts[0]
    try:
        x = float(parts[1])
        y = float(parts[2])
    except ValueError:
        print(f"Skipping line with non-numeric coords: {raw}")
        continue
    
    try:
        turtleDraw.pencolor(color)
    except Exception:

        turtleDraw.pencolor("black")
    if prev_point is None:
        turtleDraw.penup()
        turtleDraw.goto(x, y)
            
        turtleDraw.pendown()
        pen_down = True
        prev_point = (x, y)
    else:

        if not pen_down:
            turtleDraw.pendown()
            pen_down = True

        dx = x - prev_point[0]
        dy = y - prev_point[1]
        dist = math.hypot(dx, dy)
        total_distance += dist

        turtleDraw.goto(x, y)
        prev_point = (x, y)

    right_x = 450 / 2 - 10  
    bottom_y = -450 / 2 + 20 
    writer.goto(right_x, bottom_y)
    writer.write(f"Total distance = {total_distance:.2f}", align="right", font=("Arial", 12, "normal"))

    window.update()

input("Press Enter to close the window...")
turtle.bye()