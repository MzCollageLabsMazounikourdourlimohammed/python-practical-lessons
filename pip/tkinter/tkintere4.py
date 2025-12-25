from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("1000x1500")

frame =Frame(root, bg="lightgrey", width=200, height=200)
frame.pack(pady=10)


Label(frame, text="Name:",anchor="center").place(x=0,y=2)
Entry(frame).place(x=60,y=5)



lf = LabelFrame(root, text="  Personal Information", padx=10, pady=10)
lf.pack(pady=10)
Label(lf, text="Name:").pack()
Entry(lf).pack()
Label(lf, text="Email:").pack()
Entry(lf).pack()
lf.pack()



def show_info():
    messagebox.showinfo("success", "  تم التسجيل بنجاح")

Button(root, text="message", command=show_info).pack(pady=10)

def open_window():
    win = Toplevel(root)
    win.title(" New Window")
    win.geometry("1000x1500")
    Label(win, text=" New Content").pack()

Button(root, text="New Window  ", command=open_window).pack(pady=10)
root.mainloop()