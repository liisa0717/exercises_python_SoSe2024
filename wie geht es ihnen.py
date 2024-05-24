#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:42:30 2024

@author: lisagerstenberg
"""

def buchstaben_ändern(string = "Wie geht es Ihnen?", alter_buchstabe = "e", neuer_buchstabe = "a"):
    ergebnis = ""
    
    for charg in string:
        if charg.lower() == alter_buchstabe.lower():
            ergebnis += neuer_buchstabe
        else:
            ergebnis += charg
    return ergebnis

print(buchstaben_ändern("Wie geht es Ihnen?", "e", "a"))
        
            
