import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QCheckBox, QRadioButton, QSpinBox, QSlider, QVBoxLayout, QHBoxLayout


#=======================

# إنشاء التطبيق
app = QApplication(sys.argv)

# إنشاء نافذة رئيسية
window = QWidget()
window.setWindowTitle("PyQt5 Example")  # عنوان النافذة
window.setGeometry(100, 100, 600, 400)  # الموقع والحجم (x, y, width, height)
layout = QVBoxLayout()   # ترتيب عمودي

# عناصر واجهة
label = QLabel("Hello PyQt5")  # تسمية نصية
layout.addWidget(label)

button = QPushButton("Click Me")  # زر
layout.addWidget(button)

entry = QLineEdit()  # مربع نص
layout.addWidget(entry)

text_area = QTextEdit()  # منطقة نص متعددة الأسطر
layout.addWidget(text_area)

combo = QComboBox()  # قائمة منسدلة
combo.addItems(["Option 1", "Option 2", "Option 3"])
layout.addWidget(combo)

checkbox = QCheckBox("Check Me")
layout.addWidget(checkbox)

radio1 = QRadioButton("Choice 1")
layout.addWidget(radio1)

radio2 = QRadioButton("Choice 2")
layout.addWidget(radio2)

spinbox = QSpinBox()  # أرقام قابلة للتعديل
layout.addWidget(spinbox)

slider = QSlider()  # شريط تمرير
layout.addWidget(slider)












window.setLayout(layout)
window.show()  # عرض النافذة
sys.exit(app.exec_())  # بدء حلقة التطبيق