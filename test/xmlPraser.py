import  xml.dom.minidom

#打开xml文档
from PyQt5.QtWidgets import QTreeWidgetItem

dom = xml.dom.minidom.parse('../tree.xml').documentElement

def prase(node,widget):
    nodename = node.getAttribute("nodename")
    nodevalue = node.getAttribute("nodevalue")
    widget.setText(0,nodename)
    widget.setText(1,nodevalue)

    for nodes in node.getElementsByTagName("node"):
        prase(nodes,QTreeWidgetItem(widget))
    #return widget
    #
    # widgetRefresh = QTreeWidgetItem(widget)
    # widgetRefresh.setText(0,nodename)
    # widgetRefresh.setText(1,nodevalue)
    # prase(node,widgetRefresh)
