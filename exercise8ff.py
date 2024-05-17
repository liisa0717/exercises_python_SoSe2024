# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:33:26 2024

@author: s_gerstenberg22
"""

def vokon_zählen(wort):
    vokale = "aeiou"
    wort_lower = wort.lower()
    
    buchstaben = [i for i in wort_lower if i.isalpha()]
    vokale = [k for k in wort_lower if k in vokale]
    
    print(f"Es gibt {len(vokale)} Vokalen und {len(buchstaben) - len(vokale)} Konsonanten")
    
    vokon_zählen("Berlin")
   