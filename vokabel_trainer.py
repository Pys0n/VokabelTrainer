# Version: v2.3.1  ——Stand: 16.01.2023
# bei Fragen, Problemen oder Update-Ideen: jason.krueger2010@web.de

from os import system
from os.path import exists
import pathlib
from time import sleep
from datetime import date

PATH = str(pathlib.Path(__file__).parent.absolute())
FILENAME = 'vokabeln_en.dat'
FILE_ENGLISCH = PATH+"/"+FILENAME
FILENAME = 'vokabeln_fr.dat'
FILE_FRANZOSISCH = PATH+"/"+FILENAME
FILENAME = 'statistic_en.dat'
FILE_STATISTIC_EN = PATH+"/"+FILENAME
FILENAME = 'statistic_fr.dat'
FILE_STATISTIC_FR = PATH+"/"+FILENAME

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
    RESET  = '\033[0m' # RESET COLOR


def print_list(liste):
    # Diese Funktion gibt die Deutsche(n) Vokabel(n) aus
    for x in range(len(liste)):
        if x > 0:
            print(', ',end='')
        print(liste[x], end='')


def en_vokabeln_eingeben(dictionary_en):
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
        vokabel = {'num':len(dictionary_en)+1, 'de':de, 'en':en, 'date':datum, 'cat':cat}
        print(vokabel)
        print()
        print('Wollen Sie diese Vokabel Speichern?')
        wahl = input('Drücken sie n+<Enter> um die Vokabel nicht zu Speichern \nund nur <Enter> um sie zu Speichern: \n')
        system('clear')
        if wahl == '':
            dictionary_en.append(vokabel)
            save_dictionarys(dictionary_en, dictionary_fr)
        else: pass
        print("<Enter> drücken für weiter")
        char = input("0+<Enter> Hauptmenü:  ")
        system('clear')


def fr_vokabeln_eingeben(dictionary_fr):
    char = ''
    while char == '':
        de = []
        fr = ' '
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
        print(f'-–Sie können nur {Color.UNDERLINE}eine{Color.RESET} Französische Vokabel eingeben!–-')
        print()
        fr = input('Französisch: ')
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
        vokabel = {'num':len(dictionary_fr)+1, 'de':de, 'fr':fr, 'date':datum, 'cat':cat}
        print(vokabel)
        print()
        print('Wollen Sie diese Vokabel Speichern?')
        wahl = input('Drücken sie n+<Enter> um die Vokabel nicht zu Speichern \nund nur <Enter> um sie zu Speichern: \n')
        system('clear')
        if wahl == '':
            dictionary_fr.append(vokabel)
            save_dictionarys(dictionary_en, dictionary_fr)
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
            if vokabel['date'] == auswahl:
                dict_datum.append(vokabel)
        return dict_datum
    elif auswahl == '3':
        dict_cat = []
        print('Bitte geben Sie die gewünschte Kategorie ein:')
        auswahl = input()
        system('clear')
        for vokabel in dictionary:
            if auswahl in vokabel['cat']:
                dict_cat.append(vokabel)
        return dict_cat
        
    assert False, "Es wurde nicht 1,2 oder 3 ausgewählt"

def abfragen_de_en(gefilterte_liste):
    # Diese Funktion beinhaltet die Abfrage der Englischen Vokabeln
    richtig = 0
    falsch = 0
    nichtGewusst = 0
    beantwortet = 0

    for i in range(0, len(gefilterte_liste)):
        vokabel = gefilterte_liste[i]
        print('Deutsch: ', end='')
        print(Color.GREEN, end='')
        print_list(vokabel['de'])
        print(Color.RESET, end='')
        print(f'                                {beantwortet}/{len(gefilterte_liste)}')
        print()
        print(f'Englisch:                                        {Color.CYAN}0 Beenden{Color.RESET}')
        auswahl = input(Color.YELLOW)
        print(Color.RESET, end='')
        if auswahl == vokabel['en']:
            print(Color.GREEN, end='')
            print('Richtig/Right')
            print(Color.RESET, end='')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1
            datum = str(date.today())
            with open(FILE_STATISTIC_EN, 'a') as file:
                file.write(vokabel['num']+';'+'0'+';'+datum+'\n')
        elif auswahl == '':
            print(Color.GREEN, end='')
            print(vokabel['en'], 'wäre Richtig gewesen')
            print(Color.RESET, end='')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_EN, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n')
        elif auswahl == '0':
            system('clear')
            break
        else:
            print(Color.RED, end='')
            print('Falsch/Wrong:')
            print(Color.GREEN, end='')
            print(vokabel['en'])
            print(Color.RESET, end='')
            sleep(5)
            falsch = falsch + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_EN, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n')
        system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    input(f"{Color.CYAN}Weiter mit Enter...{Color.RESET}")
    system('clear')
    

