from time import sleep
from vokabeln import *
import os

def print_list(liste):
    # Diese Funktion gibt die Deutsche(n) Vokabel(n) aus
    for x in range(len(liste)):
        if x > 0:
            print(', ',end='')
        print(liste[x], end='')
    print()

def abfragen_de_untermenu():
    """
        1. Alle Vokabeln
        2. Nach Datum
        3. Nach Kategorie

        _ (Z)ufällig
    """

def abfragen_de():
    # Diese Funktion beinhaltet die Abfrage der Deutschen Vokabeln
    while True:
        richtig = 0
        falsch = 0
        nichtGewusst = 0
        beantwortet = 0

        Eingabe1 = int(input('Wie viele Vokabeln sollen abgefragt werden? '))
        sleep(1)
        os.system('clear')
        print('OK')
        sleep(1)
        os.system('clear')
        print('Los geht´s!!')
        sleep(1)
        os.system('clear')
        for i in range(Eingabe1):
            vokabel = dictionary[i]
            print('Deutsch: ', end='')
            print_list(vokabel.de)
            print()
            print('Englisch:                                        0.Beenden')
            Eingabe = input()
            if Eingabe == vokabel.en:
                print('Richtig/Right')
                sleep(3)
                richtig = richtig + 1
                beantwortet = beantwortet + 1 
            elif Eingabe == '':
                print(vokabel.en, 'wäre Richtig gewesen')
                sleep(5)
                nichtGewusst = nichtGewusst + 1
                beantwortet = beantwortet + 1 
            elif Eingabe == '0':
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
        print('Fragen beantwortet        :', beantwortet,'/',Eingabe1)
        input("Weiter mit Enter...")
        os.system('clear')
    

def abfragen_en():
    # Diese Funktion beinhaltet die Abfrage der Englischen Vokabeln
    while True:
        richtig = 0
        falsch = 0
        nichtGewusst = 0
        beantwortet = 0

        Eingabe1 = int(input('Wie viele Vokabeln sollen abgefragt werden? '))
        sleep(1)
        os.system('clear')
        print('OK')
        sleep(1)
        os.system('clear')
        print('Los geht´s!!')
        sleep(1)
        os.system('clear')
        for i in range(Eingabe1):
            vokabel = dictionary[i]
            print('Englisch: ', end='')
            print(vokabel.en)
            print()     
            print('Deutsch:                                        0.Beenden')
            Eingabe = input()
            if Eingabe in vokabel.de:
                print('Richtig/Right')
                sleep(3)
                richtig = richtig + 1
                beantwortet = beantwortet + 1 
            elif Eingabe == '':
                print(vokabel.de, 'wäre Richtig gewesen')
                sleep(5)
                nichtGewusst = nichtGewusst + 1
                beantwortet = beantwortet + 1 
            elif Eingabe == '0':
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
        print('Fragen nicht Gewusst      :', nichtGewusst,'/',Eingabe1)
        input("Weiter mit Enter...")
        os.system('clear')


os.system('clear')
# Hauptprogramm:
while True:
    print('    Vokabelprogramm - Study          Ersteller: Jason Krüger')
    print()
    print('    1 Englische Vokabeln abfragen')
    print('    2 Deutsche Vokalen abfragen')
    print()
    print('    5 Vokabeln eingeben')
    print('    6 Statistik')
    print()
    print('    0 Beenden')
    Eingabe = int(input())
    os.system('clear')
    if Eingabe == 1:
        abfragen_de()
    elif Eingabe == 2:
        abfragen_en()
    elif Eingabe == 5:
        pass
    elif Eingabe == 6:
        pass
    elif Eingabe == 0:
        break
