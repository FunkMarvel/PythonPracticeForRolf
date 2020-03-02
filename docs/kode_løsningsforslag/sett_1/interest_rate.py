p = 5  # 5% interest rate.
A = 1000  # initial amount in euros.
y = 3  # number of years.

B = A*((1 + p/100)**(y))  # new amount after 3 years.
print("After %g years the initial amount has grown to %g€." % (y, B))

# running example:
"""$ python3 interest_rate.py
After 3 years the initial amount has grown to 1157.63€."""
