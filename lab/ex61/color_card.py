from PySide6.QtGui import QColor, QFont, QPainter, QPen, Qt

from tools.pyside6 import BaseWindow, launch


class MyApp(BaseWindow):
    def paint(self, p: QPainter):
        p.setBrush(QColor("#000000"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRect(self.rect())

        count = 0
        for y in range(4):
            for x in range(4):
                red = count * 16
                count += 1
                for g in range(16):
                    green = g * 16
                    for b in range(16):
                        blue = b * 16
                        p.setPen(QPen(QColor("#000000")))
                        p.setBrush(QColor(red, green, blue))
                        p.drawRect(1 + 9 * b + 150 * x, 1 + 9 * g + 150 * y, 9, 9)
                p.setPen(QPen(QColor("#ffffff"), 1))
                p.setFont(QFont("Arial Narrow", 15, 800, False))
                p.drawText(65 + 150 * x, 85 + 150 * y, str(red))


launch(MyApp, 600, 600, "Color Card")
