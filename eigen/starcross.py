from PySide6.QtGui import QColor, QPainter, QPen

from tools.pyside6 import BaseWindow, launch

BLACK = QColor("#000000")
WHITE = QColor("#ffffff")


class Starcross(BaseWindow):
    def paint(self, p: QPainter):
        p.setPen(QPen(BLACK))

        for y in range(9):
            for x in range(9):
                if x == y or x == 4 or y == 4 or x + y == 8:
                    p.setBrush(BLACK)
                    p.drawRect(x * 40, y * 40, 40, 40)

                else:
                    p.setBrush(WHITE)
                    p.drawRect(x * 40, y * 40, 40, 40)


launch(Starcross, 360, 360, "Star")
