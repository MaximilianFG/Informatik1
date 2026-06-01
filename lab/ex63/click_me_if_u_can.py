from PySide6.QtGui import QColor, QFont, QPainter, QPen, Qt

from tools.pyside6 import BaseWindow, launch

import random


class MyApp(BaseWindow):
    def setup(self):
        self.nose_x = self.width() / 2
        self.nose_y = self.height() / 2
        self.nose_radius = 30
        self.score = 0

    def move_nose(self):
        self.nose_x = random.randint(self.nose_radius, self.width() - self.nose_radius)
        self.nose_y = random.randint(100, self.height() - self.nose_radius)
        self.nose_radius = random.randint(10, 50)

    def paint(self, p: QPainter):
        # Fill background with a black rectangle, no outline
        p.setBrush(QColor("#000000"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRect(self.rect())

        p.setPen(QPen(QColor("#ffffff"), 1))
        p.setFont(QFont("Arial Narrow", 20, 400, False))
        time = 10 - self.elapsed()

        if time > 0:
            p.drawText(20, 40, "Time: " + str(round(time, 1)))
            p.drawText(460, 40, "Score: " + str(self.score))

            # Draw circle
            p.setBrush(QColor("#ff0000"))
            p.drawEllipse(
                self.nose_x - self.nose_radius,
                self.nose_y - self.nose_radius,
                self.nose_radius * 2,
                self.nose_radius * 2,
            )
        else:
            p.setFont(QFont("Arial Narrow", 32, 400, False))
            p.drawText(150, 300, "Game Over!")
            p.drawText(150, 350, "Score: " + str(self.score))

    def mousePressEvent(self, event):
        dx = self.mousePos.x() - self.nose_x
        dy = self.mousePos.y() - self.nose_y
        distance = (dx**2 + dy**2) ** 0.5

        if distance <= self.nose_radius and 10 - self.elapsed() > 0:
            self.score += 1
            self.move_nose()
            self.update()


launch(MyApp, 600, 600, "Click Me If You Can")
