from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QListWidget

app = QApplication([])
main = QWidget()
main.setWindowTitle('Розумні замітки')
main.resize(600, 500)
main.move(300, 300)

label1 = QLabel('Список заміток')
label2 = QLabel('Список тегів')
text_ed = QTextEdit()
text1 = QListWidget()
text2 = QListWidget()
line = QLineEdit()

btn_1 = QPushButton('Створити замітку')
btn_2 = QPushButton('Видалиеи замітку')
btn_3 = QPushButton('Зберегти замітку')
btn_4 = QPushButton('Додати до замітки')
btn_5 = QPushButton('Відкріпити від замітки')
btn_6 = QPushButton('Шукати замітки по тегу')

layout_h1 = QHBoxLayout()
layout_h1.addWidget(btn_1)
layout_h1.addWidget(btn_2)

layout_h2 = QHBoxLayout()
layout_h2.addWidget(btn_4)
layout_h2.addWidget(btn_5)

layout_v1 = QVBoxLayout()
layout_v1.addWidget(text_ed)

layout_v2 = QVBoxLayout()
layout_v2.addWidget(label1)
layout_v2.addWidget(text1)
layout_v2.addLayout(layout_h1)
layout_v2.addWidget(btn_3)
layout_v2.addWidget(label2)
layout_v2.addWidget(text2)
layout_v2.addWidget(line)
layout_v2.addLayout(layout_h2)
layout_v2.addWidget(btn_6)

layout_h = QHBoxLayout() 
layout_h.addLayout(layout_v1, 60) 
layout_h.addLayout(layout_v2, 40)

# layout_h.addStretch(1)

main.setLayout(layout_h)

main.show()
app.exec_()




















# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit

# app = QApplication([])
# main = QWidget()

# button1 = QPushButton('Натисни')
# label1 = QLabel('fdfdf')

# v1 = QVBoxLayout()
# v1.addWidget(label1)
# v1.addWidget(button1)

# main.setLayout(v1)

# main.show()
# main.resize(400,400)
# main.setWindowTitle('Тестова програма')
# app.exec_()