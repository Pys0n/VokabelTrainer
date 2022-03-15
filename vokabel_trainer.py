from os import system
from os.path import exists
import pathlib
from time import sleep
from collections import namedtuple
from datetime import date

Vokabel = namedtuple("Vokabel", ["de","en","date","cat",])  # 'stat' hinzufügen
FILENAME = 'vokabeln.dat'
PATH = str(pathlib.Path(__file__).parent.absolute())
FILE = PATH+"/"+FILENAME


class Color:
    UNDERLINE = '\033[4m'
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    CYAN   = '\33[36m'
    WHITE  = '\33[37m'
    RESET  = '\033[0m' #RESET COLOR


def print_list(liste):
    # Diese Funktion gibt die Deutsche(n) Vokabel(n) aus
    for x in range(len(liste)):
        if x > 0:
            print(', ',end='')
        print(liste[x], end='')


def vokabeln_eingeben(dictionary):
    char = ''
    while char == '':
        de = []
        en = ' '
        cat = []
        i = 1
        print(f"\t{Color.BLUE}{Color.UNDERLINE}Vokabeln eingeben{Color.RESET}")
        print()
        print('-–Drücken Sie <Enter> wenn sie alle Vokabeln Eingegeben haben–-')
        print()
        while True:
            print(i, end='')
            deutsch = input('. Deutsch: ')
            if len(deutsch) > 0:
                de.append(deutsch)
                i += 1
            else: break
        print()
        i = 1
        print(f'-–Sie können nur {Color.UNDERLINE}eine{Color.RESET} Englische Vokabel eingeben!–-')
        print()
        en = input('Englisch: ')
        print()
        #print('-–Dies ist ein Pflichtfeld!–- -–Bitte geben Sie "Kl. ..." für die Klasse an–-')
        category = input('Klasse: ')
        cat.append("Kl. " + category)
        i = 2
        while True:
            print(i, end='')
            category = input('. Kategorie: ')
            if len(category):
                cat.append(category)
                i += 1
            else:
                break
        system('clear')
        datum = str(date.today())
        vokabel = Vokabel(de, en, datum, cat)
        print(vokabel)
        print()
        print('Wollen Sie diese Vokabel Speichern?')
        wahl = input('Drücken sie n+<Enter> um die Vokabel nicht zu Speichern \nund nur <Enter> um sie zu Speichern: \n')
        system('clear')
        if wahl == '':
            dictionary.append(vokabel)
            save_dictionary(dictionary)
        else: pass
        print("<Enter> drücken für weiter")
        char = input("0+<Enter> Hauptmenü:  ")
        system('clear')


def abfragen_untermenu(dictionary):
    print('1. Alle Vokabeln ')
    print('2. Nach Datum    ')
    print('3. Nach Kategorie')
    print()
    auswahl = input(Color.YELLOW)
    print(Color.RESET, end='')
    system('clear')
    if auswahl == '1':
        return dictionary
    elif auswahl == '2':
        dict_datum = []
        print('Bitte geben Sie das gewünschte Datum im Format "jjjj-mm-tt" ein:')
        auswahl = input()
        system('clear')
        for vokabel in dictionary:
            if vokabel.date == auswahl:
                dict_datum.append(vokabel)
        return dict_datum
    elif auswahl == '3':
        dict_cat = []
        print('Bitte geben Sie die gewünschte Kategorie ein:')
        auswahl = input()
        system('clear')
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
        print(Color.GREEN, end='')
        print_list(vokabel.de)
        print(Color.RESET, end='')
        print(f'                                {beantwortet}/{len(gefilterte_liste)}')
        print()
        print(f'Englisch:                                        {Color.CYAN}0 Beenden{Color.RESET}')
        auswahl = input(Color.YELLOW)
        print(Color.RESET, end='')
        if auswahl.lower() == vokabel.en.lower():
            print(Color.GREEN, end='')
            print('Richtig/Right')
            print(Color.RESET, end='')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1 
        elif auswahl.lower() == '':
            print(Color.GREEN, end='')
            print(vokabel.en, end='')
            print(' wäre Richtig gewesen')
            print(Color.RESET, end='')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
        elif auswahl.lower() == '0':
            system('clear')
            break
        else:
            print(Color.RED, end='')
            print('Falsch/Wrong:')
            print(Color.GREEN, end='')
            print(vokabel.en)
            print(Color.RESET, end='')
            sleep(5)
            falsch = falsch + 1
            beantwortet = beantwortet + 1 
        system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    input(f"{Color.CYAN}Weiter mit Enter...{Color.RESET}")
    system('clear')
    

