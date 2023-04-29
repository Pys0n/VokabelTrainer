from datetime import date

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

from myFunctions import *

class VocabularyinputUI(QWidget):

    def __init__(self):
        super(VocabularyinputUI, self).__init__()
        self.back_btn = QPushButton('Zurück')
        self.save_btn = QPushButton('Speichern')
        self.add_mainLang_input_btn = QPushButton('Hinzufügen')
        self.add_lang_input_btn = QPushButton('Hinzufügen')
        self.add_cat_comboBox_btn = QPushButton('Hinzufügen')

        self.save_btn.setStyleSheet('QWidget {background-color: #00ff00}')
        self.back_btn.setStyleSheet('QWidget {background-color: #ff0000}')
        self.add_mainLang_input_btn.setStyleSheet('QWidget {background-color: #00ff00}')
        self.add_lang_input_btn.setStyleSheet('QWidget {background-color: #00ff00}')
        self.add_cat_comboBox_btn.setStyleSheet('QWidget {background-color: #00ff00}')

        self.vok_input_mainLangName = QLabel()
        self.vok_input_langName = QLabel()

        titleLabel = QLabel('<b>Vokabeln eingeben</b>')
        titleLabel.setFont(QFont('Arial', 15))

        title = QHBoxLayout()
        title.addStretch(1)
        title.addWidget(titleLabel)
        title.addStretch(1)

        self.createMainLang_lineEdit = QLineEdit()
        self.createLang_lineEdit = QLineEdit()
    

        self.createCat_comboBox = QComboBox()
        self.createCat_comboBox.setEditable(True)
        self.createCat_comboBox.addItem('None')
        
        mainScroll = QScrollArea()
        mainScroll.setWidgetResizable(True)
        mainScrollContent = QWidget(mainScroll)
        self.mainScrollLayout = QVBoxLayout(mainScrollContent)
        mainScrollContent.setLayout(self.mainScrollLayout)
        mainScroll.setWidget(mainScrollContent)

        scrollMainLang = QScrollArea()
        scrollMainLang.setWidgetResizable(True)
        scrollContentMainLang = QWidget(scrollMainLang)
        self.scrollMainLangLayout = QVBoxLayout(scrollContentMainLang)
        scrollContentMainLang.setLayout(self.scrollMainLangLayout)
        scrollMainLang.setWidget(scrollContentMainLang)

        scrollLang = QScrollArea()
        scrollLang.setWidgetResizable(True)
        scrollContentLang = QWidget(scrollLang)
        self.scrollLangLayout = QVBoxLayout(scrollContentLang)
        scrollContentLang.setLayout(self.scrollLangLayout)
        scrollLang.setWidget(scrollContentLang)

        scrollCat = QScrollArea()
        scrollCat.setWidgetResizable(True)
        scrollContentCat = QWidget(scrollCat)
        self.scrollCatLayout = QVBoxLayout(scrollContentCat)
        scrollContentCat.setLayout(self.scrollCatLayout)
        scrollCat.setWidget(scrollContentCat)

        hL_mainLang = QHBoxLayout()
        hL_mainLang.addWidget(self.createMainLang_lineEdit)
        hL_mainLang.addWidget(self.add_mainLang_input_btn)

        hL_lang = QHBoxLayout()
        hL_lang.addWidget(self.createLang_lineEdit)
        hL_lang.addWidget(self.add_lang_input_btn)

        hL_cat = QHBoxLayout()
        hL_cat.addWidget(self.createCat_comboBox)
        hL_cat.addWidget(self.add_cat_comboBox_btn)


        hL = QHBoxLayout()
        hL.addWidget(self.back_btn)
        hL.addWidget(self.save_btn)

        vL = QVBoxLayout()
        vL.addLayout(title)
        vL.addWidget(mainScroll)
        vL.addLayout(hL)

        self.mainScrollLayout.addWidget(self.vok_input_mainLangName)
        self.mainScrollLayout.addLayout(hL_mainLang)
        self.mainScrollLayout.addWidget(scrollMainLang)
        self.mainScrollLayout.addStretch(1)

        self.mainScrollLayout.addWidget(self.vok_input_langName)
        self.mainScrollLayout.addLayout(hL_lang)
        self.mainScrollLayout.addWidget(scrollLang)
        self.mainScrollLayout.addStretch(1)

        self.mainScrollLayout.addWidget(QLabel('Kategorien:'))
        self.mainScrollLayout.addLayout(hL_cat)
        self.mainScrollLayout.addWidget(scrollCat)
        self.mainScrollLayout.addStretch(1)

        self.add_mainLang_input_btn.clicked.connect(self.vokInput_add_mainLang)
        self.add_lang_input_btn.clicked.connect(self.vokInput_add_lang)
        self.add_cat_comboBox_btn.clicked.connect(self.vokComboBox_add_cat)
        self.save_btn.clicked.connect(self.add_vok2dict)

        self.createMainLang_lineEdit.returnPressed.connect(self.vokInput_add_mainLang)
        self.createLang_lineEdit.returnPressed.connect(self.vokInput_add_lang)

        self.setLayout(vL)

    def add_vok2dict(self):
        if len(self.new_langList) != 0 or len(self.new_mainLangList) != 0:
            datum = str(date.today())
            if self.lang == 'Englisch':
                vokabel = {'num':len(self.dict)+1, 'de':self.new_mainLangList, 'en':self.new_langList, 'date':datum, 'cat':self.new_catList}
            elif self.lang == 'Französisch':
                vokabel = {'num':len(self.dict)+1, 'de':self.new_mainLangList, 'fr':self.new_langList, 'date':datum, 'cat':self.new_catList}
            self.dict.append(vokabel)
            if self.lang == 'Englisch':
                save_dictionary('en',vokabel)
            elif self.lang == 'Französisch':
                save_dictionary('fr', vokabel)
            self.clearLayout()
            self.createCat_comboBox.clear()
            self.createCat_comboBox.addItem('None')
            self.createCat_comboBox.addItems(sorted(self.cat_list))

    def clearLayout(self):
        self.new_mainLangList = []
        while self.scrollMainLangLayout.count():
            child = self.scrollMainLangLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.new_langList = []
        while self.scrollLangLayout.count():
            child = self.scrollLangLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def vokInput_add_mainLang(self):
        if self.createMainLang_lineEdit.text() not in self.new_mainLangList:
            self.new_mainLangList.append(self.createMainLang_lineEdit.text())
            self.scrollMainLangLayout.addWidget(FlatButton(self, 'vokInputMainLang', str(self.createMainLang_lineEdit.text())))
        self.createMainLang_lineEdit.setText('')

    def vokInput_add_lang(self):
        if self.createLang_lineEdit.text() not in self.new_langList:
            self.new_langList.append(self.createLang_lineEdit.text())
            self.scrollLangLayout.addWidget(FlatButton(self, 'vokInputLang', str(self.createLang_lineEdit.text())))
        self.createLang_lineEdit.setText('')

    def vokComboBox_add_cat(self):
        if self.createCat_comboBox.currentText() not in self.new_catList and self.createCat_comboBox.currentText() != 'None':
            self.new_catList.append(self.createCat_comboBox.currentText())
            self.scrollCatLayout.addWidget(FlatButton(self, 'vokInputCat', str(self.createCat_comboBox.currentText())))
        if self.createCat_comboBox.currentText() not in self.cat_list:
            self.cat_list.append(self.createCat_comboBox.currentText())
            self.createCat_comboBox.clear()
            self.createCat_comboBox.addItem('None')
            self.createCat_comboBox.addItems(sorted(self.cat_list))
        self.createCat_comboBox.setCurrentText('None')

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

    def load(self, mainLang, lang, dict):
        self.mainLang = mainLang
        self.lang = lang
        self.dict = dict
        try:
            self.cat_list = []
            self.createCat_comboBox.clear()
            for vok in self.dict:
                for cat in vok['cat']:
                    if cat not in self.cat_list:
                        self.cat_list.append(cat)
            self.createCat_comboBox.addItem('None')
            self.createCat_comboBox.addItems(sorted(self.cat_list))
        except: pass
        self.new_mainLangList = []
        self.new_langList = []
        self.new_catList = []
        self.vok_input_mainLangName.setText(self.mainLang+':')
        self.vok_input_langName.setText(self.lang+':')