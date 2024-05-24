#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:20:59 2024

@author: lisagerstenberg
"""

import numpy as np

M = np.eye(5, dtype="int") #int brauchen wir, damit Kommda zwischen Zahlen ist

M[3:, :2] = 2 #Spalte 3- Ende sprechen wir an, wir wollen ändern spalte 0 und spalte 1 zu wert 2
M[ :2, 3: ] = 3 #Zeile 0-2  und ab Spalte 3

print(M)

