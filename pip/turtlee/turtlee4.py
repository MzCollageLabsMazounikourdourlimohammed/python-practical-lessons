from turtle import *

# t = Turtle()
# screen = Screen()
# screen.listen()

# def up():
#     t.setheading(90)
#     t.forward(20)

# def down():
#     t.setheading(270)
#     t.forward(20)

# def left_move():
#     t.setheading(180)
#     t.forward(20)

# def right_move():
#     t.setheading(0)
#     t.forward(20)

# screen.onkey(up, "Up")
# screen.onkey(down, "Down")
# screen.onkey(left_move, "Left")
# screen.onkey(right_move, "Right")

# done()
#===================

# t = Turtle()

# def drag_move(x, y):
#     t.ondrag(None)    # لمنع تكرار الحدث أثناء السحب نفسه
#     t.goto(x, y)
#     t.ondrag(drag_move)

# t.ondrag(drag_move)

# done()

#====================

from turtle import *
import random

t = Turtle()
screen = Screen()
screen.listen()

colors = ["red", "blue", "green", "orange", "purple", "black"]

# الرسم بالفأرة
def draw(x, y):
    t.goto(x, y)

def change_color():
    t.color(random.choice(colors))

def clear_screen():
    t.clear()

# حجم القلم
def inc_size():
    t.pensize(t.pensize() + 1)

def dec_size():
    size = t.pensize()
    if size > 1:
        t.pensize(size - 1)

# ربط الأحداث
screen.onclick(draw)
screen.onkey(change_color, "q")
screen.onkey(clear_screen, "w")
screen.onkey(inc_size, "a")
screen.onkey(dec_size, "s")

done()
