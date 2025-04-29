from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from second_win import *
class Mw (QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width , win_height)
        self.move(win_x , win_y)
    def initUI(self):
        self.hello_tect = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next  )
        self.button.setFixedSize(100 , 30)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_tect)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button , alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.tw = Tw()
        self.hide()
        
app = QApplication([])
mw = Mw()
app.exec_()
