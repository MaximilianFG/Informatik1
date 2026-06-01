from PySide6.QtGui import QColor, QFont, QPainter, QPen, Qt

from tools.pyside6 import BaseWindow, launch


class MyApp(BaseWindow):
    def paint(self, p: QPainter):
        # Fill background with a white rectangle, no outline
        p.setBrush(QColor("#ffffff"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRect(self.rect())

        p.setBrush(QColor("#E51433"))
        p.drawRect(10, 11, 6, 41)
        p.drawRect(23, 27, 6, 25)
        p.drawRect(39, 27, 6, 25)
        p.drawRect(52, 11, 6, 41)
        p.drawRect(68, 27, 6, 25)
        p.drawRect(81, 27, 6, 25)
        p.drawRect(94, 27, 6, 25)  #

        p.setPen(QPen(QColor("#3F4847"), 1))
        font = QFont("Arial Narrow", 12, 800, False)
        p.setFont(font)
        p.drawText(10, 72, "HOCHSCHULE")
        p.drawText(10, 88, "DER MEDIEN")


launch(MyApp, 109, 100, "HdM Logo")
