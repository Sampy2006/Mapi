import sys
import os

from Search import *

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QCheckBox
from PyQt5.QtGui import QPixmap, QFont, QPainter
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

SCREEN_SIZE = 600, 450


# print('Hello, world!')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.setWindowTitle('Мапи')

        self.delta = 0.005

        self.ll = ['2.294986', '48.858141']

        self.getImage()
        self.initUI()

    def main_menu(self):
        pass

    def game(self):
        pass

    def getImage(self):
        response = paint(self.ll, str(self.delta))

        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def initUI(self):
        try:
            self.setGeometry(100, 100, *SCREEN_SIZE)
            self.setWindowTitle('Отображение карты')

            ## Изображение
            painter = QPainter(self)
            pixmap = QPixmap(self.map_file)
            painter.drawPixmap(self.rect(), pixmap)

            self.show()

        except Example as e:
            print(e)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key_PageUp:
                if self.delta > 0:
                    self.delta -= 0.001

            if event.key() == Qt.Key_PageDown:
                if self.delta < 80:
                    self.delta += 0.005

            print(self.delta)

            self.getImage()

        except Example as e:
            print(e)

    def paintEvent(self, a0: QtGui.QPaintEvent):
        self.initUI()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
