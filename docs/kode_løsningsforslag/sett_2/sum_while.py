# Exercise 2.11, author Anders P. Åsbø.
"""
s = 0; k = 1; M = 100 #integer division when it should be float division, but not a problem in python 3.

while k < M: #k should be smaler than or equal to M, not just smaler than.
    s += 1/k #this is a while loop, but the loop block misses a statement which increases k by 1 each time it loops.

print s #python 2 syntax won't work in python 3
"""

# my atempt at fixing this code:
s = 0
k = 1.0
M = 100.0  # making each number float, just in case.

while k <= M:  # with <= the sum is actually equal to the expression we're trying to compute.
    s += 1.0/k  # again with the float.
    k = k + 1  # count k up by one.

print(s)  # format the syntax for python 3, and run.

# running example:
"""
$ python3 sum_while.py
5.187377517639621
"""
