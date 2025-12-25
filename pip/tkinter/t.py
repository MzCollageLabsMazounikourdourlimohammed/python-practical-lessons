import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Mobile App Interface")
root.geometry("400x700")  # حجم الهاتف تقريبًا

# ===== Scrollable Canvas =====
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor="nw")

# ===== محتوى التطبيق =====
header = tk.Label(frame, text="Welcome App", font=("Arial", 18, "bold"),
                  bg="lightblue", fg="white", height=2)
header.pack(fill="x", pady=10)

# إدخال نص
entry = tk.Entry(frame, font=("Arial", 14))
entry.pack(pady=10, padx=20, fill="x")

def show_entry():
    messagebox.showinfo("Input", entry.get())

tk.Button(frame, text="Show Text", font=("Arial", 14), bg="green", fg="white",
          command=show_entry).pack(pady=10, padx=20, fill="x")

# Text قابل للتمرير
text_widget = tk.Text(frame, height=8, font=("Arial", 12), wrap="word")
text_widget.pack(pady=10, padx=20, fill="both")
text_widget.insert("1.0", "Enter long text here...")

# أزرار كبيرة للتفاعل
for i in range(1, 6):
    tk.Button(frame, text=f"Option {i}", font=("Arial", 14), bg="orange", fg="white").pack(pady=5, padx=20, fill="x")

# Canvas للرسم أو الصور
canvas_area = tk.Canvas(frame, width=300, height=150, bg="white")
canvas_area.pack(pady=10)
canvas_area.create_rectangle(20, 20, 100, 100, fill="red")
canvas_area.create_text(150, 75, text="Canvas Area", font=("Arial", 12))

# Scale و Spinbox
tk.Scale(frame, from_=0, to=100, orient="horizontal", label="Volume").pack(pady=10, padx=20, fill="x")
tk.Spinbox(frame, from_=0, to=10, font=("Arial", 12)).pack(pady=5, padx=20, fill="x")

# ===== تحديث حجم Frame للتمرير =====
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

root.mainloop()
