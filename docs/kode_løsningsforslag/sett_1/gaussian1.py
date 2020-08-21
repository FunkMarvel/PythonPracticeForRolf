"""
Oppgave 1.10, kick.py, av Anders P. Åsbø.

Dette programmet evaluerer en gitt Gaussisk fordeling ved en gitt x-verdi.
"""
import numpy as np  # import-komandoer skal stå øverst under doc-stringen.

m = 0  # gjennomsnittsverdi.
s = 2  # standard-avvik.
x = 1  # x-verdi.

# beregner funksjonsverdien. Pass på parantesene!
f = (1.0/(np.sqrt(2*np.pi)*s))*np.exp((-1.0/2) * ((x - m) / s) ** 2)
print("f(%g) = %g" % (x, f))

# kjøreeksempel:
"""
In [8]: run gaussian1.py
f(1) = 0.176033
"""
# tatt på kalkulator får jeg f(1) = 0.176033.