def abfragen_en_de(gefilterte_liste):
    # Diese Funktion beinhaltet die Abfrage der Deutschen Vokabeln
    richtig = 0
    falsch = 0
    nichtGewusst = 0
    beantwortet = 0

    for vokabel in gefilterte_liste:
        print('Englisch: ', end='')
        print(Color.GREEN, end='')
        print(f"{vokabel['en']:30}",end='')
        print(Color.RESET, end='')
        print(f"        {beantwortet}/{len(gefilterte_liste)}")
        print()     
        print(f'Deutsch:                                        {Color.CYAN}0 Beenden{Color.RESET}')
        auswahl = input(Color.YELLOW)
        print(Color.RESET, end='')
        if auswahl in vokabel['de']: 
            print(Color.GREEN, end='')
            print('Richtig/Right')
            print(Color.RESET, end='')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_EN, 'a') as file:
                file.write(vokabel['num']+';'+'0'+';'+datum+'\n')
        elif auswahl == '':
            print(Color.GREEN, end='')
            print_list(vokabel['de'])
            print(' wäre Richtig gewesen')
            print(Color.RESET, end='')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_EN, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n')
        elif auswahl == '0':
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
            datum = str(date.today())
            with open(FILE_STATISTIC_EN, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n')
        system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    input(f"{Color.CYAN}Weiter mit Enter...{Color.RESET}")
    system('clear')


def abfragen_de_fr(gefilterte_liste):
    # Diese Funktion beinhaltet die Abfrage der Französischen Vokabeln
    richtig = 0
    falsch = 0
    nichtGewusst = 0
    beantwortet = 0

    for vokabel in gefilterte_liste:
        print('Deutsch: ', end='')
        print(Color.GREEN, end='')
        print_list(vokabel['de'])
        print(Color.RESET, end='')
        print(f"        {beantwortet}/{len(gefilterte_liste)}")
        print()     
        print(f'Französisch:                                   {Color.CYAN}0 Beenden{Color.RESET}')
        auswahl = input(Color.YELLOW)
        print(Color.RESET, end='')
        if auswahl == vokabel['fr']: 
            print(Color.GREEN, end='')
            print('Richtig/Correct')
            print(Color.RESET, end='')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_FR, 'a') as file:
                file.write(vokabel['num']+';'+'0'+';'+datum+'\n')
        elif auswahl == '':
            print(Color.GREEN, end='')
            print(vokabel['fr'], 'wäre Richtig gewesen')
            print(Color.RESET, end='')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_FR, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n')
        elif auswahl == '0':
            system('clear')
            break
        else:
            print(Color.RED, end='')
            print('Falsch/Faux:')
            print(Color.GREEN, end='')
            print(vokabel['fr'])
            print(Color.RESET, end='')
            sleep(5)
            falsch = falsch + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_FR, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n')
        system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    input(f"{Color.CYAN}Weiter mit Enter...{Color.RESET}")
    system('clear')


