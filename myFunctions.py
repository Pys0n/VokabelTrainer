import pathlib
from os.path import exists
from datetime import date

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

PATH = str(pathlib.Path(__file__).parent.absolute())
FILENAME = 'vokabeln_en.dat'
FILE_ENGLISCH = PATH+"/"+FILENAME
FILENAME = 'vokabeln_fr.dat'
FILE_FRANZOSISCH = PATH+"/"+FILENAME
FILENAME = 'statistic_en.dat'
FILE_STATISTIC_EN = PATH+"/"+FILENAME
FILENAME = 'statistic_fr.dat'
FILE_STATISTIC_FR = PATH+"/"+FILENAME

def save_dictionary(lang, vokabel):
    if lang == 'en':
        file = FILE_ENGLISCH
        try:
            vokabel_lang = vokabel['en']
        except: print('pass')

    if lang == 'fr':
        file = FILE_FRANZOSISCH
        try:
            vokabel_lang = vokabel['fr']
        except: print('pass')

    with open(file, 'a', encoding='utf-8') as file:
        vokabel_de = ""
        for w in vokabel['de']:
            vokabel_de += w + '|'
        vokabel_de = vokabel_de.rstrip('|')

        new_vokabel_lang = ""
        for w in vokabel_lang:
            new_vokabel_lang += w + '|'
        new_vokabel_lang = new_vokabel_lang.rstrip('|')

        vokabel_cat = ""
        for w in vokabel['cat']:
            vokabel_cat += w + '|'
        vokabel_cat = vokabel_cat.rstrip('|')

        file.write(f"{vokabel['num']};{vokabel_de};{new_vokabel_lang};{vokabel['date']};{vokabel_cat}\n")

def load_dictionary_en():
    if not exists(FILE_ENGLISCH):
        print("Datei kann nicht geöffnet werden")
        exit()

    dictionary_en = []
    parsed_lines = []
    with open(FILE_ENGLISCH, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()
            parsed_lines.append(line.split(';'))

    for line in parsed_lines:
        de = line[1].split('|')
        for i in range(len(de)):
            de[i] = de[i].strip("'")

        en = line[2].split('|')
        for i in range(len(en)):
            en[i] = en[i].strip("'")

        cat = line[4].split('|')
        for i in range(len(cat)):
            cat[i] = cat[i].strip("'")

        dictionary_en.append({'num':line[0], 'de':de, 'en':en, 'date':line[3], 'cat':cat})
        
    return dictionary_en

def load_dictionary_fr():

    if not exists(FILE_FRANZOSISCH):
        print("Datei kann nicht geöffnet werden")
        exit()

    dictionary_fr = []
    parsed_lines = []
    with open(FILE_FRANZOSISCH, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()
            parsed_lines.append(line.split(';'))

    for line in parsed_lines:
        de = line[1].split('|')
        for i in range(len(de)):
            de[i] = de[i].strip("'")

        fr = line[2].split('|')
        for i in range(len(fr)):
            fr[i] = fr[i].strip("'")

        cat = line[4].split('|')
        for i in range(len(cat)):
            cat[i] = cat[i].strip("'")

        dictionary_fr.append({'num':line[0], 'de':de, 'fr':fr, 'date':line[3], 'cat':cat})

    return dictionary_fr

def make_string(liste):
    if len(liste) != 1:
        for x in range(len(liste)):
            if x == 0:
                string = liste[x-1]
            else:
                string = string + ', ' + liste[x-1]
    else:
        string = liste[0]
    return string

class FlatButton(QPushButton):
    def __init__(self, catTab, way, label: str):
        self.way = way
        self.catTab  = catTab
        self.label = label
        super(FlatButton, self).__init__()
        self.setText(self.label)
        self.setStyleSheet("border: 0")
        self.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.catTab.deleteButton(self, self.way, self.label)
        self.close()

def get_statistic_today(lang):
    parsed_lines = []
    statistics = {'right':0,'wrong':0,'answered':0}
    try:
        if lang[0] == 'en' or lang[1] == 'en':
            with open(PATH+'/'+'statistic_en.dat', 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.rstrip()
                    parsed_lines.append(line.split(';'))

            for line in parsed_lines:
                if line[2] == str(date.today()):
                    if line[1] == '0':
                        statistics['right'] += 1
                    elif line[1] == '1':
                        statistics['wrong'] += 1
                    statistics['answered'] += 1
    except: pass
    try:
        if lang[0] == 'fr' or lang[1] == 'fr':
            with open(PATH+'/'+'statistic_fr.dat', 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.rstrip()
                    parsed_lines.append(line.split(';'))

            for line in parsed_lines:
                if line[2] == str(date.today()):
                    if line[1] == '0':
                        statistics['right'] += 1
                    elif line[1] == '1':
                        statistics['wrong'] += 1
                    statistics['answered'] += 1    
    except:pass
    return statistics
