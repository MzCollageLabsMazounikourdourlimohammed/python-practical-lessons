from turtle import *

t = Turtle()
def m(x, y):
    t.goto(x, y)

screen = Screen()
screen.onclick(m)

done()