def abfragen_fr_de(gefilterte_liste):
    # Diese Funktion beinhaltet die Abfrage der Deutschen Vokabeln
    richtig = 0
    falsch = 0
    nichtGewusst = 0
    beantwortet = 0

    for vokabel in gefilterte_liste:
        print('Französisch: ', end='')
        print(Color.GREEN, end='')
        print(f"{vokabel['fr']:30}",end='')
        print(Color.RESET, end='')
        print(f"        {beantwortet}/{len(gefilterte_liste)}")
        print()     
        print(f'Deutsch:                                        {Color.CYAN}0 Beenden{Color.RESET}')
        auswahl = input(Color.YELLOW)
        print(Color.RESET, end='')
        if auswahl in vokabel['de']: 
            print(Color.GREEN, end='')
            print('Richtig/Correct')
            print(Color.RESET, end='')
            sleep(3)
            richtig = richtig + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_FR, 'a') as file:
                file.write(vokabel['num']+';'+'0'+';'+datum+'\n')
        elif auswahl == '':
            print(Color.GREEN, end='')
            print_list(vokabel['de'])
            print(' wäre Richtig gewesen')
            print(Color.RESET, end='')
            sleep(5)
            nichtGewusst = nichtGewusst + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_FR, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n')
        elif auswahl == '0':
            system('clear')
            break
        else:
            print(Color.RED, end='')
            print('Falsch/Faux:')
            print(Color.GREEN, end='')
            print_list(vokabel['de'])
            print(Color.RESET, end='')
            sleep(5)
            falsch = falsch + 1
            beantwortet = beantwortet + 1 
            datum = str(date.today())
            with open(FILE_STATISTIC_FR, 'a') as file:
                file.write(vokabel['num']+';'+'1'+';'+datum+'\n') 
        system('clear')

    # Auswertung
    print('Fragen richtig beantwortet:', richtig)
    print('Fragen falsch beantwortet :', falsch)
    print('Fragen nicht Gewusst      :', nichtGewusst)
    print('Fragen beantwortet        :', beantwortet,'/',len(gefilterte_liste))
    input(f"{Color.CYAN}Weiter mit Enter...{Color.RESET}")
    system('clear')


def save_dictionarys(dictionary_en, dictionary_fr):
    with open(FILE_ENGLISCH, 'w') as file:
        for vokabel in dictionary_en:
            vokabel_de = ""
            for w in vokabel['de']:
                vokabel_de += w + '|'
            vokabel_de = vokabel_de.rstrip('|')

            vokabel_cat = ""
            for w in vokabel['cat']:
                vokabel_cat += w + '|'
            vokabel_cat = vokabel_cat.rstrip('|')

            file.write(f"{vokabel['num']};{vokabel_de};{vokabel['en']};{vokabel['date']};{vokabel_cat}\n")

    with open(FILE_FRANZOSISCH, 'w') as file:
        for vokabel in dictionary_fr:
            vokabel_de = ""
            for w in vokabel['de']:
                vokabel_de += w + '|'
            vokabel_de = vokabel_de.rstrip('|')

            vokabel_cat = ""
            for w in vokabel['cat']:
                vokabel_cat += w + '|'
            vokabel_cat = vokabel_cat.rstrip('|')

            file.write(f"{vokabel['num']};{vokabel_de};{vokabel['fr']};{vokabel['date']};{vokabel_cat}\n")


def load_dictionarys():
    if not exists(FILE_ENGLISCH):
        print("Datei kann nicht geöffnet werden")
        exit()

    dictionary_en = []
    parsed_lines = []
    with open(FILE_ENGLISCH,'r') as file:
        for line in file:
            line = line.rstrip()
            parsed_lines.append(line.split(';'))

    for line in parsed_lines:
        de = line[1].split('|')
        for i in range(len(de)):
            de[i] = de[i].strip("'")

        cat = line[4].split('|')
        for i in range(len(cat)):
            cat[i] = cat[i].strip("'")

        dictionary_en.append({'num':line[0], 'de':de, 'en':line[2], 'date':line[3], 'cat':cat})
        
    if not exists(FILE_FRANZOSISCH):
        print("Datei kann nicht geöffnet werden")
        exit()

    dictionary_fr = []
    parsed_lines = []
    with open(FILE_FRANZOSISCH,'r') as file:
        for line in file:
            line = line.rstrip()
            parsed_lines.append(line.split(';'))

    for line in parsed_lines:
        de = line[1].split('|')
        for i in range(len(de)):
            de[i] = de[i].strip("'")

        cat = line[4].split('|')
        for i in range(len(cat)):
            cat[i] = cat[i].strip("'")

        dictionary_fr.append({'num':line[0], 'de':de, 'fr':line[2], 'date':line[3], 'cat':cat})

    return dictionary_en, dictionary_fr


