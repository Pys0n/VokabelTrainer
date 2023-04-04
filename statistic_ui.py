from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *


class StatisticUI(QWidget):

    def __init__(self):
        super(StatisticUI, self).__init__()
        self.next_btn = QPushButton('Weiter')

        self.title = QLabel('<b>Statistik Jetzt:</b>')
        self.rightLabel = QLabel('0')
        self.wrongLabel = QLabel('0')
        self.allLabel = QLabel('0')

        self.todayTitle = QLabel('<b>Statistik Heute:</b>')
        self.todayRightLabel = QLabel('0')
        self.todayWrongLabel = QLabel('0')
        self.todayAllLabel = QLabel('0')

        vL1 = QVBoxLayout()
        vL1.addWidget(self.title)
        vL1.addWidget(self.rightLabel)
        vL1.addWidget(self.wrongLabel)
        vL1.addWidget(self.allLabel)

        vL2 = QVBoxLayout()
        vL2.addWidget(self.todayTitle)
        vL2.addWidget(self.todayRightLabel)
        vL2.addWidget(self.todayWrongLabel)
        vL2.addWidget(self.todayAllLabel)

        hLstats = QHBoxLayout()
        hLstats.addLayout(vL1)
        hLstats.addStretch(1)
        hLstats.addLayout(vL2)

        titleLabel = QLabel('<b>Statistik</b>')
        titleLabel.setFont(QFont('Arial', 15))

        titleLayout = QHBoxLayout()
        titleLayout.addStretch(1)
        titleLayout.addWidget(titleLabel)
        titleLayout.addStretch(1)

        vL = QVBoxLayout()
        vL.addLayout(titleLayout)
        vL.addStretch(1)
        vL.addLayout(hLstats)
        vL.addStretch(4)
        vL.addWidget(self.next_btn)

        #self.next_btn.clicked.connect(self.setMAIN)

        self.setLayout(vL)

    def showEvent(self, event):
        self.rightLabel.setText('Richtig beantwortet: '+str(self.right))
        self.wrongLabel.setText('Falsch beantwortet: '+str(self.wrong))
        self.allLabel.setText('Beantwortet: '+str(self.answered)+'/'+str(self.len))
      
        #self.todayRightLabel.setText('Richtig beantwortet: '+str(self.right))
        #self.todayWrongLabel.setText('Falsch beantwortet: '+str(self.wrong))
        #self.todayAllLabel.setText('Beantwortet: '+str(self.answered))

        self.todayRightLabel.setText('Richtig beantwortet: Kommt bald')
        self.todayWrongLabel.setText('Falsch beantwortet: Kommt bald')
        self.todayAllLabel.setText('Beantwortet: Kommt bald')

    def setStatistic(self, right, wrong, answered, len):
        self.right = right
        self.wrong = wrong
        self.answered = answered
        self.len = len
