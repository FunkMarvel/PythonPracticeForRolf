"""
Oppgave 2.9, ball_table.py, av Anders P. Åsbø.

Dette programmet beregner beregner en balls posijon per tid, når den blir sparket rett opp på månen.
Verdiene printes ut i en tabell.
"""
import numpy as np

n = 10  # antall tidssteg.
i = 0  # initial indeks.

v0 = 4.0  # ballens startfart [m/s].
g = 1.62  # månens tyngdeaksellerasjon [m/s**2].

ts = 2.0*v0/g  # sluttverdi for tid [s].
dt = ts/n  # beregner størelsen på tidssteg [s], slik at t == ts når i == n.

T = np.empty(n+1)  # tomt array for tidskoordinater.
Y = np.empty(n+1)  # tomt array for y-koordinater.

# løper gjennom indekser:
while i < n + 1:
    T[i] = i*dt  # beregner tid siden start, og lagrer i array.
    Y[i] = v0*T[i] - (1.0/2.0)*g*(T[i]**2)  # beregner høyde, og lagrer i array.
    i += 1  # øker indeks med 1.

# lager overskrifter for tabell:
print(f"Høyde i meter: | Tid i sekunder:")
# for-løkke løper gjennom begge arrayene med zip():
for t, y in zip(T, Y):
    # printer koordinater til tabell:
    print(f" {y = :.3f} m {'':1s} | {t = :.3f} s.")

# running example:
"""
run ball_table2.py
Høyde i meter: | Tid i sekunder:
 y = 0.000 m   | t = 0.000 s.
 y = 1.778 m   | t = 0.494 s.
 y = 3.160 m   | t = 0.988 s.
 y = 4.148 m   | t = 1.481 s.
 y = 4.741 m   | t = 1.975 s.
 y = 4.938 m   | t = 2.469 s.
 y = 4.741 m   | t = 2.963 s.
 y = 4.148 m   | t = 3.457 s.
 y = 3.160 m   | t = 3.951 s.
 y = 1.778 m   | t = 4.444 s.
 y = 0.000 m   | t = 4.938 s.
"""
