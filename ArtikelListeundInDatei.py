#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
objects = {} #dictionary

def countTextinFile():
    file = input("Datei angeben:\n>");f = open(file,"r",encoding="utf8");content = f.read();f.close()
    counts,lookingfor = 0,input('Häufigkeit von was wird gesucht?\n>')
    for search in content.split():
        if search == lookingfor:counts = counts + 1
    print(str("Search in>\n"+file+"\n"+content));print(counts,' mal wurde "', lookingfor,'"gefunden');input("Beliebige Taste drücken für zurück")

def add():
    global objects;os.system('cls' if os.name == 'nt' else 'clear');show()
    print("Artikelnrummer:")
    id = input("> ")
    
    if id in objects:
        print("Bereits Vorhanden")
    else:
        print("Bitte Gegenstand eingeben")
        name,objects[id] = input("> "),name
    return
        
def show():
    global objects
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Artikel \t Gegenstand")
    
    for gegenstand in objects:
        zeile = str(gegenstand)+" \t "+str(objects[gegenstand]);print(zeile)
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
        for gegenstand in objects:zeile = str(gegenstand)+" \t "+str(objects[gegenstand])+"\n";fh.write(zeile)
    print("Erfolgreich gespeichert!\n>Zurück mit enter");input()
    return()


def delete():
    os.system('cls' if os.name == 'nt' else 'clear');show()
    print("Bitte Inventarnummer eingeben:");id = input("> ")
    if id in objects:del(objects[id])
    else:print(str(id)+" # Nicht gefunden");input()


def showUI():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----------Hauptmenü\n1) Anlegen\n2) Löschen\n3) Speichern\n4) Häufigkeit\n5) Beenden");show()
    try:
        eingabe = int(input("> "))
        if eingabe == 1:add()
        elif eingabe == 2:delete()
        elif eingabe == 3:speichern()
        elif eingabe == 4:countTextinFile()
        elif eingabe == 5:sys.exit(0)
        else:raise Exception("ungültige Eingabe")
    except Exception as e:print(str(e));input();showUI()

if __name__ == '__main__': 
    while True:
        showUI()


