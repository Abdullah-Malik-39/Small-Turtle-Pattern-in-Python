import turtle
from turtle import *
speed(15)
bgcolor("black")
r,g,b = 255,0,0
t = turtle.Turtle()
colormode(255)
for n in range(255*2):
    if n<255//3 : 
        g += 3
    elif n<255*2//3 : 
        r -= 3
    elif n<255 : 
        b += 3
    elif n<255*4//3 : 
        g -= 3
    elif n<255*5//3 : 
        r += 3
    else:
        b -= 3
    fd(0+n)
    rt(91)
    pencolor(r,g,b)