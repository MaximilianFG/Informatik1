from PySide6.QtGui import QColor, QPainter, Qt

from tools.pyside6 import BaseWindow, launch

import random


class MyApp(BaseWindow):
    def paint(self, p: QPainter):
        random.seed(42)

        p.setBrush(QColor("#000000"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRect(self.rect())

        for a in range(500):
            gray = random.randint(100, 256)
            size = random.randint(1, 5)
            p.setBrush(QColor(gray, gray, gray))
            p.drawEllipse(random.randint(1, 600), random.randint(1, 600), size, size)


launch(MyApp, 600, 600, "Sternenhimmel")
