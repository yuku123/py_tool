import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QApplication
from PyQt5.QtCore import Qt


class initial(QWidget):
    def __init__(self):
        super(initial,self).__init__()
        self.form1 = QWidget()
        self.formLayout1 = QHBoxLayout(self.form1)
        self.label1 = QLabel()
        self.label1.setText("初始化界面")
        self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout1.addWidget(self.label1)
        self.setLayout(self.formLayout1)

class test1(QWidget):
    def __init__(self):
        super(test1,self).__init__()
        self.form1 = QWidget()
        self.formLayout1 = QHBoxLayout(self.form1)
        self.label1 = QLabel()
        self.label1.setText("增加人员信息面板")
        self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout1.addWidget(self.label1)
        self.setLayout(self.formLayout1)

class test2(QWidget):
    def __init__(self):
        super(test2,self).__init__()
        self.form1 = QWidget()
        self.formLayout1 = QHBoxLayout(self.form1)
        self.label1 = QLabel()
        self.label1.setText("aaa")
        self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout1.addWidget(self.label1)
        self.setLayout(self.formLayout1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = test1()
    ex.show()
    sys.exit(app.exec_())