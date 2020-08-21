"""
Oppgave 1.11, kick.py, av Anders P. Åsbø.

Dette programmet beregner tyngde- og luftmotstandskraft på en ball av
masse m sparket med starthastighet V_1 og V_2.
"""
from numpy import pi  # importerer bare det jeg skal bruke.

q = 1.2  # lufttetthet [kg/m**3].
a = 0.11  # radius til ball [m].
A = pi*a**2.0  # tversnittareal [m**2].
C_d = 0.4  # luftmotstandskonstant.
m = 0.43  # masse til ball [kg].
g = 9.81  # jordas tyngdeaksellerasjon [m/s**2].
V_1 = 120.0/3.6  # ballens fart ved hardt spark [m/s].
V_2 = 30.0/3.6  # ballens fart ved svakt spark [m/s].

F_d1 = (1.0/2)*C_d*q*A*(V_1**2)  # luftmotstandskraft ved høy fart [N].
F_d2 = (1.0/2)*C_d*q*A*(V_2**2)  # luftmotstandskraft ved lav fart [N].
G = m*g  # ballens tyngde [N].
R1 = F_d1/G  # luftmotstand per tyngde for høy fart.
R2 = F_d2/G  # luftmotstand per tyngde for lav fart.
print(f"Ballens tyngde er {G = :.1f} N.")
print(f"Hardt spark gir {F_d1 = :.1f} N, og F_d1/G = {R1:.1f}")
print(f"Svakt spark gir {F_d2 = :.1f} N, og F_d2/G = {R2:.1f}")

# kjøreeksempel:
"""
In [7]: run kick.py
Ballens tyngde er G = 4.2 N.
Hardt spark gir F_d1 = 10.1 N, og F_d1/G = 2.4
Svakt spark gir F_d2 = 0.6 N, og F_d2/G = 0.2
"""
