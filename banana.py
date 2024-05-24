#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:14:46 2024

@author: lisagerstenberg
"""

def buchstaben_ersetzen(string="banana", alter_buchstabe="a", neuer_buchstabe="eiou"):
    ergebnis = [] # Initialisieren der Ergebnis-Zeichenkette
    
    # Durchlaufe jedes Zeichen (char) in der Eingabezeichenkette (string)
    for char in string:
        # Überprüfe, ob das aktuelle Zeichen gleich dem zu ersetzenden Buchstaben ist (unabhängig von Groß-/Kleinschreibung)
        if char.lower() == alter_buchstabe.lower():
            # Ersetze das Zeichen durch den neuen Buchstaben
            ergebnis += neuer_buchstabe
        else:
            # Behalte das ursprüngliche Zeichen bei
            ergebnis += char
    ergebnis.append(ergebnis)
    
    return ergebnis  # Rückgabe der modifizierten Zeichenkette

# Testen der Funktion
print(buchstaben_ersetzen("banana", "a", "e"))  # Ausgabe: "benene"

     
    