import sys

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
    def add(self,QWidget):
        self.addTab(QWidget,"asdasdas")

    def tabCloseRequested(self,i):
        self.removeTab(i)
    def mouseDoubleClickEvent(self):
        print("dasdasdadsadsadasdasdasd")


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = TabContainer()
#     demo.show()
#     sys.exit(app.exec_())