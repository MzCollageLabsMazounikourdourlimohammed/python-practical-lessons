from tkinter import *

root = Tk()
root.geometry("1000x1500")


label =Label(root, 
                 text="Welcome ",         # نص العنصر
                 font=("Arial", 16, "bold"),  # نوع وحجم الخط
                 bg="yellow",              # لون الخلفية
                 fg="blue",                # لون النص
                 width=20,                 # عرض العنصر
                 height=2,                 # ارتفاع العنصر
                 relief="ridge",           # شكل الحدود
                 # flat groove sunken raised ridge
                 bd=5,                     # سمك الحدود
                 anchor="center"  ,        # محاذاة النص
                 # N S E W NE
                 cursor="cross"  ,      #شكل المؤشر
                  #hand2 arrow cross
                 )


label.pack(pady=10)

def Welcome():
    print("Welcome from last session")

button = Button(root, 
                   text=" Say hi",          # نص الزر
                   font=("Times", 14), 
                   bg="lightgreen",          # لون الخلفية
                   fg="black",               # لون النص
                   activebackground="green", # عند الضغط
                   activeforeground="white", 
                   width=15, 
                   height=2,
                   relief="raised",
                   bd=4,
                   command=Welcome)        # الدالة المرتبطة
button.pack(pady=10)

entry =Entry(root, 
                 width=30, 
                 font=("Arial", 12), 
                 bg="white", 
                 fg="black", 
                 show="*",                # إخفاء النص (كلمة مرور)
                 justify="center")        # محاذاة النص
entry.pack(pady=5)

def ShowText():
    print("You typed:", entry.get())

Button(root, text="Show Text ", command=ShowText).pack()

text =Text(root, 
               width=40, 
               height=5, 
               font=("Arial", 12), 
               wrap="word",     # التفاف بالكلمات
               bg="lightyellow", 
               fg="black")
text.pack(pady=10)

text.insert("1.0", "  Enter your text...")  # إدراج نص مبدئي


var = IntVar()
chk = Checkbutton(root, 
                     text="active", 
                     variable=var,    # متغير مرتبط بالحالة
                     onvalue=1,       # القيمة عند التفعيل
                     offvalue=0,      # القيمة عند الإلغاء
                     font=("Arial", 12))
chk.pack()


gender = StringVar()
r1 = Radiobutton(root, text="Boy", variable=gender, value="B")
r2 = Radiobutton(root, text="Girl", variable=gender, value="G")
r1.pack()
r2.pack()

listbox = Listbox(root, height=5, selectmode="single", font=("Arial", 12))
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack(pady=10)

canvas = Canvas(root, width=100, height=100, bg="white")
canvas.pack(pady=10)

canvas.create_rectangle(20, 20, 50, 50, fill="red")  # مستطيل
canvas.create_oval(25, 25, 75, 75, fill="blue")      # دائرة
canvas.create_line(0, 0, 100, 100, fill="green", width=3)
canvas.create_text(120, 30, text="مرحبا", font=("Arial", 14), fill="black")



spin = Spinbox(root, from_=0, to=5, width=5, font=("Arial", 12))
spin.pack(pady=10)

scale = Scale(root, from_=0, to=100, orient="horizontal", length=200, tickinterval=10)
scale.pack(pady=10)


root.mainloop()