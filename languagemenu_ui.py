from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class LanguagemenuUI(QWidget):

    def __init__(self):
        super().__init__()
        self.back_btn = QPushButton('Zurück')
        self.back_btn.setStyleSheet('QWidget {background-color: #ff0000}')
        self.voc_query = QPushButton('Vokabeln Abfragen')
        self.voc_edit = QPushButton('Vokabeln eingeben/bearbeiten')
        #self.add_tags = QPushButton('Marker setzen')

        self.titleLabel = QLabel('<b>...</b>')
        self.titleLabel.setFont(QFont('Arial', 15))

        title = QHBoxLayout()
        title.addStretch(1)
        title.addWidget(self.titleLabel)
        title.addStretch(1)

        vL = QVBoxLayout()
        vL.addLayout(title)
        vL.addStretch(5)
        vL.addWidget(self.voc_query)
        vL.addStretch(1)
        vL.addWidget(self.voc_edit)
        vL.addStretch(1)
        #vL.addWidget(self.add_tags)
        #vL.addStretch(1)
        vL.addWidget(self.back_btn)
        vL.addStretch(7)

        self.setLayout(vL)

    def showEvent(self, event):
        pass

    def load(self, langName):
        self.titleLabel.setText('<b>'+langName+'</b>')
