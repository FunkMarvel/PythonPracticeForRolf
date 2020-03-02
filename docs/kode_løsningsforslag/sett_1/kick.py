import numpy as np  # woop.

# variables:
q = 1.2  # air density in kg/m**3
a = 0.11  # radius of the ball, 11 cm in meters.
A = np.pi*a**2.0  # area of the cross section.
C_d = 0.4  # drag coefficient.
m = 0.43  # weight of the ball in kg.
g = 9.81  # gravitational acceleration of earth in m/s**2.
V_1 = 120.0/3.6  # hard kick-speed converted from 120 km/h to V_1 m/s.
V_2 = 30.0/3.6  # soft kick-speed converted from 30 km/h to V_2 m/s.

# calculating the forces:
F_d1 = (1.0/2)*C_d*q*A*(V_1**2)  # calculating drag force for hard kick-speed.
F_d2 = (1.0/2)*C_d*q*A*(V_2**2)  # calculating drag force for soft kick-speed.
G = m*g  # calculating gravity force.
R1 = F_d1/G  # calculating ratio nr. 1.
R2 = F_d2/G  # calculating ratio nr. 2.
print("In both cases the force of gravity is %.1fN." % G)
print("The hard kick gives a drag force of %.1fN, with a ratio between it and the gravitational force of %.1f" % (F_d1, R1))
print("The soft kick gives a drag force of %.1fN, with a ratio between it and the gravitational force of %.1f" % (F_d2, R2))

# running example:
"""$ python3 kick.py In both cases the force of gravity is 4.2N.
The hard kick gives a drag force of 10.1N, with a ratio between it and the gravitational force of 2.4
The soft kick gives a drag force of 0.6N, with a ratio between it and the gravitational force of 0.2"""
