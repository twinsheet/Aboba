from PyQt6 import QtWidgets

from untitled_ui import Ui_QMainWindow

class CustomDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QMainWindow()
        self.ui.setupUi(self)
