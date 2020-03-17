#Exercise 3.8, Anders P. Åsbø.
def triangle_area(vertices): #defining my function.
    A = (0.5)*(abs(vertices[1][0]*vertices[2][1] \
    - vertices[2][0]*vertices[1][1] \
    - vertices[0][0]*vertices[2][1] \
    + vertices[2][0]*vertices[0][1] \
    + vertices[0][0]*vertices[1][1] \
    - vertices[1][0]*vertices[0][1] ))
    return A

def test_triangle_area(): #defining the test-function.
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = ('computed area = %g != %g (expected)' % (computed, expected))
    assert success, msg

test_triangle_area() #running the test.

v1 = (4,5); v2 = (1,0); v3 = (9,2) #testing with a arbitrary triangle.
vertices = [v1,v2,v3]
A = triangle_area(vertices)
print("The area of the triangle is %g." % A)

#running example
"""
$ python3 area_triangle.py
The area of the triangle is 17.
"""
