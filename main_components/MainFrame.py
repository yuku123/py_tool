
import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QMainWindow, QSplitter, QHBoxLayout, QWidget, QApplication, QVBoxLayout

from main_components.NavigationTree import NavigationTree
from main_components.TabContainer import TabContainer


class MainFrame(QMainWindow):
    ##分割的组件
    split = None
    ##左边分割部分的树状组件
    navigationTree = None
    tabContainer = None

    def __init__(self):
        super(MainFrame,self).__init__()

        self.navigationTree = NavigationTree(self)
        self.tabContainer = TabContainer()
        self.split = QSplitter(Qt.Horizontal)
        ## 本界面的设置
        self.setWindowTitle("牛逼哄哄的大系统")
        #self.move(500,500)
        self.showMaximized()
        ## 其他的设置
        self.configThisWindow()

    def configThisWindow(self):

        self.split.addWidget(self.navigationTree)
        self.split.addWidget(self.tabContainer)

        self.split.setStretchFactor(0,1)
        self.split.setStretchFactor(1,7)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.split)
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)

        self.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
