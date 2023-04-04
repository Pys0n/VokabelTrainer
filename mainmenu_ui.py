from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *


class MainmenuUI(QWidget):

    def __init__(self):
        super().__init__()
        self.en = QPushButton('Englisch')
        self.fr = QPushButton('Französisch')
        self.ubersetzer = QPushButton('Übersetzer')
        self.changelog_btn = QPushButton('Changelog')
        self.stat_btn = QPushButton('Statistik')
        self.quit_btn = QPushButton('Beenden')

        self.quit_btn.setStyleSheet('QWidget {background-color: #ff0004}')


        vL = QVBoxLayout()
        vL.addStretch(8)
        vL.addWidget(self.en)
        vL.addStretch(1)
        vL.addWidget(self.fr)
        vL.addStretch(3)
        vL.addWidget(self.ubersetzer)
        vL.addStretch(3)
        vL.addWidget(self.changelog_btn)
        vL.addWidget(self.stat_btn)
        vL.addWidget(self.quit_btn)
        vL.addStretch(8)

        self.setLayout(vL)

    def showEvent(self, event):
        pass

    def load(self):
        pass