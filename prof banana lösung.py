#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:27:44 2024

@author: lisagerstenberg
"""

def buchstabe_ersetzen(string, buchstabe): #ursprüngliche Funktion definieren
    
    vokale = "aeiou"
    
    def buchstabe_ersetzen(x, y, z): #funktion definiert, und welche Buchstaben geändert werden sollen
        
        x_list = list(x.lower()) #wort des strings klein schreiben und in liste umändern, dann jeder buchstabe ein element. unser Satz wird eine Liste
        # x string von da oben
        
        for i in range(len(x_list)): #für jeden Element in wort wie lange eben Liste ist, werden für alle die Buchstabe y sind
        
            if x_list [i] == y: # wenn Buchstabe in x liste y ist, 
            
                x_list[i] = z #dann wollen wir in dieser Position genau z einsetzen
                
            return "".join(x_list)    #liste wird wieder als String zusammengepastet "" steht für leere Liste 
     
    for v in vokale : #für alle Elemente in string vokalen, print Funktion
            print(buchstabe_ersetzen(x = string, y = buchstabe, z = v), end = " ")
            
buchstabe_ersetzen(string = "italia" , buchstabe = "i")
         

#nicht 2x print Funktion