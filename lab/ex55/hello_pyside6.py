from PySide6.QtGui import QColor, QFont, QPainter, QPen, Qt

from tools.pyside6 import BaseWindow, launch


class MyApp(BaseWindow):
    def paint(self, p: QPainter):
        # Fill background with a white rectangle, no outline
        p.setBrush(QColor("#ffffff"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRect(self.rect())

        # Draw yellow "PacMan" pie with black outline
        p.setPen(QPen(QColor("#000000"), 1))
        p.setBrush(QColor("#0dff00"))
        p.drawPie(20, 20, 60, 60, 35 * 16, 290 * 16)

        # Draw black eye of "PacMan"
        p.setBrush(QColor("#2B00FF"))
        p.drawEllipse(40, 30, 10, 10)

        p.setPen(QPen(QColor("#ff0000"), 1))
        p.drawLine(50, 50, 80, 50)

        p.setPen(QPen(QColor("#000000"), 1))
        # Draw greeting and current time in HH:MM:SS as texts
        font = QFont("Calibri", 32, 400, False)
        p.setFont(font)
        clock = f"{self.hours():02d}:{self.minutes():02d}:{self.seconds():02d}"
        p.drawText(80, 56, clock)
        font.setPointSize(16)
        p.setFont(font)
        p.drawText(80, 76, "Hallo!")


launch(MyApp, 300, 100, "Hello, Python!")
