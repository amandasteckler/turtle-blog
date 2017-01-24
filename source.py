from turtle import *

penup()
goto(-180, 0)
pendown()

color("red")

for i in range(50):
    forward(i)
    left(90)

penup()
goto(180, 0)
pendown()

color(0.0, 0.5, 0.0)

for i in range(50):
    forward(i)
    right(91)

pensize(15)
color("darkCyan")
fillcolor("blue")
goto(0, 180)

begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

circle(90)
