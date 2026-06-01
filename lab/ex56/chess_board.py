from PySide6.QtGui import QColor, QPainter

from tools.pyside6 import BaseWindow, launch


class MyApp(BaseWindow):
    def paint(self, p: QPainter):
        count = 2
        for y in range(8):
            for x in range(8):
                if count % 2 == 0:
                    p.setBrush(QColor("#ffffff"))
                    p.drawRect(1 + 40 * x, 1 + 40 * y, 40 + 40 * x, 40 + 40 * y)
                else:
                    p.setBrush(QColor("#000000"))
                    p.drawRect(1 + 40 * x, 1 + 40 * y, 40 + 40 * x, 40 + 40 * y)
                count += 1
            count += 1


launch(MyApp, 320, 320, "Hello, Python!")
