from PyQt6.QtWidgets import *
from remotegui import *


class Logic(QMainWindow, Ui_Dialog):
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 10
    MIN_CHANNEL: int = 1
    MAX_CHANNEL: int = 5
    FAV_CHANNEL: int = 1
    CHANNEL_LIST = ["netflix_channel.jpg", "hulu_channel.jpg", "disneyplus_channel.jpg",
                    "primevideo_channel.jpg", "news_channel.jpg"]

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL):
        super().__init__()
        self.setupUi(self)
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

#       POWER BUTTON
        self.power_button.clicked.connect(lambda: self.power())
#       VOLUME BUTTON'S
        self.volume_up_button.clicked.connect(lambda: self.volume_up())
        self.volume_down_button.clicked.connect(lambda: self.volume_down())
#       CHANNEL BUTTON'S
        self.channel_up_button.clicked.connect(lambda: self.channel_up())
        self.channel_down_button.clicked.connect(lambda: self.channel_down())
#       CHANNEL SELECT
        self.channel1_button.clicked.connect(lambda: self.channel_select(1))
        self.channel2_button.clicked.connect(lambda: self.channel_select(2))
        self.channel3_button.clicked.connect(lambda: self.channel_select(3))
        self.channel4_button.clicked.connect(lambda: self.channel_select(4))
        self.channel5_button.clicked.connect(lambda: self.channel_select(5))
#       MUTE BUTTON
        self.mute_button.clicked.connect(lambda: self.mute())
#       FAVORITE BUTTON'S
        self.set_fav_button.clicked.connect(lambda: self.set_favorite(0))
        self.go_fav_button.clicked.connect(lambda: self.set_favorite(1))

    def power(self):
        """
        Turns on and off the TV depending on its initial status
        """
        if self.__status:
            self.__status = False
            self.tv_screen.setPixmap(QtGui.QPixmap("off_screen.jpg"))
            self.volume_slider.setSliderPosition(0)
        else:
            self.__status = True
            self.tv_screen.setPixmap(QtGui.QPixmap(self.CHANNEL_LIST[self.__channel - 1]))
            if self.__muted:
                self.volume_slider.setSliderPosition(0)
            else:
                self.volume_slider.setSliderPosition(self.__volume)

    def mute(self):
        """
        Mutes or unmutes the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.volume_slider.setSliderPosition(self.__volume)
            else:
                self.__muted = True
                self.volume_slider.setSliderPosition(0)

    def channel_up(self):
        """
        Increases TVs channel by one until the channels max is reached then goes back to channel zero
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
            self.tv_screen.setPixmap(QtGui.QPixmap(self.CHANNEL_LIST[self.__channel - 1]))

    def channel_down(self):
        """
        Decreases TVs channel by 1 until the minimum channel is reached then goes to max channel
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
            self.tv_screen.setPixmap(QtGui.QPixmap(self.CHANNEL_LIST[self.__channel - 1]))

    def channel_select(self, index):
        """
        Changes the channel to whatever number is clicked.
        """
        if self.__status:
            self.__channel = index
            self.tv_screen.setPixmap(QtGui.QPixmap(self.CHANNEL_LIST[self.__channel - 1]))

    def volume_up(self):
        """
        Increases TVs volume by one
        """
        if self.__status:
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1
            if self.__muted:
                self.__muted = False
            self.volume_slider.setSliderPosition(self.__volume)

    def volume_down(self):
        """
        Decreases TVs volume by one
        """
        if self.__status:
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1
            if self.__muted:
                self.__muted = False
            self.volume_slider.setSliderPosition(self.__volume)

    def set_favorite(self, value):
        """
        When Set is clicked it changes the favorite channel to the current channel.
        When Go is clicked it changes the current channel to the favorite channel.
        """
        if self.__status:
            if value == 0:
                self.FAV_CHANNEL = self.__channel
            if value == 1:
                self.__channel = self.FAV_CHANNEL
                self.tv_screen.setPixmap(QtGui.QPixmap(self.CHANNEL_LIST[self.__channel - 1]))
