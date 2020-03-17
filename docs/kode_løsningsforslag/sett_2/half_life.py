# Exercise 1.3, author Anders P. Åsbø.
# solution to a):
from math import exp, log  # only importing what I need has been duly noted.


def N(t):  # function calculating remaining mass after t seconds of nuclear decay.
    N = N_0*(exp(-t/T))
    return N


N_0 = 4.5  # initial mass of carbon-11 in kg.
T = 1760  # the time-constant of carbon-11 in s.
t = 10*60  # 10 min converted to seconds.
R = N(t)  # calculating the answer.

print("a)" '\n' "%.2fkg of carbon-11 remains after 10 min." % R)

# adding a break between the two running examples.
print("-------------------------------------------------")

# solution to b):


def T(t_half):  # function calculating the time-constant.
    T = (t_half)/(log(2))
    return T


t_half = 1220  # the half-life of carbon-11 in s.
N_0 = 4.5  # initial mass of carbon-11 in kg.
T = T(t_half)  # calculating the time-constant of carbon-11 in s.

print("b)" '\n' "The time-constant of carbon-11 is %.0f seconds." '\n' "%.2fkg of carbon-11 remains after 10 min." % (T, R))

# running example:
"""
$ python3 half_life.py
a)
3.20kg of carbon-11 remains after 10 min.
-------------------------------------------------
b)
The time-constant of carbon-11 is 1760 seconds.
3.20kg of carbon-11 remains after 10 min.
"""
