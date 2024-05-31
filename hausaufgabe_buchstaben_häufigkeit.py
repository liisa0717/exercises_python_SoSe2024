#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:22:57 2024

@author: lisagerstenberg
"""

def buchstaben_häufigkeit(s):
    # Initialisiere ein leeres Dictionary
    haeufigkeit = {}
    
    # Iteriere über jeden Charakter im String
    for char in s:
        # Prüfe, ob der Charakter ein Buchstabe ist
        if char.isalpha():
            # Konvertiere den Buchstaben zu Kleinbuchstaben
            char = char.lower()
            # Aktualisiere die Häufigkeit des Buchstabens im Dictionary
            if char in haeufigkeit:
                haeufigkeit[char] += 1
            else:
                haeufigkeit[char] = 1
    
    # Sortiere das Dictionary alphabetisch nach den Schlüsseln
    haeufigkeit = dict(sorted(haeufigkeit.items()))
    
    return haeufigkeit

# Beispielaufruf der Funktion
resultat = buchstaben_häufigkeit("123Wie g&eht es Ihnen%$?")
print(resultat)