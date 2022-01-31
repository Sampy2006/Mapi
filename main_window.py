import sys
import os

from Search import *

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QCheckBox
from PyQt5.QtGui import QPixmap, QFont

SCREEN_SIZE = 600, 450


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.setWindowTitle('Мапи')

        self.delta = '0.005'

        self.ll = ['2.294986', '48.858141']

        self.getImage()
        self.initUI()

    def main_menu(self):
        pass

    def game(self):
        pass

    def getImage(self):
        response = paint(self.ll, self.delta)

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
            self.pixmap = QPixmap(self.map_file)
            self.image = QLabel(self)
            self.image.move(0, 0)
            '''self.image.resize(*SCREEN_SIZE)'''
            self.image.setPixmap(self.pixmap)
        except Example as e:
            print(e)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
