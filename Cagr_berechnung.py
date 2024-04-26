# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:46:11 2024

@author: s_gerstenberg22
"""

def carg_berechnung (AK, EK, t):
   AK_abs = abs(AK)
   t_abs = abs(t)
   cagr = ((EK/AK_abs)**(1/t_abs)-1)
   return cagr

print(carg_berechnung(100, 700, 30))
    
AK = 120
t = 30
cagr = carg_berechnung(100, 700, 30)
EK = AK * (1 + cagr) ** t 

print(EK)
