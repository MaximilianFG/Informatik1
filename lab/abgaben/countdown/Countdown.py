from PySide6.QtGui import QColor, QPainter, Qt, QFont, QPen, QPolygon
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTimer, QPoint, QRect

from tools.pyside6 import BaseWindow, launch

from datetime import datetime, timedelta, time

from pathlib import Path

BASE_DIR = Path(__file__).parent
TIMESLOTS = [
    time(8, 15),
    time(10, 00),
    time(11, 45),
    time(14, 15),
    time(16, 00),
    time(17, 45),
    time(19, 30),
]


class MyApp(BaseWindow):
    def _get_next_slot(self):
        now = datetime.now()
        current_time = now.time()

        for slot in TIMESLOTS:
            return now.replace(hour=slot.hour, minute=slot.minute, second=0)

        return (now + timedelta(days=1)).replace(
            hour=TIMESLOTS[0].hour, minute=TIMESLOTS[0].minute, second=0
        )

    def setup(self):
        self.override_target = None
        self.countdown()

        self.total_seconds_start = (target_time - current_time).total_seconds()

        # Volume slider
        self.volume = 0.1
        self.volume_rect = QRect(860, 765, 200, 25)
        self.slider_active = False

        # Tick Sound
        self.tick = QSoundEffect()
        self.tick.setSource(QUrl.fromLocalFile(str(BASE_DIR / "audio" / "tick.wav")))
        self.tick.setLoopCount(1)
        self.tick.setVolume(0.5)

        # Timer
        self.last_second = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        self.timer.start(500)

        # Hintergrundmusik mit Playlist
        self.playlist = [
            QUrl.fromLocalFile(str(BASE_DIR / "audio" / "elevator1.mp3")),
            QUrl.fromLocalFile(str(BASE_DIR / "audio" / "elevator2.mp3")),
            QUrl.fromLocalFile(str(BASE_DIR / "audio" / "elevator3.mp3")),
            QUrl.fromLocalFile(str(BASE_DIR / "audio" / "elevator4.mp3")),
        ]
        self.current_track = 0

        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(0.05)

        self.music = QMediaPlayer()
        self.music.setAudioOutput(self.audio_output)
        self.music.mediaStatusChanged.connect(self._next_track)
        self._play_current()

        # Skip button
        self.skip_cx = 510
        self.skip_cy = 780
        self.skip_radius = 30

    def _play_current(self):
        self.music.setSource(self.playlist[self.current_track])
        self.music.play()

    def _next_track(self, status=None):
        if status is None or status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self._play_current()

    def _tick(self):
        self.countdown()

        if self.seconds_left != self.last_second:
            self.last_second = self.seconds_left
            self.tick.play()
            self.update()

    def mousePressEvent(self, event):
        dx = event.pos().x() - self.skip_cx
        dy = event.pos().y() - self.skip_cy

        if dx**2 + dy**2 <= self.skip_radius**2:
            self._next_track()

        if self.volume_rect.contains(event.pos()):
            self.slider_active = True
            self._update_volume(event.pos().x())

    def mouseMoveEvent(self, event):
        if self.slider_active:
            self._update_volume(event.pos().x())

    def mouseReleaseEvent(self, event):
        self.slider_active = False

    def _update_volume(self, x):
        left = self.volume_rect.left()
        right = self.volume_rect.right()
        self.volume = max(0.0, min(1.0, (x - left) / (right - left)))
        self.audio_output.setVolume(self.volume)
        self.update()

    def countdown(self):
        current_time = datetime.now()
        if self.override_target:
            if current_time >= self.override_target:
                self.override_target = None
                target_time = current_time.replace(hour=8, minute=15, second=0)
                if target_time <= current_time:
                    target_time += timedelta(days=1)
            else:
                target_time = self.override_target
        else:
            target_time = current_time.replace(hour=8, minute=15, second=0)
            if target_time <= current_time:
                target_time += timedelta(days=1)

        self.total_d_seconds = (target_time - current_time).total_seconds()
        self.minutes_left = int(self.total_d_seconds // 60)
        self.seconds_left = int(self.total_d_seconds % 60)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.override_target = datetime.now() + timedelta(seconds=10)
            self.total_d_seconds = 10
            self.total_seconds_start = 10
            self.minutes_left = 0
            self.seconds_left = 10
            self.update()

    def paint(self, p: QPainter):
        # Hintergrund Rot
        p.setBrush(QColor("#E51433"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRect(self.rect())

        # Untere Hälfte Weiß
        p.setBrush(QColor("#ffffff"))
        p.drawRect(0, 300, 1440, 600)

        # HdM Logo unten rechts
        p.setBrush(QColor("#E51433"))
        p.drawRect(10, 808, 6, 41)
        p.drawRect(23, 824, 6, 25)
        p.drawRect(39, 824, 6, 25)
        p.drawRect(52, 808, 6, 41)
        p.drawRect(68, 824, 6, 25)
        p.drawRect(81, 824, 6, 25)
        p.drawRect(94, 824, 6, 25)
        p.setPen(QPen(QColor("#3F4847"), 1))
        p.setFont(QFont("Frutiger", 13, 800, False))
        p.drawText(10, 869, "HOCHSCHULE")
        p.drawText(10, 890, "DER MEDIEN")

        # Informatik Schriftzug
        p.setPen(QPen(QColor("#ffffff"), 1))
        p.setFont(QFont("Frutiger", 100, 800, False))
        p.drawText(50, 250, "Informatik")
        # Progress Bar
        p.setPen(Qt.PenStyle.NoPen)
        progress = 1 - (self.total_d_seconds / self.total_seconds_start)
        progress_paint = int(self.width() * progress)

        if progress_paint > 0:
            p.setBrush(QColor("#3F4847"))
            p.drawRect(0, 300, progress_paint, 50)

        # Countdown
        p.setPen(QPen(QColor("#3F4847"), 1))
        p.setFont(QFont("Frutiger", 150, 800, False))
        countdown_text = f"{self.minutes_left:02d} : {self.seconds_left:02d}"
        p.drawText(
            0, 450, self.width(), 200, Qt.AlignmentFlag.AlignHCenter, countdown_text
        )

        # Skip Button
        p.setBrush(QColor("#3F4847"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(480, 750, 60, 60)

        p.setBrush(QColor("#ffffff"))
        triangle = QPolygon([QPoint(528, 780), QPoint(493, 760), QPoint(493, 800)])
        p.drawPolygon(triangle)
        triangle2 = QPolygon([QPoint(538, 780), QPoint(503, 760), QPoint(503, 800)])
        p.drawPolygon(triangle2)

        # Volume Slider
        p.setBrush(QColor("#3F4847"))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(self.volume_rect, 5, 5)

        filled_rect = QRect(
            self.volume_rect.x(),
            self.volume_rect.y(),
            int(self.volume_rect.width() * self.volume),
            self.volume_rect.height(),
        )
        p.setPen(QPen(QColor("#3F4847"), 1))
        p.setBrush(QColor("#E51433"))
        p.drawRoundedRect(filled_rect, 5, 5)


launch(MyApp, 1440, 900, "Countdown")
