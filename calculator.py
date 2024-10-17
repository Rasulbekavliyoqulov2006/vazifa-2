from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(600, 500)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.lbl = ""
        
        self.window()
        self.create_buttons()

        self.show()

    def window(self):
        self.num = QLineEdit(self)
        self.num.setAlignment(Qt.AlignRight)
        self.num.setReadOnly(True)
        self.num.setStyleSheet("font-size: 30px; padding: 10px; background-color: #f0f0f0; border: 2px solid #ccc;")
        self.layout.addWidget(self.num, 0, 0, 1, 4)

    def create_buttons(self):
        self.number_button('1', 1, 0)
        self.number_button('2', 1, 1)
        self.number_button('3', 1, 2)
        self.number_button('+', 1, 3)

        self.number_button('4', 2, 0)
        self.number_button('5', 2, 1)
        self.number_button('6', 2, 2)
        self.number_button('-', 2, 3)

        self.number_button('7', 3, 0)
        self.number_button('8', 3, 1)
        self.number_button('9', 3, 2)
        self.number_button('*', 3, 3)

        self.number_button('0', 4, 0)
        self.number_button('C', 4, 1)
        self.number_button('=', 4, 2)
        self.number_button('/', 4, 3)

    def number_button(self, text, row, col):
        lbl1 = QPushButton(text, self)
        lbl1.clicked.connect(self.button)
        self.layout.addWidget(lbl1, row, col)

    def button(self):
        lbl2 = self.sender().text()

        if lbl2 == "C":
            self.clear_button()
        elif lbl2 == "=":
            self.result()
        else:
            self.add(lbl2)

    def clear_button(self):
        self.lbl = ""
        self.num.clear()

    def result(self):
        try:
            natija = eval(self.lbl)
            self.num.setText(str(natija))
            self.lbl = str(natija)
        except Exception:
            self.num.setText("Error")
            self.lbl = ""

    def add(self, text):
        self.lbl += text
        self.num.setText(self.lbl)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
