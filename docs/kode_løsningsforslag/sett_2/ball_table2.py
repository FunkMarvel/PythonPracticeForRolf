# Exercise 2.9, author Anders P. Åsbø.
# I used the 2.8 example solution, from the 1st of september lecture, as a reference when writing the while-loop.
n = 10  # defining the upper limit of the while-loop.
i = 0  # starting point of the while-loop.

v0 = 4.0  # initial speed of the ball in m/s.
g = 1.62  # gravitational acceleration of the moon in (m/s)/s (for fun).

ts = 2.0*v0/g  # final point in time of the ball's lunar adventure.
dt = ts/n  # defining the uniformly-spaced interval for t, such that when i == n, t == ts.

T = []  # empty list for the time-coordinates.
Y = []  # empty list for the space-coordinates.

# converted the lecturer's for-loop (2.8 a) to a while-loop (2.8 b) before modifying it for 2.9.
while i < n + 1:
    t = i*dt  # calculating the time-coordinate,
    T.append(t)  # and adding it to T.
    y = v0*t - (1.0/2.0)*g*(t**2)  # calculating the space-coordinate,
    Y.append(y)  # and adding it to Y.
    i = i + 1  # counting i up by one.

# just adding the headers for my table.
print("%s | %8s" % ("Height in meters:", "Time in seconds:"))
# here's the exercise's for-loop using zip() to run through both lists in parallel.
for t, y in zip(T, Y):
    # printing the rest of the table (the "|" only lines up when y < 10).
    print(" y = %.3fm %7s  t = %.3fs." % (y, "|", t))

# running example:
"""
$ python3 ball_table2.py
Height in meters: | Time in seconds:
 y = 0.000m       |  t = 0.000s.
 y = 1.778m       |  t = 0.494s.
 y = 3.160m       |  t = 0.988s.
 y = 4.148m       |  t = 1.481s.
 y = 4.741m       |  t = 1.975s.
 y = 4.938m       |  t = 2.469s.
 y = 4.741m       |  t = 2.963s.
 y = 4.148m       |  t = 3.457s.
 y = 3.160m       |  t = 3.951s.
 y = 1.778m       |  t = 4.444s.
 y = 0.000m       |  t = 4.938s.
"""