def abfragen_de(gefilterte_liste):
    # Diese Funktion beinhaltet die Abfrage der Englischen Vokabeln
    richtig = 0
    falsch = 0
    nichtGewusst = 0
    beantwortet = 0

    for vokabel in gefilterte_liste:
        print('Englisch: ', end='')
        print(Color.GREEN, end='')
        print(f"{vokabel.en:30}",end='')
        print(Color.RESET, end='')
        print(f"        {beantwortet}/{len(gefilterte_liste)}")
        print()     
        print(f'Deutsch:                                        {Color.CYAN}0 Beenden{Color.RESET}')
        auswahl = input(Color.YELLOW)
        print(Color.RESET, end='')
        if auswahl.lower() in vokabel.de.lower():
            print(Color.GREEN, end='')
            print('Richtig/Right')
            print(Color.RESET, end='')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1 
        elif auswahl.lower() == '':
            print(Color.GREEN, end='')
            print_list(vokabel.de)
            print(' wäre Richtig gewesen')
            print(Color.RESET, end='')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
        elif auswahl.lower() == '0':
            system('clear')
            break
        else:
            print(Color.RED, end='')
            print('Falsch/Wrong:')
            print(Color.GREEN, end='')
            print_list(vokabel.de)
            print(Color.RESET, end='')
            sleep(5)
            falsch = falsch + 1
            beantwortet = beantwortet + 1 
        system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    print(f'{Color.CYAN}0 Beenden{Color.RESET}')
    system('clear')


def save_dictionary(dictionary):
    with open(FILE, 'w') as file:
        for vokabel in dictionary:
            vokabel_de = ""
            for w in vokabel.de:
                vokabel_de += w + '|'
            vokabel_de = vokabel_de.rstrip('|')

            vokabel_cat = ""
            for w in vokabel.cat:
                vokabel_cat += w + '|'
            vokabel_cat = vokabel_cat.rstrip('|')

            file.write(f"{vokabel_de};{vokabel.en};{vokabel.date};{vokabel_cat}\n")


def load_dictionary():
    if not exists(FILE):
        print("Datei kann nicht geöffnet werden")
        exit()

    Vokabel = namedtuple("Vokabel", ["de","en","date","cat"])
    dictionary = []
    parsed_lines = []
    with open(FILE,'r') as file:
        for line in file:
            line = line.rstrip()
            parsed_lines.append(line.split(';'))

    for line in parsed_lines:
        de = line[0].split('|')
        for i in range(len(de)):
            de[i] = de[i].strip("'")

        cat = line[3].split('|')
        for i in range(len(cat)):
            cat[i] = cat[i].strip("'")

        dictionary.append(Vokabel(de, line[1], line[2], cat))
        
    return dictionary


def main(dictionary):
    system('clear')
    while True:
        print(f'    {Color.BLUE}{Color.UNDERLINE}Vokabelprogramm - Study{Color.RESET}          {Color.VIOLET}Ersteller{Color.RESET}: Jason Krüger')
        print()
        print('    1 - Englische Vokabeln abfragen')
        print('    2 - Deutsche Vokabeln abfragen')
        print()
        print('    5 - Vokabeln eingeben')
        print('    6 - Statistik')
        print()
        print(f'    {Color.CYAN}0 - Beenden{Color.RESET}')
        auswahl = int(input("\n"+Color.YELLOW))
        print(Color.RESET, end='')
        system('clear')
        if auswahl == 1: 
            gefilterte_liste = abfragen_untermenu(dictionary)
            abfragen_en(gefilterte_liste)
        elif auswahl == 2:
            gefilterte_liste = abfragen_untermenu(dictionary)
            abfragen_de(gefilterte_liste)
        elif auswahl == 5:
            vokabeln_eingeben(dictionary)
        elif auswahl == 6:
            pass
        elif auswahl == 0:
            break


if __name__ == '__main__':
    dictionary = load_dictionary()
    main(dictionary)
