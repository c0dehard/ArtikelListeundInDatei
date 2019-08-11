# -*- coding: UTF-8 -*-
#das encoding sollte drignend drin stehen, gibt sonnst probleme
import os
import sys

objects = {} #leeres dictionary


def countTextinFile():
    file = input("Datei angeben:\n>")
    f = open(file,"r",encoding="utf8")
    content = f.read()
    f.close()
    counts = 0
    lookingfor = input('Häufigkeit von was wird gesucht?\n>')
    for search in content.split():
        if search == lookingfor:
            counts = counts + 1
    print(str("Search in>\n"+file+"\n"+content))
    print(counts,' mal wurde "', lookingfor,'"gefunden')
    input("Beliebige Taste drücken für zurück")

def add():
    global objects
    os.system("cls")#clear für unix systeme
    show()
    print("Artikelnrummer:")
    id = input("> ")
    
    if id in objects: #prüfen ob die eingegebene zahl in der dictionary als Key ist!
        print("Bereits Vorhanden")
    else:
        print("Bitte Gegenstand eingeben")
        name = input("> ")
        
        objects[id] = name
        
    return #geht wohl zurück in die main methode
        

def show():
    global objects
    os.system("cls")#für unix wieder ändern zu clear
    print("Artikel \t Gegenstand")
    
    for gegenstand in objects:
        zeile = str(gegenstand)+" \t "+str(objects[gegenstand])
        print(zeile)
    print("\n")
    return

def speichern():
    global objects
    os.system("cls")
    print("Speichern unter (keine Dateiendung nötig): ")
    datei = input("> ")
    datei = datei +".c0dehard"
    with open(datei, "w")as fh:
        #fh = filehandler, mögliche attribute w write, r read, a append
        fh.write("Artikel \t Gegenstand\n")
        for gegenstand in objects:
            zeile = str(gegenstand)+" \t "+str(objects[gegenstand])+"\n"
            fh.write(zeile)
            
    print("Erfolgreich gespeichert!\n>Zurück mit enter")
    input()
    return()


def delete():
    #global objects #auch hier wieder die globale variable reinholen
    os.system("cls")#bei unix/linux/mac 'clear' 
    show()
    print("Bitte Inventarnummer eingeben:")
    id = input("> ") #id existiert jeweils nur in seinem eigenen scope und stört niemanden!
    if id in objects:
        del(objects[id])  #inbuild option del object an stelle der eingegebenen id aus dem dict löschen
    else:
        print(str(id)+" # Nicht gefunden")
        input()#damit die konsole ofen bleibt
    return 


def showUI():
    os.system("cls")#clear für unix usw!
    print("----------Hauptmenü")
    show()
    print("1) Anlegen\n2) Löschen\n3) Speichern\n4) Häufigkeit\n5) Beenden")

#menü, da es switchcase so wie man es in anderen sprachen kennt 
    try:
        eingabe = int(input("> "))
        if eingabe == 1:
            add()
        elif eingabe == 2:
            delete()
        elif eingabe == 3:
            speichern()
        elif eingabe == 4:
            countTextinFile()
        elif eingabe == 5:
            sys.exit(0)
        else:
            raise Exception("ungültige Eingabe")
        
    except Exception as e:
        print(str(e))
        input()
        showUI()



if __name__ == '__main__':   #mainmethode des programs
    while True:
        showUI()



