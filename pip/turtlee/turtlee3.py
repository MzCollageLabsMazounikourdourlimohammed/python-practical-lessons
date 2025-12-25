from turtle import *

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("lightblue")
screen.title(" Turtle Controls")
# screen.bgpic("background.gif") 

shape()  # turtle, arrow, circle, square, triangle, classic
shapesize(2, 2)  # طول العرض 
speed(3)

# colormode(255)
# color(120, 90, 200)
# ألوان ورسم
color("red", "yellow") #لون الشكل 
#strok fill  لون القلم وداخلي 
pensize(4)

penup()
goto(-200, 100)
pendown()


#البدا والايقاف 
begin_fill() 
forward(120)
left(120)
forward(120)
left(120)
forward(120)
end_fill()

# clear()  
#    # يمسح الرسم فقط
# reset()

color("red")
penup()
goto(0, -50)
pendown()
for i in range(10):
    forward(100)
    backward(100)
    left(90+i**2*2)

done()
