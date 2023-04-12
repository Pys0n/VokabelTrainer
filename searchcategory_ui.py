from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

from myFunctions import FlatButton



class SearchcategoryUI(QWidget):

    def __init__(self):
        super(SearchcategoryUI, self).__init__()
        self.save_btn = QPushButton('Kategorien übernehmen')
        clear_btn = QPushButton('Alle Löschen')
        add_comboBox_btn = QPushButton('Hinzufügen')

        self.save_btn.setStyleSheet('QWidget {background-color: #00ff00}')
        clear_btn.setStyleSheet('QWidget {background-color: #ff0000}')
        add_comboBox_btn.setStyleSheet('QWidget {background-color: #00ff00}')

        titleLabel = QLabel('<b>Kategorienauswahl</b>')
        titleLabel.setFont(QFont('Arial', 15))

        title = QHBoxLayout()
        title.addStretch(1)
        title.addWidget(titleLabel)
        title.addStretch(1)

        self.catInput = QLineEdit()
        self.categories = QComboBox()
        self.categories.setEditable(True)
        self.categories.addItem('None')

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        self.scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(self.scrollLayout)
        scroll.setWidget(scrollContent)

        hL1 = QHBoxLayout()
        hL1.addWidget(self.categories)
        hL1.addWidget(add_comboBox_btn)

        hL2 = QHBoxLayout()
        hL2.addStretch(1)
        hL2.addWidget(clear_btn)
        hL2.addWidget(self.save_btn)
        hL2.addStretch(1)

        vL = QVBoxLayout()
        vL.addLayout(title)
        vL.addLayout(hL1)
        vL.addWidget(scroll)
        vL.addLayout(hL2)

        add_comboBox_btn.clicked.connect(self.add_comboBox)
        clear_btn.clicked.connect(self.clearCats)

        self.setLayout(vL)

    def add_comboBox(self):
        if self.categories.currentText() not in self.choosedCats and self.categories.currentText() != 'None':
            self.choosedCats.append(self.categories.currentText())
            self.scrollLayout.addWidget(FlatButton(self, 'catSearch',str(self.categories.currentText())))
        self.categories.setCurrentText('None')

    def clearCats(self):
        self.choosedCats = []
        while self.scrollLayout.count():
            child = self.scrollLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


    def deleteButton(self, button, way, label):
        if way == 'vokInputMainLang':
            self.new_mainLangList.remove(label)
        elif way == 'vokInputLang':
            self.new_langList.remove(label)
        elif way == 'vokInputCat':
            self.new_catList.remove(label)
        button.close()

    def showEvent(self, event):
        pass

    def load(self, lang, dict):
        self.lang = lang
        self.dict = dict
        self.categories.clear()
        self.categories.addItem('None')
        try:
            self.cat_list = []
            for vok in self.dict:
                for cat in vok['cat']:
                    if cat not in self.cat_list:
                        self.cat_list.append(cat)
            self.cat_list = sorted(self.cat_list)
            self.categories.addItems(self.cat_list)
        except: pass