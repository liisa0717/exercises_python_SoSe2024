#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:26:16 2024

@author: lisagerstenberg
"""

def vokon_zählen(wort):
    wort_lower = wort.lower()
    vokale = "aeiou"
    
    konsonanten = [k for k in wort_lower if k.isalpha and k not in vokale]
    vokale =  [v for v in wort_lower if v.isalpha and v in vokale]   
    
    anzahl_vokale = len(vokale)
    anzahl_konsonanten = len(konsonanten)
    
    return anzahl_konsonanten, anzahl_vokale

anzahl_vokale, anzahl_konsonanten = vokon_zählen("Berlin")

print(f"Es gibt {anzahl_vokale} Vokale und {anzahl_konsonanten}")