#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:43:17 2024

@author: lisagerstenberg
"""

import numpy as np

E = np.array([[[1,2,3], 
               [4,5,6], 
               [7,8,9]], 
              
              [[9,8,7], 
               [6,5,4], 
               [3,2,1]], 
              
              [[9,8,7], 
               [3,2,1], 
               [6,5,4]]])  #mittelwert in jeder scheibe gleich obwohl zahlen stimmen

print(E.sum(axis = 0))  #summieren entlang 3. Achse, denn wir addieren ersten wert in jeder Zeile (1+9+9, 2+8+8)


print(E.sum(axis = 1))  #summieren die spalten (2+5+8, 1+4+7) summe von jeder SPalte in jeder der Scheiben


print(E.sum(axis = 2))  #summieren horizontal (1+2+3, 4+5+6)

print(E.sum(axis = (1, 2)))
