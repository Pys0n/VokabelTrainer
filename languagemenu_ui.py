from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class LanguagemenuUI(QWidget):

    def __init__(self):
        super().__init__()
        self.back_btn = QPushButton('Zurück')
        self.back_btn.setStyleSheet('QWidget {background-color: #ff0000}')
        self.lang_mainLang = QPushButton('Deutsch Abfragen')
        self.mainLang_lang = QPushButton('... Abfragen')
        self.vok_eingabe = QPushButton('Vokabeln eingeben')
        self.random_btn = QPushButton('Zufällig Abfragen')
        self.cat_btn = QPushButton('Kategorien wählen')

        self.titleLabel = QLabel('<b>...</b>')
        self.titleLabel.setFont(QFont('Arial', 15))

        title = QHBoxLayout()
        title.addStretch(1)
        title.addWidget(self.titleLabel)
        title.addStretch(1)

        vL = QVBoxLayout()
        vL.addLayout(title)
        vL.addStretch(5)
        vL.addWidget(self.lang_mainLang)
        vL.addWidget(self.mainLang_lang)
        vL.addWidget(self.random_btn)
        vL.addStretch(1)
        vL.addWidget(self.cat_btn)
        vL.addStretch(1)
        vL.addWidget(self.vok_eingabe)
        vL.addStretch(1)
        vL.addWidget(self.back_btn)
        vL.addStretch(5)

        self.setLayout(vL)

    def showEvent(self, event):
        pass

    def load(self, langName):
        self.language = langName
        self.mainLang_lang.setText(langName+' Abfragen')
        self.titleLabel.setText('<b>'+langName+'</b>')
