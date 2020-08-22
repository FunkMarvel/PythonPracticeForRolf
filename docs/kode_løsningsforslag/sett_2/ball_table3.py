# Exercise 2.17, author Anders P. Åsbø.

import numpy as np
# solution to a):
# using the same code as in 2.9 to generate the t and y values.

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

ty1 = np.empty((2, n+1))  # creating nested array 1.
ty1[0, :] = T
ty1[1, :] = Y

print("a)" '\n' "t:  |y:")  # adding headers.
for i in range(len(ty1[0])):  # printing the table from a nested list with columns.
    print(f"{ty1[0, i]:.2f}|{ty1[1, i]:.2f}")

print("\n---------\n")  # adding a break between the two running examples.

# solution to b):
ty2 = np.empty((n+1, 2))  # creating nested list 2.

ty2[:, 0] = T
ty2[:, 1] = Y

print("b)" '\n' "t:  |y:")  # adding headers.
for i in range(len(ty2)):  # printing the table from a nested list with rows.
    print(f"{ty2[i, 0]:.2f}|{ty2[i, 1]:.2f}")

# running examples:
"""
$ python3 ball_table3.py
a)
t:  |y:
0.00|0.00
0.49|1.78
0.99|3.16
1.48|4.15
1.98|4.74
2.47|4.94
2.96|4.74
3.46|4.15
3.95|3.16
4.44|1.78
4.94|0.00
---------
b)
t:  |y:
0.00|0.00
0.49|1.78
0.99|3.16
1.48|4.15
1.98|4.74
2.47|4.94
2.96|4.74
3.46|4.15
3.95|3.16
4.44|1.78
4.94|0.00
"""
