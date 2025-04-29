from PyQt5.QtCore import Qt
from final_win import *
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
class Tw (QWidget):
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
        self.vert1 = QVBoxLayout()
        self.vert2 = QVBoxLayout()
        self.goriz = QHBoxLayout()
        self.tecst1 = QLabel(txt_name)
        self.tecst2 = QLabel(txt_age)
        self.tecst3 = QLabel(txt_test1)
        self.tecst4 = QLabel(txt_test2)
        self.tecst5 = QLabel(txt_test3)
        self.timer = QLabel(txt_timer)
        self.b1 = QPushButton(txt_starttest1)
        self.b1.setFixedSize(200 , 30)
        self.b2 = QPushButton(txt_starttest2)
        self.b2.setFixedSize(200 , 30)
        self.b3 = QPushButton(txt_starttest3)
        self.b3.setFixedSize(200 , 30)
        self.b4 = QPushButton(txt_sendresults)
        self.b4.setFixedSize(200 , 30)
        self.inp1 =  QLineEdit(txt_hintname)
        self.inp1.setFixedSize(300 , 30)
        self.inp2 =  QLineEdit(txt_hintage)
        self.inp2.setFixedSize(100 , 30)
        self.inp3 =  QLineEdit(txt_hinttest1)
        self.inp3.setFixedSize(100 , 30)
        self.inp4 =  QLineEdit(txt_hinttest2)
        self.inp4.setFixedSize(100 , 30)
        self.inp5 =  QLineEdit(txt_hinttest3)
        self.inp5.setFixedSize(100 , 30)
        self.vert1.addWidget(self.tecst1)
        self.vert1.addWidget(self.inp1)
        self.vert1.addWidget(self.tecst2)
        self.vert1.addWidget(self.inp2)
        self.vert1.addWidget(self.tecst3)
        self.vert1.addWidget(self.b1)
        self.vert1.addWidget(self.inp3)
        self.vert1.addWidget(self.tecst4)
        self.vert1.addWidget(self.b2)
        self.vert1.addWidget(self.tecst5)
        self.vert1.addWidget(self.b3)
        self.vert1.addWidget(self.inp4)
        self.vert1.addWidget(self.inp5)
        self.vert1.addWidget(self.b4 , alignment = Qt.AlignCenter)
        self.vert2.addWidget(self.timer , alignment = Qt.AlignCenter)
        
        
        
        self.goriz.addLayout(self.vert1)
        self.goriz.addLayout(self.vert2)
        self.setLayout(self.goriz)
    def connects(self):
        self.b4.clicked.connect(self.next_click)
    def next_click(self):
        self.fw = Fw()
        self.hide()