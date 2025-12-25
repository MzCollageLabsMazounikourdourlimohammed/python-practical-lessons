from turtle import *

t = Turtle()

speed(3)
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

for i in range(72):
    color(colors[i % 6])
    circle(100)
    right(5)

done()
