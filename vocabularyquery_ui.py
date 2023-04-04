#from random import randint
#from os.path import exists
#import pathlib
#from datetime import date

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

from statistic_ui import StatisticUI
from myFunctions import *

#PATH = str(pathlib.Path(__file__).parent.absolute())
#FILENAME = 'statistic_en.dat'
#FILE_STATISTIC_EN = PATH+"/"+FILENAME
#FILENAME = 'statistic_fr.dat'
#FILE_STATISTIC_FR = PATH+"/"+FILENAME

class VocabularyqueryUI(QWidget):

    def __init__(self):
        super(VocabularyqueryUI, self).__init__()
        self.last = QLabel()
        self.vok = QLabel()
        self.mainLangLabel = QLabel()
        self.langLabel = QLabel()

        self.input = QLineEdit()

        self.ready_btn = QPushButton('Überprüfen')
        self.back_btn = QPushButton('Zurück')
        self.ready_btn.setStyleSheet('QWidget {background-color: #00ff00}')
        self.back_btn.setStyleSheet('QWidget {background-color: #ff0000}')

        titleLabel = QLabel('<b>Vokabel Abfrage</b>')
        titleLabel.setFont(QFont('Arial', 15))

        title = QHBoxLayout()
        title.addStretch(1)
        title.addWidget(titleLabel)
        title.addStretch(1)

        hL = QHBoxLayout()
        hL.addWidget(self.back_btn)
        hL.addWidget(self.ready_btn)

        vL = QVBoxLayout()
        vL.addLayout(title)
        vL.addStretch(5)
        vL.addWidget(self.mainLangLabel)
        vL.addWidget(self.vok)
        vL.addStretch(1)
        vL.addWidget(self.langLabel)
        vL.addWidget(self.input)
        vL.addStretch(2)
        vL.addWidget(self.last)
        vL.addStretch(2)
        vL.addLayout(hL)

        self.setLayout(vL)

    def showEvent(self, event):
        pass

    def load(self, dict, names, random):
        self.random = random
        self.dict = dict
        self.mainLang = names[0]
        self.mainLangName = names[1]
        self.lang = names[2]
        self.langName = names[3]
        self.run = 0
        self.last.setText("\n\n\n\n")
        self.mainLangLabel.setText(self.mainLangName+':')
        self.langLabel.setText(self.langName+':')
        if len(self.dict) != 0:
            self.vok.setText(make_string(self.dict[self.run][self.mainLang]))
        self.right = 0
        self.wrong = 0
        self.answered = 0