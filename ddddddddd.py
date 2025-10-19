from PyQt6.QtWidgets import (QApplication)

from untitled_ui import Ui_QMainWindow
import random as r
import string as s


class MainWindow(Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QMainWindow()
        self.ui.setupUi(self)

        self.length = self.ui.spinBox.setValue()



    def generate_password(self, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        characters = ' '
        if use_uppercase:
            characters += s.ascii_uppercase
        if use_lowercase:
            characters += s.ascii_lowercase
        if use_digits:
            characters += s.digits
        if use_special:
            characters += s.punctuation

        if not characters:
            raise ValueError('')

        password = ''.join(r.choice(characters) for _ in range(self.length))
        return password


app = QApplication([])
window = MainWindow()
window.show()
app.exec()