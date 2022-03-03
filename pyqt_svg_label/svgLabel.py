import os, inspect, sys

from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QLabel


class SvgLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.__renderer = ''

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.restore()
        if self.__renderer:
            self.__renderer.render(painter)
        return super().paintEvent(e)

    def setSvgFile(self, filename: str):
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
        filename = os.path.join(caller_path, filename).replace('\\', '/')
        self.__renderer = QSvgRenderer(filename)
        self.resize(self.__renderer.defaultSize())