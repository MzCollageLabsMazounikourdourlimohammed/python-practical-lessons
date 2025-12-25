import tkinter as tk

def show_name():
    user_text = entry.get()
    label_result.config(text="مرحبا: " + user_text)

window = tk.Tk()
window.title("برنامج بسيط")
window.geometry("300x200")

# عنوان
label = tk.Label(window, text="اكتب اسمك:", font=("Arial", 14))
label.pack()

# إدخال
entry = tk.Entry(window, width=25)
entry.pack()

# زر
button = tk.Button(window, text="اظهار الاسم", command=show_name)
button.pack()

# نتيجة
label_result = tk.Label(window, text="", font=("Arial", 14), fg="blue")
label_result.pack()

window.mainloop()
