#Exercise 3.22, Anders P. Åsbø.
def fact(n): #defining my function.
    i = 1
    f = 1
    while i <= n: #this returns 1! = 1 and 0! = 1, so no trickery needed.
        f = f*i #calculating the factorial step by step.
        i = i + 1 #counting up by one.
    return f

n = 70 #the bane of many a calculator.
G = fact(n)
print("%g! = %G" % (n,G)) #printing the result.

def test_fact(): #here we have the test-function.
    n = 4
    expected = 4*3*2*1
    computed = fact(n)
    assert computed == expected
    assert fact(0) == 1
    assert fact(1) == 1

test_fact() #and here we run the test.

#running example:
"""
$ python3 gaussian2.py
70! = 1.19786E+100
"""
