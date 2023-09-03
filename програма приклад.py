from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
def show_winner():
    number = randint(0,99)
    winner.setText("Переможець:")
    text.setText(str(number))
app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.resize(900,400)

winner = QLabel("Нажміть, щоб дізнатись переможця!")
text = QLabel("?")
button = QPushButton("Результат")

v_win = QVBoxLayout()
v_win.addWidget(winner, alignment = Qt.AlignCenter)
v_win.addWidget(text, alignment = Qt.AlignCenter)
v_win.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(v_win)

button.clicked.connect(show_winner)

app.exec_()