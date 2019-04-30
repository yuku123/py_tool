import sys

from PyQt5.QtWidgets import QApplication

from main_components.MainFrame import MainFrame

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client = MainFrame()
    client.show()
    app.exec_()