def stats():
    system('clear')
    print('         Kommt bald')
    print()
    input('  Drücke <Enter> um Fortzuahren\n\t\t')
    system('clear')


def info():
    system('clear')
    print('         INFO')
    print()
    print(f'{Color.VIOLET}Ersteller{Color.RESET}: Jason Krüger\n')
    print('vAlpha(08.01.2022):')
    print('- Abfrage EN, DE\n')
    print('v1.0.0(13.02.2022):')
    print('- Vokabeln EN eingeben')
    print('- Vokabeln werden dauerhaft abgespeichert\n')
    print('v2.0.0(30.11.2022):')
    print('- Abfrage FR, DE')
    print('- Vokabeln FR eingeben')
    print('v2.0.1(13.01.2023):')
    print('- 44 neue FR-vokabeln\n')
    print('v2.1.0(16.01.2023):')
    print('- Erkennung und Speicherung von Richtig und Falsch\n')
    print('v2.2.0(17.01.2023):')
    print('- num-Funktion für jede Vokael hinzugefügt')
    print('  -> num = jede Vokabel hat eine eigene Nummer(siehe: vokabeln_en.dat/vokabeln_fr.dat)')
    print('- Speicherung von Richtig und Falsch in einer Extra-Datei\n')
    print('v2.3.0(17.01.2023):')
    print('- Speicherung von Richtig und Falsch in einer Extra-Datei überareitet')
    print('  -> für die Statistik\n')
    print('v2.3.1(17.01.2023):')
    print('- kleiner Bug-Fix\n')
    input('  Drücke <Enter> um Fortzuahren\n\t\t')
    system('clear')


def main(dictionary_en, dictionary_fr):
    save_dictionarys(dictionary_en, dictionary_fr)
    system('clear')
    while True:
        print(f'         {Color.BLUE}{Color.UNDERLINE}Vokabelprogramm - Study{Color.RESET}             v2.3.1')
        print()
        print('                Englisch\n')
        print('    1 - Englische Vokabeln abfragen')
        print('    2 - Deutsche Vokabeln abfragen')
        print()
        print('              Französisch\n')
        print('    3 - Französische Vokabeln abfragen')
        print('    4 - Deutsche Vokabeln abfragen')
        print()
        print('    5 - Englische Vokabeln eingeben')
        print('    6 - Französische Vokabeln eingeben')
        print()
        print('    i - Info')
        print('    s - Statistik')
        print()
        print(f'    {Color.CYAN}0 - Beenden{Color.RESET}')
        auswahl = input("\n"+Color.YELLOW)
        print(Color.RESET, end='')
        system('clear')
        if auswahl == '1': 
            gefilterte_liste = abfragen_untermenu(dictionary_en)
            abfragen_de_en(gefilterte_liste)
        elif auswahl == '2':
            gefilterte_liste = abfragen_untermenu(dictionary_en)
            abfragen_en_de(gefilterte_liste)
        elif auswahl == '3':
            gefilterte_liste = abfragen_untermenu(dictionary_fr)
            abfragen_de_fr(gefilterte_liste)
        elif auswahl == '4':
            gefilterte_liste = abfragen_untermenu(dictionary_fr)
            abfragen_fr_de(gefilterte_liste)
        elif auswahl == '5':
            en_vokabeln_eingeben(dictionary_en)
        elif auswahl == '6':
            fr_vokabeln_eingeben(dictionary_fr)
        elif auswahl.lower() == 'i':
            info()
        elif auswahl.lower() == 's':
            stats()
        elif auswahl == '0':
            break


if __name__ == '__main__':
    dictionary_en, dictionary_fr = load_dictionarys()
    main(dictionary_en, dictionary_fr)
    save_dictionarys(dictionary_en, dictionary_fr)