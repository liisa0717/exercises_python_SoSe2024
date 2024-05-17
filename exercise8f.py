# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:10:55 2024

@author: s_gerstenberg22
"""

def vokon_zählen(text):
    vokale = "aeiou"
    konsonanten_count = 0
    vokale_count = 0
    for buchstabe in text():
        if buchstabe.isalpha():
            if buchstabe in vokale:
               vokale_count += 1
        else:
            konsonanten_count+= 1        
    return konsonanten_count, vokale_count

print(f"Die Anzahl der Konsonanten beträgt {len(konsonanten_count)} und die Anzahl der Vokale ist {len(vokale_count)}")
vokon_zählen("Berlin")




          