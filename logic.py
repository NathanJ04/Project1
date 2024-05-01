from PyQt6.QtWidgets import *
from remotegui import *


class Logic(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
