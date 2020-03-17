#Exercise 3.8, Anders P. Åsbø.
#a)
from numpy.lib.scimath import sqrt #importing the sqrt function from numpy.

def R(a,b,c): #defining my function.
    R1 = ((-b) + (sqrt((b**2)-4*a*c)))/(2*a) #using the quadratic formula.
    R2 = ((-b) - (sqrt((b**2)-4*a*c)))/(2*a)
    return (R1,R2) #returning the roots as a tuple (or point in the complex 4D space).

#b)
R2 = R(1,2,1) #testing for real roots with a known example.
print("b) \n Solving x² + 2x + 1. \n It should be x = -1 for both roots. \n My function returns:")
print(R2)

print(" ")

R3 = R(1,2,2) #testing for complex roots with a known example.
print("Solving x² + 2x + 2. \n The roots should be x1 = (-1 + j) and x2 = (-1 - j). \n My function returns:")
print(R3)

#running example:
"""
$ python3 roots_quadratic.py
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
