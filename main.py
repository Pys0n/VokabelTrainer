import sys
from random import shuffle, randint
from datetime import date

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

from mainmenu_ui import MainmenuUI
from statistic_ui import StatisticUI
from changelog_ui import ChangelogUI
from languagemenu_ui import LanguagemenuUI
from vocabularyinput_ui import VocabularyinputUI
from searchcategory_ui import SearchcategoryUI
from vocabularyquery_ui import VocabularyqueryUI
from myFunctions import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.mainmenu_ui = MainmenuUI()
        self.vocabularyquery_ui = VocabularyqueryUI()
        self.languagemenu_ui = LanguagemenuUI()
        self.changelog_ui = ChangelogUI()
        self.searchcategory_ui = SearchcategoryUI()
        self.vocabularyinput_ui = VocabularyinputUI()
        self.statistic_ui = StatisticUI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.mainmenu_ui)
        self.Stack.addWidget(self.vocabularyquery_ui)
        self.Stack.addWidget(self.languagemenu_ui)
        self.Stack.addWidget(self.changelog_ui)
        self.Stack.addWidget(self.searchcategory_ui)
        self.Stack.addWidget(self.vocabularyinput_ui)
        self.Stack.addWidget(self.statistic_ui)

        # statistic_ui
        self.statistic_ui.next_btn.clicked.connect(self.setMenu)
        # changelog_ui
        self.changelog_ui.back_btn.clicked.connect(self.setMAIN)
        # mainmenu_ui
        self.mainmenu_ui.en.clicked.connect(self.setEN_MENU)
        self.mainmenu_ui.fr.clicked.connect(self.setFR_MENU)
        self.mainmenu_ui.changelog_btn.clicked.connect(self.setCHANGELOG)
        #self.mainmenu_ui.stat_btn.clicked.connect(self.stat)
        self.mainmenu_ui.quit_btn.clicked.connect(self.quit)
        # languagemenu_ui
        self.languagemenu_ui.back_btn.clicked.connect(self.setMAIN)
        # vocabularyinput_ui
        self.vocabularyinput_ui.back_btn.clicked.connect(self.back)
        # searchcategory_ui
        self.searchcategory_ui.save_btn.clicked.connect(self.setMenu)
        # vocabularyquery_ui
        self.vocabularyquery_ui.back_btn.clicked.connect(self.showSTATS) 
        self.vocabularyquery_ui.ready_btn.clicked.connect(self.btnNextClicked) 
        self.vocabularyquery_ui.input.returnPressed.connect(self.btnNextClicked)

        hL = QHBoxLayout()
        hL.addStretch(1)
        hL.addWidget(self.Stack)
        hL.addStretch(1)

        self.setLayout(hL)

        self.setGeometry(100,100,450,500)
        self.setWindowTitle('Vokabeltrainer')
        self.setMAIN()

    def setMAIN(self):
        self.searchcategory_ui.choosedCats = []
        self.searchcategory_ui.clearCats()
        self.mainmenu_ui.load()
        self.Stack.setCurrentIndex(0)

    def setDE_EN(self):
        self.dict = load_dictionary_en()
        if len(self.searchcategory_ui.choosedCats) != 0:
            self.makeDict()
        shuffle(self.dict)
        self.mainLang = 'de'
        self.mainLangName = 'Deutsch'
        self.lang = 'en'
        self.langName = 'Englisch'
        self.vocabularyquery_ui.load(self.dict, ['de', 'Deutsch', 'en', 'Englisch'], False)
        self.Stack.setCurrentIndex(1)

    def setEN_MENU(self):
        self.clearVokInput()
        self.languagemenu_ui.load('Englisch')
        self.languagemenu_ui.lang_mainLang.clicked.connect(self.setEN_DE)
        self.languagemenu_ui.mainLang_lang.clicked.connect(self.setDE_EN)
        self.languagemenu_ui.vok_eingabe.clicked.connect(self.setVOK_INPUT_EN)
        self.languagemenu_ui.random_btn.clicked.connect(self.setEN_RANDOM)
        self.languagemenu_ui.cat_btn.clicked.connect(self.setEN_CATEGORY)
        self.Stack.setCurrentIndex(2)
    
    def setEN_DE(self):
        self.dict = load_dictionary_en()
        if len(self.searchcategory_ui.choosedCats) != 0:
            self.makeDict()
        shuffle(self.dict)
        self.mainLang = 'en'
        self.mainLangName = 'Englisch'
        self.lang = 'de'
        self.langName = 'Deutsch'
        self.vocabularyquery_ui.load(self.dict, ['en', 'Englisch', 'de', 'Deutsch'], False)
        self.Stack.setCurrentIndex(1)

    def setEN_RANDOM(self):
        self.dict = load_dictionary_en()
        if len(self.searchcategory_ui.choosedCats) != 0:
            self.makeDict()
        shuffle(self.dict)
        self.mainLang = 'en'
        self.mainLangName = 'Englisch'
        self.lang = 'de'
        self.langName = 'Deutsch'
        self.vocabularyquery_ui.load(self.dict, ['en', 'Englisch', 'de', 'Deutsch'], True)
        self.Stack.setCurrentIndex(1)

    def setDE_FR(self):
        self.dict = load_dictionary_fr()
        if len(self.searchcategory_ui.choosedCats) != 0:
            self.makeDict()
        shuffle(self.dict)
        self.mainLang = 'de'
        self.mainLangName = 'Deutsch'
        self.lang = 'fr'
        self.langName = 'Französisch'
        self.vocabularyquery_ui.load(self.dict, ['de', 'Deutsch', 'fr', 'Französisch'], False)
        self.Stack.setCurrentIndex(1)

    def setFR_MENU(self):
        self.clearVokInput()
        self.languagemenu_ui.load('Französisch')
        self.languagemenu_ui.lang_mainLang.clicked.connect(self.setFR_DE)
        self.languagemenu_ui.mainLang_lang.clicked.connect(self.setDE_FR)
        self.languagemenu_ui.vok_eingabe.clicked.connect(self.setVOK_INPUT_FR)
        self.languagemenu_ui.random_btn.clicked.connect(self.setFR_RANDOM)
        self.languagemenu_ui.cat_btn.clicked.connect(self.setFR_CATEGORY)
        self.Stack.setCurrentIndex(2)

    def setFR_DE(self):
        self.dict = load_dictionary_fr()
        if len(self.searchcategory_ui.choosedCats) != 0:
            self.makeDict()
        shuffle(self.dict)
        self.mainLang = 'fr'
        self.mainLangName = 'Französisch'
        self.lang = 'de'
        self.langName = 'Deutsch'
        self.vocabularyquery_ui.load(self.dict, ['fr', 'Französisch', 'de', 'Deutsch'], False)
        self.Stack.setCurrentIndex(1)

    def setFR_RANDOM(self):
        self.dict = load_dictionary_fr()
        if len(self.searchcategory_ui.choosedCats) != 0:
            self.makeDict()
        shuffle(self.dict)
        self.mainLang = 'fr'
        self.mainLangName = 'Französisch'
        self.lang = 'de'
        self.langName = 'Deutsch'
        self.vocabularyquery_ui.load(self.dict, ['fr', 'Französisch', 'de', 'Deutsch'], True)
        self.Stack.setCurrentIndex(1)

    def setCHANGELOG(self):
        self.changelog_ui.load()
        self.Stack.setCurrentIndex(3)

    def setEN_CATEGORY(self):
        self.dict = load_dictionary_en()
        self.lang = 'en'
        self.searchcategory_ui.load(self.lang, self.dict)
        self.Stack.setCurrentIndex(4)

    def setFR_CATEGORY(self):
        self.dict = load_dictionary_fr()
        self.lang = 'fr'
        self.searchcategory_ui.load(self.lang, self.dict)
        self.Stack.setCurrentIndex(4)

    def setVOK_INPUT_EN(self):
        self.dict = load_dictionary_en()
        self.mainLang = 'Deutsch'
        self.lang = 'Englisch'
        self.vocabularyinput_ui.load(self.mainLang, self.lang, self.dict)
        self.Stack.setCurrentIndex(5)

    def setVOK_INPUT_FR(self):
        self.dict = load_dictionary_fr()
        self.mainLang = 'Deutsch'
        self.lang = 'Französisch'
        self.vocabularyinput_ui.load(self.mainLang, self.lang, self.dict)
        self.Stack.setCurrentIndex(5)

    def showSTATS(self):
        self.right = self.vocabularyquery_ui.right
        self.wrong = self.vocabularyquery_ui.wrong
        self.answered = self.vocabularyquery_ui.answered
        self.lang = [self.vocabularyquery_ui.lang, self.vocabularyquery_ui.mainLang]
        self.statistic_ui.setStatistic(self.right, self.wrong, self.answered, len(self.dict), self.lang)
        self.Stack.setCurrentIndex(6)

    def quit(self):
        exit()

    def btnNextClicked(self):
        # vocabularyquery_ui.
        if self.lang == 'en' or self.mainLang == 'en':
            FILE_STATISTIC = FILE_STATISTIC_EN
        elif self.lang == 'fr' or self.mainLang == 'fr':
            FILE_STATISTIC = FILE_STATISTIC_FR

        try:
            correct = make_string(self.dict[self.vocabularyquery_ui.run][self.lang])
        
            word = make_string(self.dict[self.vocabularyquery_ui.run][self.mainLang])
        
            datum = str(date.today())
            with open(FILE_STATISTIC, 'a') as file:
                if self.vocabularyquery_ui.input.text() in self.dict[self.vocabularyquery_ui.run][self.lang]:
                    file.write(self.dict[self.vocabularyquery_ui.run]['num']+';'+'0'+';'+datum+'\n')
                    self.vocabularyquery_ui.last.setText(f'<b style="color: #00ff00">Richtig</b><br>{self.mainLangName}: {word}<br>{self.langName}: {correct}\n')
                    self.vocabularyquery_ui.right = self.vocabularyquery_ui.right + 1
                else:
                    file.write(self.dict[self.vocabularyquery_ui.run]['num']+';'+'1'+';'+datum+'\n')
                    self.vocabularyquery_ui.last.setText(f'<b style="color: #ff0000">Falsch</b><br>{self.mainLangName}: {word}<br>{self.langName}: {correct}<br>Deine Antwort: {self.vocabularyquery_ui.input.text()}')
                    self.vocabularyquery_ui.wrong = self.vocabularyquery_ui.wrong + 1
                self.vocabularyquery_ui.answered = self.vocabularyquery_ui.answered + 1

        except: pass

        if self.vocabularyquery_ui.run < len(self.dict)-1:
            if self.vocabularyquery_ui.random:
                shuffleList = [self.mainLang, self.mainLangName, self.lang, self.langName]
                num = randint(1,2)
                if num == 1:
                    self.lang = shuffleList[0]
                    self.langName = shuffleList[1]
                    self.mainLang = shuffleList[2]
                    self.mainLangName = shuffleList[3]
                elif num == 2:
                    self.mainLang = shuffleList[0]
                    self.mainLangName = shuffleList[1]
                    self.lang = shuffleList[2]
                    self.langName = shuffleList[3]
                self.vocabularyquery_ui.mainLangLabel.setText(self.mainLangName+':')
                self.vocabularyquery_ui.langLabel.setText(self.langName+':')
            self.vocabularyquery_ui.run += 1
            try:
                if make_string(self.dict[self.vocabularyquery_ui.run][self.mainLang]) != correct:
                    self.vocabularyquery_ui.vok.setText(make_string(self.dict[self.vocabularyquery_ui.run][self.mainLang]))
                    self.vocabularyquery_ui.input.setText('')
                else:
                    if self.vocabularyquery_ui.right != 0 and self.vocabularyquery_ui.wrong != 0:
                        self.showSTATS()
            except:
                self.vocabularyquery_ui.input.setText('')
        else:
            if self.vocabularyquery_ui.right != 0 and self.vocabularyquery_ui.wrong != 0:
                self.showSTATS()

    def goMain(self):
        self.searchcategory_ui.categories.clear()
        self.searchcategory_ui.categories.addItem('None')
        self.setMAIN()

    def clearVokInput(self):
        self.vocabularyinput_ui.new_mainLangList = []
        while self.vocabularyinput_ui.scrollMainLangLayout.count():
            child = self.vocabularyinput_ui.scrollMainLangLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.vocabularyinput_ui.new_langList = []
        while self.vocabularyinput_ui.scrollLangLayout.count():
            child = self.vocabularyinput_ui.scrollLangLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.vocabularyinput_ui.new_catList = []
        while self.vocabularyinput_ui.scrollCatLayout.count():
            child = self.vocabularyinput_ui.scrollCatLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def makeDict(self):
        for cat in self.searchcategory_ui.choosedCats:
            newDict = []
            for vok in self.dict:
                if cat in vok['cat']:
                    newDict.append(vok)
            self.dict = newDict

    def setMenu(self):
        self.makeDict()
        try:
            if self.lang == 'en' or self.mainLang == 'en':
                self.setEN_MENU()
            elif self.lang == 'fr' or self.mainLang == 'fr':
                self.setFR_MENU()
        except:
            if self.lang == 'en':
                self.setEN_MENU()
            elif self.lang == 'fr':
                self.setFR_MENU()

    def back(self):
        if self.lang == 'Englisch' or self.mainLang == 'Englisch':
            self.setEN_MENU()
        elif self.lang == 'Französisch' or self.mainLang == 'Französisch':
            self.setFR_MENU()

def main():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()