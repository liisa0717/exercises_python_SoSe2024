
print(2+2)
P = 1 # Principal
t = 1 # Time
i = 1 # Interest
n = 60*24*365
A = P * (1+i/n)**(t*n) # Calculation
print(A)

from math import exp
print(exp(1))

def carg_berechnung (AK, EK, t):
    carg = ((EK/AK) ** (1/t)-1)
    AK = 100
    EK = 700
    t = 30
    return(carg)
    