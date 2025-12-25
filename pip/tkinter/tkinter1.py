import tkinter as tk

window = tk.Tk()             # إنشاء نافذة
window.title("My First App") # عنوان النافذة
window.geometry("400x300")   # الحجم: عرض × ارتفاع

# لعرض نص  والتحكم في 
label = tk.Label(window, text="Hello My Friends!", font=("Arial", 20))

label.pack() 
# اسهل في التعامل يضع عناصر فوق بعض


# label.grid(row=2, column=2) 
#يوزع العناصر على شكل جدول

# label.place(x=0,y=30)
 
 # لاضافة حقل ادخال  
entry = tk.Entry(window, width=30)
entry.pack(padx=10,pady=20)
# entry.grid(row=2, column=2) 
# entry.place(x=100,y=130)
 # لاضافة زر 
def say_hello():
    print("You typed:", entry.get())
    print("Hello from last session!")

button = tk.Button(window, text="Click Me", command=say_hello)
button.pack()
# button.grid(row=2, column=2) 
# button.place(x=200,y=200)



    



window.mainloop()            # تشغيل نافذة التطبيق
