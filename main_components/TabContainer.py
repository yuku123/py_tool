import sys

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QTabWidget, QWidget, QApplication, QTabBar, QTextEdit
from PyQt5.uic.properties import QtCore


class TabContainer(QTabWidget):
    def __init__(self,parent = None):
        super(TabContainer,self).__init__(parent)
        self.tab1 = QTextEdit()
        self.addTab(self.tab1,"文字编写")

        self.setTabsClosable(True)
        # self.connect
        # self.connect(self.closeTab)  # 信号与槽
        #self.tabCloseRequested()
        self.removeTab(1)

    def add(self,QWidget):
        self.addTab(QWidget,"asdasdas")
    def tabCloseRequested(self, p_int):
        self.removeTab(p_int)

    def mousePressEvent(self,QMouseEvent):
        if QMouseEvent.type() == QEvent.MouseButtonDblClick:

            print('mousePressEvent')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = TabContainer()
#     demo.show()
#     sys.exit(app.exec_())