from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox)

from untitled_ui import Ui_QMainWindow
import random as r
import string as s


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QMainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generate_password)
        self.ui.pushButton_2.clicked.connect(self.copyrate)
        self.ui.pushButton_6.clicked.connect(self.settings)
        self.ui.pushButton_3.clicked.connect(self.clear_all)

        self.ui.checkBox.setChecked(True)
        self.ui.checkBox_2.setChecked(True)
        self.ui.checkBox_3.setChecked(True)
        self.ui.checkBox_4.setChecked(True)


    def generate_password(self):
        try:
            length = self.ui.spinBox.value()
            characters = ' '

            use_uppercase = self.ui.checkBox_3.isChecked()
            use_lowercase = self.ui.checkBox_2.isChecked()
            use_digits = self.ui.checkBox_4.isChecked()
            use_special = self.ui.checkBox.isChecked()
            if use_uppercase:
                characters += s.ascii_uppercase
            if use_lowercase:
                characters += s.ascii_lowercase
            if use_digits:
                characters += s.digits
            if use_special:
                characters += s.punctuation

            if not characters:
                QMessageBox.warning(self, 'Ошибка', 'Выберите хотя бы один тип символов')
                return

            password = ''.join(r.choice(characters) for i in range(length))

            self.ui.lineEdit.setText(password)

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка: {e}')


    def copyrate(self):
        p = self.ui.lineEdit.text()
        if p:
            clipboard = QApplication.clipboard()
            clipboard.setText(p)

    def settings(self):
        pass

    def clear_all(self):
        self.ui.lineEdit.clear()



app = QApplication([])
window = MainWindow()
window.show()
app.exec()