#!/usr/bin/env python3
#
# A Metadata Editor for Steam Applications
# Copyright (C) 2023  Tomás Ralph
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
##################################
#                                #
#       Created by tralph3       #
#   https://github.com/tralph3   #
#                                #
##################################

import sys
import tkinter as tk
from tkinter import messagebox

from config import config
from gui.main_window import MainWindow
from appinfo import IncompatibleVDFError


def open_gui():
    try:
        main_window = MainWindow()
        if not config.silent and config.export is None:
            main_window.window.mainloop()
    except IncompatibleVDFError as e:
        messagebox.showerror(
            title="Invalid VDF Version",
            message=f"VDF version {e.vdf_version:#08x} is not supported.",
        )


def run_splash(splash_only=False):
    import sys as _sys
    from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtCore import Qt, QTimer

    app = QApplication.instance() or QApplication(_sys.argv)

    window = QMainWindow()
    window.setWindowFlags(
        Qt.FramelessWindowHint |
        Qt.WindowStaysOnTopHint |
        Qt.SplashScreen
    )
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.setStyleSheet("background: transparent;")

    label = QLabel(window)
    pixmap = QPixmap(f"{config.IMG_PATH}/Metadeck_SPLASH.png")
    pixmap = pixmap.scaled(480, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label.setPixmap(pixmap)
    label.setFixedSize(pixmap.size())
    window.setFixedSize(pixmap.size())

    # Center on screen
    screen = app.primaryScreen().geometry()
    window.move(
        (screen.width() - pixmap.width()) // 2,
        (screen.height() - pixmap.height()) // 2
    )

    window.show()
    app.processEvents()

    # Silent patch while splash is showing
    config.silent = True
    try:
        MainWindow()
    except Exception:
        pass
    config.silent = False

    if splash_only:
        QTimer.singleShot(2000, app.quit)
    else:
        QTimer.singleShot(2000, lambda: (window.close(), open_gui()))

    app.exec_()


def main():
    if config.silent or config.export is not None:
        open_gui()
        return

    if config.splash_only:
        run_splash(splash_only=True)
        return

    # Normal launch = splash then GUI
    run_splash(splash_only=False)


if __name__ == "__main__":
    main()
