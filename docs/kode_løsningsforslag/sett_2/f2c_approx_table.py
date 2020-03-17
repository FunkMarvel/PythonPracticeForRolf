#Exercise 2.2, Anders P. Åsbø.
F = 0 #defining the startingpoint.
dF = 10 #defining the interval.

print(" F:   |   C:  | C_approx:") #adding header.

while F <= 100: #generating the table.
    C = (5.0/9.0)*(F - 32) #calculating C.
    C_a = (F - 30)/2.0 #approximating C.
    print("%.2f | %.2f | %.2f" % (F,C,C_a)) #printing the table.
    F = F + dF #counting up by one.

#running example:
"""
$ python3 f2c_approx_table.py
 F:   |   C:  | C_approx:
0.00 | -17.78 | -15.00
10.00 | -12.22 | -10.00
20.00 | -6.67 | -5.00
30.00 | -1.11 | 0.00
40.00 | 4.44 | 5.00
50.00 | 10.00 | 10.00
60.00 | 15.56 | 15.00
70.00 | 21.11 | 20.00
80.00 | 26.67 | 25.00
90.00 | 32.22 | 30.00
100.00 | 37.78 | 35.00
"""
