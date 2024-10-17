from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont
import sys

class Tetris(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tetris")
        self.setFixedSize(1400, 900)

        self.button1 = QPushButton("1", self)
        self.set_button_style(self.button1)
        self.button1.move(10, 10)  

        self.button2 = QPushButton("2", self)
        self.set_button_style(self.button2)
        self.button2.move(220, 10)  

        self.button3 = QPushButton("3", self)
        self.set_button_style(self.button3)
        self.button3.move(430, 10)  

        self.button4 = QPushButton("4", self)
        self.set_button_style(self.button4)
        self.button4.move(640, 10)  

        lyt = QHBoxLayout()

        self.button1.clicked.connect(self.shape1)  
        self.button2.clicked.connect(self.shape2)  
        self.button3.clicked.connect(self.shape3)  
        self.button4.clicked.connect(self.shape4)  

        btt_lyt = QVBoxLayout()
        btt_lyt.addWidget(self.button1)
        btt_lyt.addWidget(self.button2)
        btt_lyt.addWidget(self.button3)
        btt_lyt.addWidget(self.button4)

        self.grid_layout = QGridLayout()  
        self.grid_layout.setSpacing(10)

        lyt.addLayout(btt_lyt)
        lyt.addLayout(self.grid_layout)

        self.setLayout(lyt)

    def set_button_style(self, button):
        button.setFont(QFont("Open Sans", 23))
        button.setFixedSize(200, 100)

    def shape1(self):  
        self.clear_shapes()
        self.create_shape([(0, 0), (0, 1), (1, 0), (2, 0)])

    def shape2(self):  
        self.clear_shapes()
        self.create_shape([(0, 0), (0, 1), (1, 0), (1, 1)])

    def shape3(self):  
        self.clear_shapes()
        self.create_shape([(0, 0), (0, 1), (0, 2), (0, 3)])

    def shape4(self):  
        self.clear_shapes()
        self.create_shape([(0, 1), (1, 0), (1, 1), (2, 0)])

    def clear_shapes(self):
        for i in reversed(range(self.grid_layout.count())):
            lbl = self.grid_layout.itemAt(i).widget()
            if lbl is not None:
                lbl.deleteLater()

    def create_shape(self, positions):
        for row, col in positions:
            btn = QPushButton("", self)
            btn.setFixedSize(200, 200)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: lightblue; 
                    font-size: 20px; 
                    border: 2px solid #ccc; 
                    border-radius: 10px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #add8e6;
                }
                QPushButton:pressed {
                    background-color: #87ceeb; 
                }
            """)
            self.grid_layout.addWidget(btn, row, col)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tetris()
    window.show()
    sys.exit(app.exec_())
