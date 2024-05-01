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

        self.power_button.clicked.connect(lambda: self.power())


    def power(self):
        """
        Turns on and off the TV depending on its initial status
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Mutes or unmutes the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        """
        Increases TVs channel by one until the channels max is reached then goes back to channel zero
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Decreases TVs channel by 1 until the minimum channel is reached then goes to max channel
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Increases TVs volume by one
        """
        if self.__status:
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1
            if self.__muted:
                self.__muted = False

    def volume_down(self):
        """
        Decreases TVs volume by one
        """
        if self.__status:
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1
            if self.__muted:
                self.__muted = False

    def get_volume(self):
        """
        Function to fetch the current volume level
        :return: integer
        """
        if self.__muted:
            return self.MIN_VOLUME
        else:
            return self.__volume


