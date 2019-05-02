import sys

from PyQt5.QtWidgets import QStackedWidget, QWidget, QApplication

from expanded_components.test import test1, test2, initial


class StackedContainer(QStackedWidget):

    s = {}

    def __init__(self,parent = None):
        super(StackedContainer,self).__init__(parent)
        self.initialList()
        self.initialSelf()
        self.show()

    def initialList(self):
        self.s['initial']=initial()
        self.s['test1']=test1()
        self.s['test2']=test2()
    def initialSelf(self):
        for element in self.s.keys():
            self.addWidget(self.s.get(element))

    def getIndex(self,value):
        return self.s.get(value)