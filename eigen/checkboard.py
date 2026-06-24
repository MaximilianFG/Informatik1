from PySide6.QtGui import QColor, QPainter, QPen

from tools.pyside6 import BaseWindow, launch


class Checkboard(BaseWindow):
    def paint(self, p: QPainter):
        p.setBrush(QColor("#ffffff"))
        p.drawRect(0, 0, self.width(), self.height())

        for y in range(8):
            for x in range(8):
                if x > y:
                    p.setBrush(QColor("#ff0000"))
                    p.setPen(QPen(QColor("#000000")))
                else:
                    p.setBrush(QColor("#0000ff"))
                    p.setPen(QPen(QColor("#000000")))

                if x % 2 == 0:
                    p.drawRect(x * 40 + y % 2 * 40, y * 40, 40, 40)
                else:
                    p.setBrush(QColor("#ffffff"))
                    p.drawRect(x * 40 + y % 2 * 40, y * 40, 40, 40)


launch(Checkboard, 320, 320, "Checkboard!")
