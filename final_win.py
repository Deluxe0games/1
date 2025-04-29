from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from second_win import *
class Fw (QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width , win_height)
        self.move(win_x , win_y)
    def initUI(self):
        self.hello_tect = QLabel(txt_index)
        self.instruction = QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_tect , alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction , alignment = Qt.AlignCenter)
        self.setLayout(self.layout)