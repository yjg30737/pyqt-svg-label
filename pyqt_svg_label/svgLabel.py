import os, inspect, sys

from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QLabel
from python_get_absolute_resource_path.getAbsoulteResourcePath import get_absolute_resource_path


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
        filename = get_absolute_resource_path(filename)
        self.__renderer = QSvgRenderer(filename)
        self.resize(self.__renderer.defaultSize())