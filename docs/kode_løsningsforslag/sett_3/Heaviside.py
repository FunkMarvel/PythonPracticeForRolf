#Exercise 3.29, Anders P. Åsbø.
#a)
def H(x): #defining my function.
    if x < 0: #first part of the defenition.
        H = 0
    else: #second part.
        H = 1
    return H

#b)
def test_H():
    ex1 = 0; ex2 = 0; ex3 = 1; ex4 = 1; ex5 = 1 #expected results.
    c1 = H(-10); c2 = H((-10)**(-15)); c3 = H(0); c4 = H(10**15); c5 = H(10) #computed results.
    assert c1 == ex1; assert c2 == ex2; assert c3 == ex3; assert c4 == ex4; assert c5 == ex5 #evaluating.

test_H() #running the test.

print("H(%g) = %g." % (256,H(256))) #testing to see what it prints.
print("H(%g) = %g." % (-256,H(-256)))

#running example:
"""
$ python3 Heaviside.py
H(256) = 1.
H(-256) = 0.
"""
