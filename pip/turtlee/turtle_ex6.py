from turtle import *

t = Turtle()
# انشاء دالة  للتحرك 
def move_forward():
    t.forward(20)

def Up_forward():
    # t.right(150)
    t.forward(20)
    

screen = Screen()
screen.listen()   # اجعل الشاشة تطبق اموار لوحة المفاتيح 
screen.onkey(move_forward, "Left")
screen.onkeypress(Up_forward, "a")

done()

