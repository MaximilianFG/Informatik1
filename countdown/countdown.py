from PySide6.QtGui import QColor, QPainter, Qt, QFont, QPen, QPolygon, QPixmap
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
    def _get_next_target(self):
        now = datetime.now()

        for slot in TIMESLOTS:
            target = now.replace(hour=slot.hour, minute=slot.minute, second=0)

            if target > now:
                return target

        return (now + timedelta(days=1)).replace(
            hour=TIMESLOTS[0].hour, minute=TIMESLOTS[0].minute, second=0
        )

    def setup(self):
        self.override_target = None
        self.skip_pressed = False
        self.finished = False
        self.ten_seconds = False

        # Starting amount of seconds
        self.target = self._get_next_target()
        self.total_seconds_start = (self.target - datetime.now()).total_seconds()
        self.countdown()
        print(self.target)

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
        self.music_stopped = False

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

        # Knight
        self.knight_frames = [
            (
                QPixmap(str(BASE_DIR / "images" / "knight" / "knight1.png")).scaled(
                    100, 100
                ),
                200,
            ),
            (
                QPixmap(str(BASE_DIR / "images" / "knight" / "knight2.png")).scaled(
                    100, 100
                ),
                400,
            ),
            (
                QPixmap(str(BASE_DIR / "images" / "knight" / "knight3.png")).scaled(
                    100, 100
                ),
                400,
            ),
        ]
        self.knight_frame = 0
        self.knight_visible = False

        # Castle
        self.castle_frames = [
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle1.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle2.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle3.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle4.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle5.png")).scaled(
                200, 200
            ),
        ]
        self.castle_index = 0

        self.castle_whites = [
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle1_white.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle2_white.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle3_white.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle4_white.png")).scaled(
                200, 200
            ),
            QPixmap(str(BASE_DIR / "images" / "castle" / "castle5_white.png")).scaled(
                200, 200
            ),
        ]
        self.castle_flash = False

        # Timer von Animation und Flash
        self.anim_timer = QTimer()
        self.anim_timer.setSingleShot(True)
        self.anim_timer.timeout.connect(self._next_knight_frame)

        self.flash_timer = QTimer()
        self.flash_timer.setSingleShot(True)
        self.flash_timer.timeout.connect(self._end_flash)

        # Victory
        self.victory = QPixmap(str(BASE_DIR / "images" / "Victory.png"))
        self.victory_visible = False

        self.victory_audio_output = QAudioOutput()
        self.victory_audio_output.setVolume(0.3)

        self.victory_sound = QMediaPlayer()
        self.victory_sound.setAudioOutput(self.victory_audio_output)

        self.victory_sound.setSource(
            QUrl.fromLocalFile(str(BASE_DIR / "audio" / "victory_sound.mp3"))
        )

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

            if self.ten_seconds:
                self.knight_visible = True

                if not self.music_stopped:
                    self.music.stop()
                    self.music_stopped = True

                self.knight_frame = 2
                seconds_remaining = min(10, max(0, self.total_seconds_left))
                self.castle_index = int((1 - seconds_remaining / 10) * 4)

                self.castle_flash = True
                self.flash_timer.start(80)
                self._start_knight_frame()

            if self.total_seconds_left <= 0:  # Alles stoppen auf 0 Sekunden
                self.victory_visible = True
                self.knight_visible = False
                self.castle_flash = False
                self.finished = True
                self.minutes_left = 0
                self.seconds_left = 0
                self.anim_timer.stop()
                self.timer.stop()
                self.victory_sound.play()

            self.tick.play()
            self.update()

    def mousePressEvent(self, event):
        dx = event.pos().x() - self.skip_cx
        dy = event.pos().y() - self.skip_cy

        if dx**2 + dy**2 <= self.skip_radius**2:
            self._next_track()
            self.skip_pressed = True

        if self.volume_rect.contains(event.pos()):
            self.slider_active = True
            self._update_volume(event.pos().x())

    def mouseMoveEvent(self, event):
        if self.slider_active:
            self._update_volume(event.pos().x())

    def mouseReleaseEvent(self, event):
        self.slider_active = False
        self.skip_pressed = False

    def _update_volume(self, x):
        left = self.volume_rect.left()
        right = self.volume_rect.right()
        self.volume = max(0.0, min(1.0, (x - left) / (right - left)))
        self.audio_output.setVolume(self.volume)
        self.update()

    def _start_knight_frame(self):
        _, duration = self.knight_frames[self.knight_frame]
        self.anim_timer.start(duration)

    def _next_knight_frame(self):
        self.knight_frame = (self.knight_frame + 1) % len(self.knight_frames)
        self.update()
        if self.knight_visible:
            self._start_knight_frame()

    def _end_flash(self):
        self.castle_flash = False
        self.update()

    def countdown(self):
        now = datetime.now()
        if self.override_target:
            self.target = self.override_target
        else:
            self.target = self._get_next_target()

        if self.finished:
            return
        self.total_seconds_left = (self.target - now).total_seconds()
        self.minutes_left = int(self.total_seconds_left // 60)
        self.seconds_left = int(self.total_seconds_left % 60)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.override_target = datetime.now() + timedelta(seconds=10)
            self.total_seconds_left = 10
            self.total_seconds_start = 10
            self.minutes_left = 0
            self.seconds_left = 10
            self.update()

    def paint(self, p: QPainter):
        if self.total_seconds_left <= 10:
            self.ten_seconds = True
            color_a = QColor("#E51433")
            color_background = QColor("#ffffff")
            color_bottom = QColor("#3F4847")
        else:
            color_a = QColor("#3F4847")
            color_background = QColor("#E51433")
            color_bottom = QColor("#ffffff")

        # Hintergrund Rot
        p.setBrush(color_background)
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRect(self.rect())

        # Untere 2/3
        p.setBrush(color_bottom)
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
        p.setPen(QPen(color_bottom, 1))
        p.setFont(QFont("Frutiger", 100, 800, False))
        p.drawText(50, 250, "Informatik")

        # Progress Bar
        p.setPen(Qt.PenStyle.NoPen)
        progress = 1 - (self.total_seconds_left / self.total_seconds_start)
        progress_paint = int(self.width() * progress)

        p.setBrush(color_a)
        p.drawRect(0, 300, self.width(), 50)

        if progress_paint > 0:
            p.setBrush(color_bottom)
            p.drawRect(0, 300, progress_paint, 50)

        if not self.ten_seconds:
            # Countdown
            p.setPen(QPen(color_a, 1))
            p.setFont(QFont("Frutiger", 150, 800, False))
            countdown_text = f"{self.minutes_left:02d} : {self.seconds_left:02d}"
            p.drawText(
                0, 450, self.width(), 200, Qt.AlignmentFlag.AlignHCenter, countdown_text
            )

            # Skip Button
            p.setBrush(color_a)
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(480, 750, 60, 60)

            skip_color = color_bottom

            if self.skip_pressed:
                skip_color = color_background

            p.setBrush(skip_color)
            triangle = QPolygon([QPoint(528, 780), QPoint(493, 760), QPoint(493, 800)])
            p.drawPolygon(triangle)
            triangle2 = QPolygon([QPoint(538, 780), QPoint(503, 760), QPoint(503, 800)])
            p.drawPolygon(triangle2)

            # Volume Slider
            p.setBrush(color_a)
            p.setPen(Qt.PenStyle.NoPen)
            p.drawRoundedRect(self.volume_rect, 5, 5)

            filled_rect = QRect(
                self.volume_rect.x(),
                self.volume_rect.y(),
                int(self.volume_rect.width() * self.volume),
                self.volume_rect.height(),
            )
            p.setPen(QPen(color_a, 1))
            p.setBrush(color_background)
            p.drawRoundedRect(filled_rect, 5, 5)
        else:
            # Countdown
            p.setPen(QPen(color_a, 1))
            p.setFont(QFont("Frutiger", 150, 800, False))
            countdown_text = f"{self.minutes_left:02d} : {self.seconds_left:02d}"
            p.drawText(
                0, 700, self.width(), 200, Qt.AlignmentFlag.AlignHCenter, countdown_text
            )

        # Castle and Knight

        if self.ten_seconds:
            if self.castle_flash:
                p.drawPixmap(620, 450, self.castle_whites[self.castle_index])

            else:
                p.drawPixmap(620, 450, self.castle_frames[self.castle_index])

            if self.knight_visible:
                p.drawPixmap(810, 540, self.knight_frames[self.knight_frame][0])

            if self.victory_visible:
                p.drawPixmap(208, 100, self.victory)


launch(MyApp, 1440, 900, "Countdown")
