# Exercise 3.8, Anders P. Åsbø.

# a)
import numpy as np  # importerer kvadratrot fra NumPy biblioteket.
# grunnen til at jeg ikke bruker 'from math import sqrt', er fordi
# math.sqrt ikke takler negative tall.


def R(a, b, c):
    """Returnerer røttene til et andregradspolynom.

    Argumenter:
    a -- float: andregradskoeffisienten.
    b -- float: førstegradskoeffisienten.
    c -- float: konstantleddet.
    """
    q = b**2 - 4*a*c

    # hvis q < 0, så endrer jeg datatypen dens til komplekst tall,
    # slik at numpy.sqrt ikke gir error:
    if q < 0:
        q = complex(q)

    # regner ut røttene med andregradsformelen.
    R1 = (-b + np.sqrt(q))/(2*a)
    R2 = (-b - np.sqrt(q))/(2*a)
    return R1, R2  # returnerer røttene i en tuppel.


# b)
R1_R2 = R(1, 2, 1)  # sjekker reelle røtter.
print("b)", "Solving x² + 2x + 1.", "It should be x = -1 for both roots.",
      "My function returns:", R1_R2, sep='\n')

print(" ")

R1_R2 = R(1, 2, 2)  # sjekker komplekse røtter, leg merke til at j = sqrt(-1).
print("Solving x² + 2x + 2.",
      "The roots should be x1 = (-1 + j) and x2 = (-1 - j).",
      "My function returns:", R1_R2, sep='\n',)

# kjøreeksempel:
"""
In [14]: run roots_quadratic.py
b)
Solving x² + 2x + 1.
It should be x = -1 for both roots.
My function returns:
(-1.0, -1.0)

Solving x² + 2x + 2.
The roots should be x1 = (-1 + j) and x2 = (-1 - j).
My function returns:
((-1+1j), (-1-1j))
"""
