import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QCheckBox
from PyQt5.QtGui import QPixmap, QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 800)
        self.setFixedSize(1500, 844)
        self.setWindowTitle('Мапи')
        self.main_menu()

        self.delta = 0.005

        self.ll = 2.294986, 48.858141

    def main_menu(self):
        pass

    def game(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
