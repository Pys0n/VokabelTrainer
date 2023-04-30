from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *


class ChangelogUI(QWidget):

    def __init__(self):
        super(ChangelogUI, self).__init__()
        changelog = QLabel('<b>Changelog</b>')
        changelog.setFont(QFont('Arial', 15))
        updates = QLabel()
        updates.setText('''
                Creator: Jason Krüger

                vAlpha(08.01.2022):
                - Abfrage EN, DE

                v1.0.0(13.02.2022)
                - Vokabeln EN eingeben
                - Vokabeln werden dauerhaft abgespeichert

                v2.0.0(30.11.2022):
                - Abfrage FR, DE
                - Vokabeln FR eingeben

                v2.0.1(13.01.2023):
                - 44 neue FR-vokabeln

                v2.1.0(16.01.2023):
                - Erkennung und Speicherung von Richtig und Falsch

                v2.2.0(17.01.2023):
                - num-Funktion für jede Vokabel hinzugefügt
                  -> num = jede Vokabel hat eine eigene Nummer(siehe: vokabeln_en.dat/vokabeln_fr.dat)
                - Speicherung von Richtig und Falsch in einer Extra-Datei

                v2.3.0(17.01.2023):
                - Speicherung von Richtig und Falsch in einer Extra-Datei überareitet
                  -> für die Statistik
                
                v2.3.1(18.01.2023):
                - kleiner Bug-Fix

                v2.3.2(19.01.2023):
                - Zufällige Reihnfolge bei der Vokabelabfrage

                v2.3.3(27.02.2023):
                - kleiner Bug-Fix

                v2.3.4(06.03.2023):
                - 2 kleine Bug-Fixes

                v3.0.0(04.04.2023):
                - GUI hinzugefügt(PyQt5)
                - Fenster in Extra Datein verschoben
                - Funktionen in die Datei "myFunctions" verschoben
                - mehrere Bug-Fixes
                - Vokabeleingabe: mehrere Vokabeln einer Fremdsprache möglich
                - Vokabeldatein: Probleme gelöst
                - Untermenüs überarbeitet
                - Vokabelabfragen in Untermenüs verschoben
                - Vokabeleingabe, Vokabelabfrage: kompatibel mit allen Sprachen
                - Zufällig abfragen hinzugefügt
                - Kategorien filtern: mehrere möglich, Anzeige welche Kategorien es gibt
                - 610 neue Englische Vokabeln
                  -> Kl. 2, Kl. 3 komplett
                  -> Kl. 4, Kl. 7 angefangen 
                - 269 neue Französische Vokabeln

                v3.1.0(22.04.2023):
                - Statistik Heute hinzugefügt
                - .gitignore aktualisiert
              
                v3.1.1(29.04.2023):
                - encoding = 'utf-8' hinzugefügt
                  -> Windowsproblem behoben
                - save_dictionary-Funktionen zusammengefasst
                - Bug-Fix

                v3.1.2(30.04.2023):
                - load_dictionary-Funktionen zusammengefasst
                - Debug Ausgaben entfernt
        ''')

        self.back_btn = QPushButton('Zurück')
        self.back_btn.setStyleSheet('QWidget {background-color: #ff0000}')


        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        scroll.setWidget(updates)

        hL = QHBoxLayout()
        hL.addStretch(1)
        hL.addWidget(changelog)
        hL.addStretch(1)

        vL = QVBoxLayout()
        vL.addLayout(hL)
        vL.addWidget(scroll)
        vL.addWidget(self.back_btn)

        #self.back_btn.clicked.connect(self.setMAIN)

        self.setLayout(vL)

    def showEvent(self, event):
        pass

    def load(self):
        pass