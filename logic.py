from PyQt6.QtWidgets import *
from remotegui import *


class Logic(QMainWindow, Ui_Dialog):
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL):
        super().__init__()
        self.setupUi(self)
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel


