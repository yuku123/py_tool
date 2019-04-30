import sys

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QVBoxLayout, QHBoxLayout, QWidget


class NavigationTree(QTreeWidget):
    myControls = {}
    #顶层的父容器
    mainFrame = None

    def __init__(self,MainFrame, parent=None):

        super(NavigationTree, self).__init__()

        ##把顶层的父容器带进来
        self.mainFrame = MainFrame

        self.setWindowTitle('TreeWidget')
        self.myControls['tree'] = self

        self.setColumnCount(1)  # 说明是树形的表，
        self.setHeaderLabels(['Key'])  # 是表，则有表头
        ##填充树的样式
        self.build_tree()
        self.connectAll()

    def build_tree(self):
        root = QTreeWidgetItem(self)
        root.setText(0, '功能')
        root.setText(1, 'value')

        child1 = QTreeWidgetItem(root)  # 指出父结点
        child1.setText(0, 'aa')
        child1.setText(1, 'aa')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, '模板配置 ')

        child3 = QTreeWidgetItem(root)
        child3.setText(0, '信息配置')

        child4 = QTreeWidgetItem(child3)
        child4.setText(0, '显示面板')

        child5 = QTreeWidgetItem(child3)
        child5.setText(0, '显示面板')

        # 以下两句是主窗口的设置
        self.addTopLevelItem(root)
        self.expandAll()

    def connectAll(self):
        self.clicked.connect(self.onClicked)

    def onClicked(self):
        item = self.currentItem()
        print('Key=%s,value=%s' % (item.text(0), item.text(1)))
        if item.text(1) == 'aa':
            self.mainFrame.tabContainer.add(QWidget())
        elif item.text(0) == '查询人员信息':
            self.on_pushButton2_clicked()
        else:
            print('返回主界面')