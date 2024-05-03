# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:20:41 

@author: s_gerstenberg22
"""
import matplotlib.pyplot as plt

a = 1
r = 0.5
n = 10
s_n = []
summe = 0

for k in range (0, n):
    summe += a * (r**k)
    s_n.append(summe)

print(s_n)

plt.plot(s_n)


def spar_funktion(AK, SR, i, lz):
  
    gesamt_entwicklung = []
    aktuelles_Kapital = AK
    for k in range(1, lz+1) :
        aktuelles_Kapital = SR + aktuelles_Kapital*(1 + i)
       kapital_entwicklung.append(aktuelles_Kapital)
    
    return kapital_entwicklung

print(spar_funktion(AK=10000, SR=1000, i=0.01, lz=10))