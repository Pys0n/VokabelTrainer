from time import sleep
from vokabeln import *
import os

def print_list(liste):
    # Diese Funktion gibt die Deutsche(n) Vokabel(n) aus
    for x in range(len(liste)):
        if x > 0:
            print(', ',end='')
        print(liste[x], end='')


def abfragen_untermenu(dictionary):
    print('1. Alle Vokabeln ')
    print('2. Nach Datum    ')
    print('3. Nach Kategorie')
    print()
    auswahl = input()
    os.system('clear')
    if auswahl == '1':
        return dictionary
    elif auswahl == '2':
        dict_datum = []
        print('Bitte geben Sie das gewünschte Datum ein:')
        auswahl = input()
        os.system('clear')
        for vokabel in dictionary:
            if vokabel.date == auswahl:
                dict_datum.append(vokabel)
        return dict_datum
    elif auswahl == '3':
        dict_cat = []
        print('Bitte geben Sie die gewünschte Kategorie ein:')
        auswahl = input()
        os.system('clear')
        for vokabel in dictionary:
            if auswahl in vokabel.cat:
                dict_cat.append(vokabel)
        return dict_cat
        
    assert False, "Es wurde nicht 1,2 oder 3 ausgewählt"

def abfragen_en(gefilterte_liste):
    # Diese Funktion beinhaltet die Abfrage der Deutschen Vokabeln
    richtig = 0
    falsch = 0
    nichtGewusst = 0
    beantwortet = 0

    for i in range(0, len(gefilterte_liste)):
        vokabel = gefilterte_liste[i]
        print('Deutsch: ', end='')
        print_list(vokabel.de)
        print(f'                                {beantwortet}/{len(gefilterte_liste)}')
        print()
        print('Englisch:                                        0.Beenden')
        auswahl = input()
        if auswahl == vokabel.en:
            print('Richtig/Right')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1 
        elif auswahl == '':
            print(vokabel.en, 'wäre Richtig gewesen')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
        elif auswahl == '0':
            os.system('clear')
            break
        else:
            print('Falsch/Wrong:')
            print(vokabel.en)
            sleep(5)
            falsch = falsch + 1
            beantwortet = beantwortet + 1 
        os.system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    input("Weiter mit Enter...")
    os.system('clear')
    

def abfragen_de(gefilterte_liste):
    # Diese Funktion beinhaltet die Abfrage der Englischen Vokabeln
    richtig = 0
    falsch = 0
    nichtGewusst = 0
    beantwortet = 0

    for vokabel in gefilterte_liste:
        print('Englisch: ', end='')
        print(f"{vokabel.en:30}        {beantwortet}/{len(gefilterte_liste)}")
        print()     
        print('Deutsch:                                        0.Beenden')
        auswahl = input()
        if auswahl in vokabel.de:
            print('Richtig/Right')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1 
        elif auswahl == '':
            print_list(vokabel.de)
            print(' wäre Richtig gewesen')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
        elif auswahl == '0':
            os.system('clear')
            break
        else:
            print('Falsch/Wrong:')
            print(vokabel.de)
            sleep(5)
            falsch = falsch + 1
            beantwortet = beantwortet + 1 
        os.system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    input("Weiter mit Enter...")
    os.system('clear')


def main():
    os.system('clear')
    while True:
        print('    Vokabelprogramm - Study          Ersteller: Jason Krüger')
        print()
        print('    1 Englische Vokabeln abfragen')
        print('    2 Deutsche Vokabeln abfragen')
        print()
        print('    5 Vokabeln eingeben')
        print('    6 Statistik')
        print()
        print('    0 Beenden')
        auswahl = int(input())
        os.system('clear')
        if auswahl == 1: 
            gefilterte_liste = abfragen_untermenu(dictionary)
            abfragen_en(gefilterte_liste)
        elif auswahl == 2:
            gefilterte_liste = abfragen_untermenu(dictionary)
            abfragen_de(gefilterte_liste)
        elif auswahl == 5:
            pass
        elif auswahl == 6:
            pass
        elif auswahl == 0:
            break

main()