from untitled_ui import Ui_QMainWindow
import random as r
import string as s


class MainWindow(Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QMainWindow()
        self.ui.setupUi(self)

def generate_password(length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
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

    password = ''.join(r.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    try:
        length = Ui_QMainWindow.self.spinBox()

    except:
        pass